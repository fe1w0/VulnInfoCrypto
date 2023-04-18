import yaml
from urllib.parse import urlencode
import requests
from lxml import html
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

if __name__ == "__main__":
    classification_data = {}
    
    with open('sources/cwe_classification.yml', 'r', encoding='utf-8') as f:
        cwe_classification = yaml.safe_load(f)
        
    with open('output/cwe_result.yml', 'r', encoding='utf-8') as f:
        cwe_result = yaml.safe_load(f)
        
    for item in cwe_classification:
        number = 0
        classification_data[str(item)] = {}
        classification_data[str(item)]['number'] = number
        for cwe in cwe_classification[item]:
            cwe_name = str(list(cwe.keys())[0])
            number += len(cwe_result.get(cwe_name, []))
            classification_data[str(item)][cwe_name] = cwe_result.get(cwe_name, [])
            classification_data[str(item)]['number'] = number
        
    with open('output/classification_data.yml', 'w', encoding='utf-8') as f:
        yaml.dump(classification_data, f, indent=4, sort_keys=False, allow_unicode=True)