#!/usr/bin/python3
import requests

response = requests.get('http://127.0.0.1:5000/top10vulnerabilities?hostip=10.128.35.79')
print(response.json())

