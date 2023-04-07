from bs4 import BeautifulSoup
import json
import numpy as np
import requests
import os
import re
import time
headers = {
    'content-type': 'text/html; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/111.0.0.0 Safari/537.36'}
arr = os.listdir()
print(arr)
list_total_question = []
for x in arr:
    if x.endswith('.md'):
        with open(x,'r',encoding='utf8') as hot_diary:
            pattern = r'https://www.zhihu.com/question/(\d+)'
            list_total_question+=re.findall(pattern, hot_diary.read())
print(len(list_total_question))
list_all_url = []
for x in list_total_question:
    a1 = time.time()
    url = 'https://www.zhihu.com/api/v4/questions/'+str(x)+'/feeds?'
    datas = requests.get(url,headers=headers).json()
    for info in datas['data']:
        answerid = info['target']['id']
        final_url = 'https://www.zhihu.com/question/'+x+'/answer/'+str(answerid)
        list_all_url.append(final_url)
        #break #每条问题默认提取五条问答，此处Break则只选默认排序第一条
    a2 = time.time()
    print(a2-a1) #0.5s
    break #选一条问题进行测试
print(list_all_url)
list_json = []
for x in list_all_url:
    html = requests.get(url=x, headers=headers)
    site = BeautifulSoup(html.text, 'lxml')
    title = site.find_all('meta', attrs={'itemprop': "name"}, recursive=True, limit=1)[0].__getattribute__('attrs')[
        'content']
    text = site.find('div', attrs={'class': "RichContent-inner"})
    print(title)
    total_string = ""
    for i in text:
        if i.text.find('.css') == -1:
            total_string += i.text
    dict_json = {"instruction":title,"input":"","output":total_string}
    list_json.append(dict_json)
print(list_json)    
    
# urls = ['https://www.zhihu.com/api/v4/questions/593952517/feeds?']
# data = {}

# for url in urls:
#     # 1. Obtain the response: