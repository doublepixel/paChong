- 上传文件

  ```python
  url = 'https://httpbin.org/post'
  files = {'file': open('image.png', 'rb')}
  response = requests.post(url, files=files)
  print(response.text)
  ```

  

-  Web客户端验证

  ```python
  import requests
  auth=('test', '123456')
  response = requests.get(
      'http://192.168.199.107', 
      auth = auth
  )
  print (response.text)
  ```

  

- 代理设置

  ```python
  import requests
  # 根据协议类型，选择不同的代理
  proxies = {
      "http": "http://11.44.156.126:4532",
      "https": "http://11.134.156.126:4532",
  }
  ##如果代理需要使用HTTP Basic Auth，可以使用下面这种格式：
  '''
  proxy = { 
      "http": "name:password@11.134.156.126:4532" 
  }
  '''
  
  response = requests.get(
      "http://www.baidu.com", 
      proxies = proxies
  )
  print(response.text)
  ```

  

-  Cookies

  ```python
  import requests
  response = requests.get("https://www.douban.com/")
  # 7\. 返回CookieJar对象:
  cookiejar = response.cookies
  # 8\. 将CookieJar转为字典：
  cookiedict = requests.utils.dict_from_cookiejar(
      cookiejar
  )
  print (cookiejar)
  print (cookiedict)
  ```

  

-  Session

  ```python
  import requests
  # 1\. 创建session对象，可以保存Cookie值
  ssion = requests.session()
  # 2\. 处理 headers
  headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
  }
  # 3\. 需要登录的用户名和密码
  data = {
      "email":"18518753265",
      "password":"ljh123456"
  }
  # 4\. 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在ssion里
  ssion.post(
      "http://www.renren.com/PLogin.do",
      data = data
  )
  # 5\. ssion包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
  response = ssion.get(
      "http://www.renren.com/965722397/profile"
  )
  # 6\. 打印响应内容
  print (response.text)
  ```

  

- 跳过SSL验证

  ```python
  import requests
  response = requests.get("https://www.12306.cn/mormhweb/", verify = False)
  print (response.text)
  ```

  