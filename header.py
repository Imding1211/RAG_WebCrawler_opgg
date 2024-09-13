import requests

headers = {'Accept-Language': 'zh-TW,zh;q=0.9'}

URL = "https://www.op.gg/champions"

response = requests.get(URL, headers=headers)
print(response.text)  # 打印出中文版本的 HTML 內容