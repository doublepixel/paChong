- jsonpath

  用来解析多层嵌套的json数据;JsonPath 是一种信息抽取类库，是从JSON文档中抽取指定信息的工具，提供多种语言实现版本，包括：Javascript, Python， PHP 和 Java

  

- 文档与安装

  - http://goessner.net/articles/JsonPath
  - pip install jsonpath

- 语法

  ![image-20191030223346526](/Users/xiaoyuan/Library/Application Support/typora-user-images/image-20191030223346526.png)

  ![image-20191030223401359](/Users/xiaoyuan/Library/Application Support/typora-user-images/image-20191030223401359.png)

  ![image-20191030223411384](/Users/xiaoyuan/Library/Application Support/typora-user-images/image-20191030223411384.png)

- 用法

  ```python
  import requests
  import jsonpath
  import json
  import chardet
  url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'
  response = requests.get(url)
  html = response.text
  # 把json格式字符串转换成python对象
  jsonobj = json.loads(html)
  # 从根节点开始，匹配name节点
  citylist = jsonpath.jsonpath(jsonobj,'$..name')
  ```

  