import os
from bs4 import BeautifulSoup
import requests
url = 'https://cse.cslg.edu.cn/info/1090/3298.htm'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}

html = requests.get(url=url,headers=header).content.decode()
sug = BeautifulSoup(html,'lxml')
list = []

# inform_tbody = sug.find('table',class_='table-responsive')
# print(inform_tbody)
print(html) ####