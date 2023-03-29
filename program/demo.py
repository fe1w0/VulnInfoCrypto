import yaml
import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import re

SEARCH_MITRE_URL = "https://cve.mitre.org/cgi-bin/cvekey.cgi?"

MAX_WORKERS = 10  # 最大线程数

LOCAL_PROXIES={
    "http" : "http://127.0.0.1:7890",
    "https" : "http://127.0.0.1:7890"
    }

BLACK_LIST = ["cpabe toolkit", "Apache Commons Crypto", "Paillier Library", "PBC Library"]

RESULT = {}

FINAL_NUMBER = 0

lock = threading.Lock()  # 锁，防止结果同时写入

def read_software_info():
    with open('sources/software.yml', 'r') as f:
        software_data = yaml.safe_load(f)
    return software_data

def parse_response_info(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # cve_number
    div = soup.find('div', {'class': 'smaller', 'style': 'background-color:#e0dbd2; padding:3px; border:1px solid #706c60; margin-bottom:10px'})
    b = div.find('b')
    cve_number = int(b.text)
    
    # cve_list
    cve_list = []
    cve_re = re.compile(r'^CVE-\d{4}-\d{4,}$')  # 匹配CVE编号的正则表达式
    tr_list = soup.find_all('tr')
    for tr in tr_list:
        a = tr.find('a')
        if a is not None:
            cve_id = a.text
            if cve_re.match(cve_id):
                cve_list.append(cve_id)
    return cve_number, cve_list

def search_cve_from_mitre(soft_name, session, semaphore):
    semaphore.acquire()  # 获取信号量
    global FINAL_NUMBER
    try:
        search_url = SEARCH_MITRE_URL + urlencode({"keyword" : soft_name})
        res = session.get(search_url, proxies=LOCAL_PROXIES)
        cve_number, cve_list = parse_response_info(res)
        with lock:
            RESULT[soft_name] = {"number": cve_number, "cve_list": cve_list}
            FINAL_NUMBER = FINAL_NUMBER + cve_number
    except Exception as e:
        print(f"{soft_name}查询失败：{e}")
    finally:
        semaphore.release()  # 释放信号量

def main():
    # init: get software information
    software_info = read_software_info()
    session = requests.Session()  # 创建session对象
    semaphore = threading.Semaphore(MAX_WORKERS)  # 创建信号量
    futures = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        for software_item in software_info:
            if software_item['name'] in BLACK_LIST:
                continue
            futures.append(executor.submit(search_cve_from_mitre, software_item['name'], session, semaphore))
    for future in as_completed(futures):
        pass
    
    print(FINAL_NUMBER)
    with open('output/result.yaml', 'w') as f:
        yaml.dump(RESULT, f, indent=4, sort_keys=False)

if __name__ == "__main__":
    main()