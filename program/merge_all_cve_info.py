import yaml


def read_yaml_info(file_name):
    with open(file_name, 'r') as f:
        file_info = yaml.safe_load(f)
    return file_info


def main():
    file_name = "output/result.yml"
    yml_result = read_yaml_info(file_name)
    
    result_cves = []
    
    for product in yml_result:
        for cve in yml_result[product]['cve_list']:
            result_cves.append(cve)
        
    file_name = "output/cwe_result.yml"
    yml_cwe_result = read_yaml_info(file_name)
    
    for cwe in yml_cwe_result:
        for cve in yml_cwe_result[cwe]:
            result_cves.append(yml_cwe_result[cwe][cve]['cve_id'])
    
    print(len(result_cves))
        
if __name__ == "__main__":
    main()