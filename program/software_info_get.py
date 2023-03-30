import yaml
import requests
from urllib.parse import urlencode
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from lxml import html

SEARCH_MITRE_URL = "https://cve.mitre.org/cgi-bin/cvekey.cgi?"

MAX_WORKERS = 10  # 最大线程数

LOCAL_PROXIES={
    "http" : "http://127.0.0.1:7890",
    "https" : "http://127.0.0.1:7890"
    }

BLACK_LIST = ["cpabe toolkit", "Apache Commons Crypto", "Paillier Library", "PBC Library"]

RESULT = {}

FINAL_NUMBER = 0

# 避免重复
TOTAL_CVE_LIST = []

lock = threading.Lock()  # 锁，防止结果同时写入

def read_software_info():
    with open('sources/software.yml', 'r') as f:
        software_data = yaml.safe_load(f)
    return software_data

def parse_response_info(response):
    cve_list = {}
    
    soup = html.fromstring(response.content)       
    
    # 使用 XPath 选择器定位表格元素
    table = soup.xpath("//div[@id='TableWithRules']//table")[0]

    # 定位表格头行和数据行
    header_row, *data_rows = table.xpath(".//tr")

    # 获取表格头单元格（表格的第一行）的文本内容
    headers = [cell.text_content().strip() for cell in header_row.xpath(".//th")]

    # 获取所有数据行的文本内容
    data = [[cell.text_content().strip() for cell in row.xpath(".//td")] for row in data_rows]
    
    result = [dict(zip(headers, row)) for row in data]
    
    for item in result:
        cve_list[item['Name']] = item
           
    cve_number = len(cve_list)
    return cve_number, cve_list

def append_all_item(total_list, array):
    for item in array:
        total_list.append(item)

def search_cve_from_mitre(soft_name, session, semaphore):
    semaphore.acquire()  # 获取信号量
    global TOTAL_CVE_LIST
    try:
        search_url = SEARCH_MITRE_URL + urlencode({"keyword" : soft_name})
        res = session.get(search_url, proxies=LOCAL_PROXIES)
        cve_number, cve_list = parse_response_info(res)
        with lock:
            RESULT[soft_name] = {"number": cve_number, "cve_list": cve_list}
            # TOTAL_CVE_LIST.append(cve_list)
            append_all_item(TOTAL_CVE_LIST, cve_list)
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
    
    with open('output/result.yml', 'w') as f:
        yaml.dump(RESULT, f, indent=4, sort_keys=False)

if __name__ == "__main__":
    main()
    print(len(TOTAL_CVE_LIST))