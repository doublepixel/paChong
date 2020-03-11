# 使用Scrapyd远程控制爬虫

Scrapyd是Scrapy提供的可以远程部署和监控爬虫的工具，其官方文档为：[http://scrapyd.readthedocs.org/en/latest](https://scrapyd.readthedocs.org/en/latest/)

### 第一步：安装Scrapyd服务端和客户端工具

```sh
# 安装Scrapyd服务器端
Power@PowerMac ~$  sudo pip install Scrapyd

# 安装Scrapyd客户端工具
Power@PowerMac ~$  sudo pip install Scrapyd-client

# 启用Scrapyd服务端
Power@PowerMac ~$  Scrapyd
```

### 第二步：修改scrapyd的配置文件

```python
# 打开scrapyd配置文件（例） 
# 如果是在虚拟环境中安装则在对应的虚拟环境中的lib/python2.x|3.x/site-packages/scrapyd/default_scrapyd.conf
sudo vi /usr/local/lib/python2.7/site-packages/scrapyd/default_scrapyd.conf
```

安装好scrapyd后，将配置文件中的 `bind_address` 的值修改为 `0.0.0.0`，表示允许任何客户端访问scrapyd服务端（默认127.0.0.1，表示只允许本机访问），之后再终端下启动scrapyd服务。

```python
# 启用Scrapyd服务
Power@PowerMac ~$  scrapyd
```

> 启动成功后，可以在浏览器打开 [http://192.168.xxx.xxx:6800/](http://192.168.xxx.xxx:6800/) (启动服务的主机ip，端口6800）查看Scrapyd的监控信息。

### 第三步：配置Scrapy项目下的Scrapyd配置

##### 1. 打开Scrapy项目下的scrapy.cfg文件，例如：

```python
[settings]
default = mySpider.settings

[deploy]
#url = http://localhost:6800/
project = Tencent
```

##### 2. 启用Scrapyd 配置，在deploy后面指定当前项目的Scrapyd配置名，配置Scrapyd服务的ip和port，以及当前项目的项目名，例如：

```python
# myScrapyd是配置名
[deploy:myScrapyd]        

# url值为开启Scrapyd服务的主机ip，默认端口号为6800
# url = http://123.45.67.89:6800
# 如果是本机Scrapyd服务，则使用localhost即可
url = http://localhost:6800/    

# 需要部署和监控的Scrapy项目名
project = mySpider
```

### 第四步：通过Scrapyd客户端工具挂载项目

```python
# 挂载项目： Scrapyd-deploy 是客户端命令，参数是 Scrapyd配置名，以及 -p 指定项目名 如果修改了项目代码则需要重新挂载
Power@PowerMac ~$ Scrapyd-deploy myScrapyd -p mySpider
```

> 挂载成功后，可以在浏览器打开 **http://localhost:6800** (或是配置时指定的其他ip）查看Scrapyd的监控信息。

### 第五步：远程启动和停止爬虫

```python
# 远程启动爬虫：
# project=项目名，spider=需要启动的爬虫名
~$  curl http://localhost:6800/schedule.json -d project=mySpider -d spider=demo

# 注意：爬虫启动成功后，会生成job值，停止爬虫时需要通过job值停止。

# 远程停止爬虫：
# project=项目名，job=启动爬虫生成的job值
~$  curl http://localhost:6800/cancel.json -d project=mySpider -d job=fcb0cbx....
```

### 第六步 设置scrapyd后台运行

如果是在服务器进行搭载，那么必须要设置后台运行

1. 新建目录/var/scrapyd

   `sudo mkdir /var/scrapyd`

2. 新建文件/etc/init.d/scrapyd，名称为scrapyd

   `sudo vi /etc/init.d/scrapyd`

3. 输入内容

   ```shell
   #!/bin/bash
   PORT=6800
   HOME="/var/scrapyd"
   # 你对应的scrapyd启动文件目录，如果是在虚拟环境下安装的scrapyd那么就是对应环境的bin目录下
   BIN="/usr/local/bin/scrapyd"
    
   pid=`netstat -lnopt | grep :$PORT | awk '/python/{gsub(/\/python/,"",$7);print $7;}'`
   start() {
      if [ -n "$pid" ]; then
         echo "server already start,pid:$pid"
         return 0
      fi
    
      cd $HOME
      nohup $BIN >> $HOME/scrapyd.log 2>&1 &
      echo "start at port:$PORT"
   }
    
   stop() {
      if [ -z "$pid" ]; then
         echo "not find program on port:$PORT"
         return 0
      fi
    
      #结束程序，使用讯号2，如果不行可以尝试讯号9强制结束
      kill -9 $pid
      echo "kill program use signal 9,pid:$pid"
   }
    
   status() {
      if [ -z "$pid" ]; then
         echo "not find program on port:$PORT"
      else
         echo "program is running,pid:$pid"
      fi
   }
    
   case $1 in
      start)
         start
      ;;
      stop)
         stop
      ;;
      status)
         status
      ;;
      *)
         echo "Usage: {start|stop|status}"
      ;;
   esac
    
   exit 0
   ```

4. 可使用命令进行操作了（启动停止状态）

   `service scrapyd {start|stop|status}`

5. 设置为系统启动项

   - 启用禁用命令：`sysv-rc-conf scrapyd on/off`

6. 如果出现找不到`scrapyd.service`的报错信息，则可以使用下面命令

   ```shell
   # 第一个为你的scrapyd启动命令的目录，我这里实在虚拟环境下安装的所以在虚拟环境下的目录，如果是直接安装的则在/usr/local/bin/scrapyd 或者系统python对应的目录。~/scrapyd.log输出日志位置
   /home/ubuntu/py3/bin/scrapyd >> ~/scrapyd.log 2>&1 &
   ```