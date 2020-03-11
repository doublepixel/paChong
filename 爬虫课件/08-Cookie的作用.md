-  Cookies的作用

  - Cookies是最直接的应用就是检测用户是否已经登录

  ```python
  获取到一个有登录信息的Cookie模拟登陆
  # -*- coding:utf-8 -*-
  import urllib.request
  url = 'https://www.douban.com/people/175417123/'
  #根据刚才的登录信息来构建一个已经登录过的用户的headers信息
  headers = {
      'User-Agent':' Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:59.0) Gecko/20100101 Firefox/59.0',
      'Host':'www.renren.com',
      'Cookie':'anonymid=jgoj4xlw-3izsk4; depovince=BJ; jebecookies=62d94404-de1f-450a-919b-a2d9f4c8b811|||||; _r01_=1; JSESSIONID=abchsGLNgne0L8_wz2Emw; ick_login=cf54f2dc-8b0b-417a-96b2-32d4051f7236; jebe_key=02cb19ad-2966-4641-8828-217160ca67a0%7Cba6f6d6ec917200a4e17a85dbfe33a4a%7C1525230975024%7C1%7C1525230982574; t=87a502d75601f8e8c0c6e0f79c7c07c14; societyguester=87a502d75601f8e8c0c6e0f79c7c07c14; id=965706174; xnsid=e1264d85; ver=7.0; loginfrom=null; wp_fold=0',
  }
  # 2. 通过headers里的报头信息（主要是Cookie信息），构建Request对象
  request = urllib.request.Request(url, headers=headers)
  # 3. 直接豆瓣个人主页（主要是Cookie信息）
  #，判断这是一个已经登录的用户，并返回相应的页面
  response = urllib.request.urlopen(request)
  # 4. 打印响应内容
  print (response.read().decode())
  
  ```

- CookieJar

  - 用来储存Cookie值，存在内存中，向传出的HTTP请求添加cookie的对象。

  

  ```python
  import http.cookiejar as cookiejar
  from urllib import parse,request
  #1.构造一个CookieJar对象实例来保存cookie
  cookie = cookiejar.CookieJar()
  # 2.使用HTTPCookieProcessor()创建cookie处理器对象，
  # 参数为CookieJar()对象
  cookie_handler = request.HTTPCookieProcessor(cookie)
  #3.通过build_opener()来构建opener
  opener = request.build_opener(cookie_handler)
  #4.addheaders接受一个列表，里面每一个元素都是一个headers信息的元组
  #opener将会附带header信息
  opener.addheaders = [
      ('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:59.0) Gecko/20100101 Firefox/59.0'),
  ]
  #5.需要登录账号和密码
  data = {
      'source': 'index_nav',
      'form_email': '18518753265',
      'form_password': 'ljh123456',
  }
  #6. 通过urlencode()转码
  postdata = parse.urlencode(data).encode('utf-8')
  #7. 构建Request请求对象，包含需要发送的用户名和密码
  request = request.Request("https://www.douban.com/accounts/login", data = postdata)
  # 8. 通过opener发送这个请求，并获取登录后的Cookie值，
  opener.open(request)
  # 9. opener包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
  response = opener.open("https://www.douban.com/people/175417123/")
  #这里为了测试不添加cookie时访问改界面的效果
  #headers = {
  #    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:59.0) Gecko/20100101 #Firefox/59.0',
  #}
  # request = request.Request('https://www.douban.com/people/175417123/',headers=headers)
  # response = request.urlopen(request)
  # 10. 打印响应内容
  #打印结果查看是否访问成功
  print(response.code)
  html = response.read().decode('utf-8')
  # print(html)
  with open('douban_login.html','w') as f:
      f.write(html)
  
  ```

  

