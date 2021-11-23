from bs4 import BeautifulSoup
import requests
from dbutils.pooled_db import PooledDB
from dbutils.persistent_db import PersistentDB
import pymysql
config = {
    'host':'127.0.0.1',
    'port':3306,
    'database':'douban',
    'user': 'root',
    'password':'',
    'charset':'utf8'
}

def get_db_pool(is_mult_thread):
    if is_mult_thread:
          poolDB = PooledDB(
            # 指定数据库连接驱动
            creator=pymysql,
            # 连接池允许的最大连接数,0和None表示没有限制
            maxconnections=5,
            # 初始化时,连接池至少创建的空闲连接,0表示不创建
            mincached=5,
            # 连接池中空闲的最多连接数,0和None表示没有限制
            maxcached=5,
            # 连接池中最多共享的连接数量,0和None表示全部共享(其实没什么卵用)
            maxshared=3,
            # 连接池中如果没有可用共享连接后,是否阻塞等待,True表示等等,
            # False表示不等待然后报错
            blocking=True,
            # 开始会话前执行的命令列表
            setsession=[],
            # ping Mysql服务器检查服务是否可用
            ping=0,
            **config
        )

    else:
        poolDB = PersistentDB(
        #指定数据库连接驱动
        creator = pymysql,

        #一个连接最大复用次数,0或者None表示没有限制,默认为0
        maxusage =1000,
        **config
        )
    return poolDB
# 把数据写入数据库
def lode(name,list):
    conn = db_pool.connection()
    cursor = conn.cursor()
    for i in list:
        sql = "INSERT INTO %s VALUES('%s','%s','%s');" % (name,i[0],i[1],i[2])
        try :
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
           
            conn.rollback()
            
    conn.close()

#创建表
def create_table(name):
    
    conn = db_pool.connection()
    cursor = conn.cursor()
    sql ='''CREATE TABLE %s(
	title  CHAR(100) PRIMARY KEY,
	url CHAR(100),
	date CHAR(100)
	);'''%(name)
    try :
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    conn.close()

url = 'http://www.qianlima.com/zb/area_305/'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}

html = requests.get(url=url,headers=header).content.decode()
sug = BeautifulSoup(html,'lxml')
list = []

inform_div = sug.find('div',id='zbyg')
infrom_dl = inform_div.find_all('dl')

for i in infrom_dl:
    one = []
    title = i.a.get('title')
    one.append(title)
    url = i.a.get('href')
    one.append(url)
    date = i.dd.string
    one.append(date)

    list.append(one)

db_pool = get_db_pool(True)
# 从数据库连接池中取出一条连接
conn = db_pool.connection()
cursor = conn.cursor()

db_pool = get_db_pool(True)
create_table('xiangmu4')
lode('xiangmu4',list)


db_pool.close()