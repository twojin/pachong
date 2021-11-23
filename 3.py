import os
from bs4 import BeautifulSoup
import requests
url = 'http://lib.cslg.edu.cn/'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}

html = requests.get(url=url,headers=header).content.decode('gbk')
sug = BeautifulSoup(html,'lxml')
list = []
list.append('读者服务项目	链接')

inform_ul = sug.find_all('ul',class_='search-select-list')

inform_li = inform_ul[1].find_all('li')
for i in inform_li:
    a_lin = i.a
    title = a_lin.get('title')
    url = a_lin.get('href')
    list.append(title +'   '+url)

for i in list:
     with open(os.path.join('test','093119101-3'+'.txt'),'a+',encoding='utf-8') as f:
        f.write(i + '\n')

