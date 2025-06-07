#!/usr/bin/env python3
import sys
import yaml
import requests
import os
import glob

def send(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    url = os.environ['GAS_WEBAPP_URL']
    response = requests.post(url, json=data)
    print(f"[{file_path}] → {response.status_code}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # 引数があればそのファイルを使う
        for path in sys.argv[1:]:
            send(path)
    else:
        # 引数がなければ listings/*.yaml から最新ファイルを使う
        files = glob.glob('listings/*.yaml')
        if not files:
            print("⚠️ listings/ に YAML ファイルがありません。")
            sys.exit(1)
        latest_file = max(files, key=os.path.getctime)
        print(f"📄 最新ファイルを送信します: {latest_file}")
        send(latest_file)
