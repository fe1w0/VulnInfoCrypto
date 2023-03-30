import yaml
from urllib.parse import urlencode
import requests
from lxml import html
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

if __name__ == "__main__":
    with open('output/cwe_result.yml', 'r') as f:
        file_data = yaml.safe_load(f)
    number = 0
    for item in file_data:
        number = number + len(file_data[item])
    print(number)
         