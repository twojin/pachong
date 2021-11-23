import os
from bs4 import BeautifulSoup
import requests
url = 'http://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/?focus=book'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}

html = requests.get(url=url,headers=header).content.decode()
sug = BeautifulSoup(html,'lxml')

list = []
list.append(['书名','第一作者','出版年月'])

inform_div = sug.find('div',class_='mod-list book-list')
inform_dl = inform_div.find_all('dl')

for dl in inform_dl:
    one =[]
    l = dl.dd
    title = l.a.string
    one.append(title.replace('\n', '').replace('\r', ''))
    ldl = l.div.string
    ldl2 =ldl.split(' / '.replace('\n', '').replace('\r', ''))
    one.append(ldl2[0])
    if ldl2[2].find('-')>=0:
        one.append(ldl2[2])
    else:
        one.append(ldl2[3])
    list.append(one)

for i in list:
     with open(os.path.join('test','093119101-2'+'.txt'),'a+',encoding='utf-8') as f:
        for j in i:
            f.write(j+'   ')
        f.write('\n')
        