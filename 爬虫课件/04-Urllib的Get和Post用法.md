- Decode
  - Decode的作用是将其他编码的字符串转换成unicode编码，如str.decode('gb2312')，表示将gb2312编码的字符串str1转换成unicode编码。
- Encode
  - Encode的作用是将unicode编码转换成其他编码的字符串，如str.encode('gb2312')，表示将unicode编码的字符串str2转换成gb2312编码。

-  Get请求
  - URL编码

  ```python
  word = {"wd" : "美女"}
  # 通过urllib.urlencode()方法，将字典键值对按URL编码转换，从而能被web服务器接受。
  result = urllib.parse.urlencode(word) 
  print(result)
  ```

  - 解码

  ```python
  result = urllib.parse.unquote(result)
  print(result)
  ```

  
  - 发送请求

  ```python
   response = urllib.request.urlopen(request)
   print(response.read())
  
  ```

  

- POST请求

  - ```python
    # POST请求的目标URL（这个代码是之前的链接，方便我们使用，不用传递sign参数，新版中该参数是加密的）
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
    #构建表单数据
    formdata = {
        'i': '你好',
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION',
        'typoResult': 'false',
    }
    
    formdata = urllib.parse.urlencode(formdata)
    formdata = formdata.encode('utf-8')
    
    req = request.Request(url, data = formdata, headers = headers)
    #发起请求获取响应结果
    response = request.urlopen(req)
    #打印获取的响应结果
    print (response.read().decode('utf-8'))
    ```

    

- 忽略SSL验证

  ![12306zhengshu](https://i.loli.net/2018/09/05/5b8f8965559aa.png)

  ```python
  from urllib import request
  # 1. 导入Python SSL处理模块
  import ssl
  # 2. 表示忽略未经核实的SSL证书认证
  context = ssl._create_unverified_context()
  # 目标url
  url = "https://www.12306.cn/mormhweb/"
  #设置请求头
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
  #构建request对象
  request = urllib.request.Request(url, headers = headers)
  # 3. 在urlopen()方法里 指明添加 context 参数
  response = urllib.request.urlopen(request, context = context)
  html = response.read().decode()
  print (html)
  
  ```

  

