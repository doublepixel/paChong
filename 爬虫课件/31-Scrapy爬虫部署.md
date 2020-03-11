## 部署

- scrapyd

  是运行scrapy爬虫的服务程序,它支持以http命令方式发布、删除、启动、停止爬虫程序。而且scrapyd可以同时管理多个爬虫,每个爬虫还可以有多个版本

  ```
  pip install scrapyd
  ```

  

- scrapyd-client

  发布爬虫需要使用另一个专用工具，就是将代码打包为EGG文件，其次需要将EGG文件上传到远程主机上这些操作需要scrapyd-client来帮助我们完成

  ```
  pip install scrapyd-client
  ```


- 运行服务

  ```
  scrapyd
  ```

- 修改配置文件

- ```
  [deploy]
  url=http://localhost:6800
  project=项目名称
  ```

- 执行部署

- ```
  scrapyd-deploy -p <项目名称> --version <版本号>
  ```

- 运行爬虫

- ```
  curl http://localhost:6800/schedule.json -d project=project -d spider=somespider
  ```

- 关闭爬虫

- ```
  curl http://localhost:6800/cancel.json -d project=project -d job='jobid'
  ```

- 获取爬虫列表

- ```
  curl http://localhost:6800/listprojects.json
  ```

- 获取爬虫文件

- ```
  curl http://localhost:6800/listspiders.json?project=project
  ```

- 获取运行状态

- ```
  curl http://localhost:6800/listjobs.json?project=project
  ```

- 删除爬虫

- ```
  curl http://localhost:6800/delproject.json -d project=project
  curl http://localhost:6800/delversion.json -d project=project -d version=r99
  ```

  

https://www.cnblogs.com/xueranzp/p/5368637.html