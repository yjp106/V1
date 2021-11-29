import requests
import re


headers = {'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}   #用户代理   若无 一些网站会禁止访问

#爬取网页通用代码框架
def getHTMLText(url,headers):
    try:
        r = requests.get(url,headers=headers)
        r.raise_for_status()         #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "https://item.jd.com/10030493404006.html"
    print(getHTMLText(url,headers))


