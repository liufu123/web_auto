import requests
import json





r = requests.get("https://www.baidu.com")
print(r.status_code)
print(r.text)
