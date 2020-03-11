### 一、存入MongoDB

- ​	在Setting文件中配置

```
MONGODB 主机名
MONGODB_HOST = '127.0.0.1'
MONGODB 端口号
MONGODB_PORT= 27017
数据库名称
MONGODB_DBNAME = "Douban"
存储数据的表名称
MONGODB_SHEETNAME= "doubanmovies"
```



- 管道文件

```python
import pymongo
from scrapy.conf import settings
class DoubanPipeline(object):
    # 将数据存储在mongodb中
    def __init__(self,host,port,dbname,sheetname):
        # 创建MONGODB数据库链接
        client = pymongo.MongoClient(host=host, port=port)
        # 指定数据库
        mydb = client[dbname]
        # 存放数据的集合名称
        self.mysheet = mydb[sheetname]
    @classmethod
    def from_crawler(cls, crawler):
        host = crawler.settings["MONGODB_HOST"]
        port = crawler.settings["MONGODB_PORT"]
        dbname = crawler.settings["MONGODB_DBNAME"]
        sheetname = crawler.settings["MONGODB_SHEETNAME"]
    
        return cls(host,port,dbname,sheetname)
    def process_item(self,item,spider):
        data = dict(item)
        # mongodb数据插入语句，使用save保存数据的效率会很慢，因为它需要循环便利，操作费时
        self.mysheet.insert(data)
        return item

```

### 二、存入Mysql

- 在Setting文件中配置

```

#关于数据库的相关配置
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = ''
MYSQL_PWD = ''
MYSQL_DB = ''
```

- 管道文件

```python
import pymysql
class DoubanPipeline(object):
#     将数据存储值mysql数据库
#     _mysql_exceptions.OperationalError: (1366, 是因为数据库中的字符集与charset="utf8"不符合
    def __init__(self,host,port,user,pwd,db,charset):
        self.client = pymysql.Connect(host,user,pwd,db,port,charset='utf8')
        self.cursor = self.client.cursor()
    
    @classmethod
    def from_crawler(cls,crawler):
        host = crawler.settings['MYSQL_HOST']
        port = crawler.settings['MYSQL_PORT']
        user = crawler.settings['MYSQL_USER']
        pwd = crawler.settings['MYSQL_PWD']
        db = crawler.settings['MYSQL_DB']
        return cls(host,port,user,pwd,db,charset)
    def process_item(self,item,spider):
        insert_sql = """
               insert into doubanmovie(title, playable, content, star, commentnum, inq)
               VALUE (%s, %s, %s, %s, %s, %s)
        """
        try:
            self.cursor.execute(insert_sql, (item['title'],  item['content'], item['score'], item['info']))
            self.client.commit()
        except Exception as err:
            print(err)
            self.client.rollback()
        return item

```

- 异步插入

```python
import pymysql
#twisted是一个异步的网络框架，这里可以帮助我们
实现异步将数据插入数据库
#adbapi里面的子线程会去执行数据库的阻塞操作，
当一个线程执行完毕之后，同时，原始线程能继续
进行正常的工作，服务其他请求。
from twisted.enterprise import adbapi
#异步插入数据库
class DoubanPipeline(object):
    def __init__(self,dbpool):
        self.dbpool = dbpool
    #使用这个函数来应用settings配置文件。
    @classmethod
    def from_crawler(cls, crawler):
        parmas = {
        'host':crawler.settings['MYSQL_HOST'],
        'user':crawler.settings['MYSQL_USER'],
        'passwd':crawler.settings['MYSQL_PASSWD'],
        'db':crawler.settings['MYSQL_DB'],
        'port':3306,
        'charset':'utf8',
        }
        # **表示字典，*tuple元组,
        # 使用ConnectionPool，起始最后返回的是一个ThreadPool
        dbpool = adbapi.ConnectionPool(
            'pymysql',
            **parmas
        )
        return cls(dbpool)
    def process_item(self, item, spider):
        #这里去调用任务分配的方法
        query = self.dbpool.runInteraction(
            self.insert_data_todb,
            item,
            spider
        )
        #数据插入失败的回调
        query.addErrback(
            self.handle_error,
            item
        )
        #执行数据插入的函数
        def insert_data_todb(self,cursor,item,spider):
            insert_str,parmas = item.insertdata()
            cursor.execute(insert_str,parmas)
            print('插入成功')
    def handle_error(self,failure,item):
        print(failure)
        print('插入错误')
        #在这里执行你想要的操作
    def close_spider(self, spider):
        self.pool.close()

```

### 三、数据去重

[数据去重]: https://blog.csdn.net/zp_00000/article/details/81042589

