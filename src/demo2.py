import requests

headers = {'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}   #用户代理   若无 一些网站会禁止访问

r = requests.get('https://www.amazon.cn',headers=headers)
print(r.encoding)
r.encoding = r.apparent_encoding
#print(r.text)
print(r.request.headers)