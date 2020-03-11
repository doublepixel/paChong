- requests

  - requests是python实现的简单易用的HTTP库，使用起来比urllib简洁很多。

- Get请求

  ```python
  response = requests.get("http://www.baidu.com/")
  * response的常用方法：
      * response.text  返回解码后的字符串
      * respones.content  以字节形式（二进制）返回。
      * response.status_code　 响应状态码
      * response.request.headers　 请求的请求头
      * response.headers　 响应头
      * response.encoding = 'utf-8'   可以设置编码类型
      * response.encoding       获取当前的编码
      * response.json()   内置的JSON解码器，以json形式返回,前提返回的内容确保是json格式的，不然解析出错会抛异常
  
  ```

  

-  添加请求头

  ```python
  import requests
  kw = {'wd':'美女'}
  headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
  }
  # params 接收一个字典或者字符串的查询参数，
  # 字典类型自动转换为url编码，不需要urlencode()
  response = requests.get(
      "http://www.baidu.com/s?",
      params = kw, 
      headers = headers
  )
  ```

- **注意**
  - 使用response.text 时，Requests 会基于 HTTP 响应的文本编码自动解码响应内容，大多数 Unicode 字符集都能被无缝地解码，但是也会出现乱码请求。推荐使用response.content.deocde()
  - 使用response.content 时，返回的是服务器响应数据的原始二进制字节流，可以用来保存图片等二进制文件。

- Post请求

  ```python
  import requests
  req_url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
  #分析表单数据
  formdata = {
      'i': '老鼠爱大米',
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
  #添加请求头
  req_header = {
      'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
  }
  response = requests.post(
      req_url, 
      data = formdata, 
      headers = req_header
  )
  #print (response.text)
  # 如果是json文件可以直接显示
  print (response.json())
  
  ```

  

