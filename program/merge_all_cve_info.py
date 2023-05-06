import yaml
import re
from collections import defaultdict
import matplotlib.pyplot as plt

def read_yaml_info(file_name):
    with open(file_name, 'r') as f:
        file_info = yaml.safe_load(f)
    return file_info


def get_year_from_cve_id(cve_id):
    year_match = re.search(r'CVE-(\d{4})-', cve_id)
    if year_match:
        year = int(year_match.group(1))
    else:
        # Handle the case where no year is found
        year = None
    return year


def get_picture(cve_counts):
    plt.bar(cve_counts.keys(), cve_counts.values())
    plt.xlabel('Year')
    plt.ylabel('CVE Count')
    plt.title('Number of CVEs per Year')
    plt.show()
        

def main():
    cve_counts = defaultdict(int)
    
    file_name = "output/result.yml"
    yml_result = read_yaml_info(file_name)
    
    result_cves = []
    
    for product in yml_result:
        for cve in yml_result[product]['cve_list']:
            result_cves.append(cve)
        
    file_name = "output/cwe_result.yml"
    yml_cwe_result = read_yaml_info(file_name)
    
    # for cwe in yml_cwe_result:
    #     for cve in yml_cwe_result[cwe]:
    #         result_cves.append(yml_cwe_result[cwe][cve]['cve_id'])
        
    for cve_id in result_cves:
        cve_year = get_year_from_cve_id(cve_id)
        cve_counts[cve_year] += 1
        
    get_picture(cve_counts)
        
if __name__ == "__main__":
    main()