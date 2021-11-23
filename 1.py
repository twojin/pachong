from bs4 import BeautifulSoup
import os
html = '''<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
sug = BeautifulSoup(html,'lxml')

list = []
list.append('Title	Url')

inform = sug.find_all('li')

for li in inform:
    a_li = li.a
    link = a_li.get('href')
    infor = li.string
    to =infor + '  ' +link
    list.append(to)

for i in list:
     with open(os.path.join('test','093119101-1'+'.txt'),'a+',encoding='utf-8') as f:
        f.write(i + '\n')
