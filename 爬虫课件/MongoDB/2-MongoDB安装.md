### 一、下载    

https://www.mongodb.com/download-center/community

### 二、创建文件夹

- 创建data文件夹在，data文件夹下创建 db文件夹
- 创建log文件夹，在log文件夹下mongo.log文件

### 三、配置mongo.config

- dbpath=D:\mongodb\mongodb-win32-x86_64-2012plus-4.2.1\data\db

-  logpath=D:\mongodb\mongodb-win32-x86_64-2012plus-4.2.1\log\mongo.log

### 四、创建服务

- mongod --config "D:\mongodb\mongodb-win32-x86_64-2012plus-4.2.1\mongo.config"
  --install --serviceName "MongoDB"

### 五、启动服务

- net start MongoDB

### 六、链接mongo

-  mongo 127.0.0.1:27017

### 七、关闭服务

- net stop MongoDB

### 八、卸载服务     

-  mongod --remove