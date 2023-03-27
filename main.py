# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import urllib.request as url
import requests
import re

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 参数的使用
    data = {
        'name': 'germey',
        'age': 25
    }
    r = requests.get('https://www.httpbin.org/get', params=data)
    print(r.text)

    # 抓取网页
    r = requests.get('https://ssr1.scrape.center/')
    pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
    titles = re.findall(pattern, r.text)
    [print(title) for title in titles]

    # 抓取二进制
    r = requests.get('https://scrape.center/favicon.ico')
    print('图片二进制内容：', r.content)
    with open('favicon.ico', 'wb') as f:
        f.write(r.content)
        print('保持图片为:' + 'favicon.ico')
