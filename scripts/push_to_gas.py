#!/usr/bin/env python3
import sys
import yaml
import requests
import os

def send(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    url = os.environ['GAS_WEBAPP_URL']
    response = requests.post(url, json=data)
    print(response.status_code)

if __name__ == '__main__':
    for path in sys.argv[1:]:
        send(path)
