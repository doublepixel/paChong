- **urlparse()实现URL的识别和分段**

  ```python
  	url = 'https://book.qidian.com/info/1004608738?wd=123&page=20#Catalog'
  """
  url：待解析的url
  scheme=''：假如解析的url没有协议,可以设置默认的协议,如果url有协议，设置此参数无效
  allow_fragments=True：是否忽略锚点,默认为True表示不忽略,为False表示忽略
  """
  result = parse.urlparse(url=url,scheme='http',allow_fragments=True)
  print(result)
  print(result.scheme)
  ```

  

- **urlunparse()可以实现URL的构造**

- ```python
  url_parmas = ('https', 'book.qidian.com', '/info/1004608738', '', 'wd=123&page=20', 'Catalog')
  #components:是一个可迭代对象，长度必须为6
  result = parse.urlunparse(url_parmas)
  print(result)
  """
  https://book.qidian.com/info/1004608738?wd=123&page=20#Catalog
  """
  ```

- **urljoin()传递一个基础链接,根据基础链接可以将某一个不完整的链接拼接为一个完整链接**

  ```python
  base_url = 'https://book.qidian.com/info/1004608738?wd=123&page=20#Catalog'
  sub_url = '/info/100861102'
  full_url = parse.urljoin(base_url,sub_url)
  print(full_url)
  
  ```

  

- **parse_qs()将url编码格式的参数反序列化为字典类型**

- ```python
  parmas_str = 'page=20&wd=123'
  parmas = parse.parse_qs(parmas_str)
  print(parmas)
  """
  {'page': ['20'], 'wd': ['123']}
  """
  ```

- **quote()可以将中文转换为URL编码格式**

- ```python
  word = '中国梦'
  url = 'http://www.baidu.com/s?wd='+parse.quote(word)
  print(parse.quote(word))
  print(url)
  """
  %E4%B8%AD%E5%9B%BD%E6%A2%A6
  http://www.baidu.com/s?wd=%E4%B8%AD%E5%9B%BD%E6%A2%A6
  """
  ```

- **unquote:可以将URL编码进行解码**

- ```python
  url = 'http://www.baidu.com/s?wd=%E4%B8%AD%E5%9B%BD%E6%A2%A6'
  print(parse.unquote(url))
  """
  http://www.baidu.com/s?wd=中国梦
  """
  ```

