import requests

'''
搜索引擎关键词提交

百度关键词接口   http://www.baidu.com/s?wd=keyword
360关键词接口    http://www.so.com/s?q=keyword
替换keyword
'''

headers = {'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}   #用户代理   若无 一些网站会禁止访问
kv = {'wd':'陕西省'}
#爬取网页通用代码框架
def getHTMLText(url,headers):
    try:
        r = requests.get(url,params=kv)
        r.raise_for_status()         #如果状态不是200，引发HTTPError异常
        print(r.request.url)
        r.encoding = r.apparent_encoding
        return r.text[0:1000]
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "http://www.baidu.com/s"
    print(getHTMLText(url,headers))


