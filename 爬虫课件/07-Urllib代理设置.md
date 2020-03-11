- 自定义Opener

我们之前一直都在使用的urlopen，它是一个特殊的opener，是模块帮我们创建好的。自定义Opener会有更高级的用法

```python
import urllib.request
# 构建一个HTTPHandler 处理器对象，支持处理HTTP请求
http_handler = urllib.request.HTTPHandler()
# 构建一个HTTPHandler 处理器对象，支持处理HTTPS请求
# http_handler = urllib.request.HTTPSHandler()
# 调用urllib.request.build_opener()方法，创建支持处理HTTP请求的opener对象
opener = urllib.request.build_opener(http_handler)
# 构建 Request请求
request = urllib.request.Request("http://www.baidu.com/")
# 调用自定义opener对象的open()方法，发送request请求
response = opener.open(request)
# 获取服务器响应内容
print (response.read().decode())

```

- 代理设置

  - ![web_proxy](https://i.loli.net/2018/11/19/5bf2c0c6a0646.png)

  - **代理的作用：**

    - 1.**突破自身IP访问限制**，访问一些平时不能访问的站点。

    - 2.**访问一些单位或团体内部资源**：比如使用教育网内地址段免费代理服务器，就可以用于对教育网开放的各类FTP下载上传，以及各类资料查询共享等服务。

    - 3.**提高访问速度**：通常代理服务器都设置一个较大的硬盘缓冲区，当有外界的信息通过时，同时也将其保存到缓冲区中，当其他用户再访问相同的信息时，则直接由缓冲区中取出信息，传给用户，以提高访问速度。

    - 4.**隐藏真实IP**：上网者也可以通过这种方法隐藏自己的IP，免受攻击。对于爬虫来说，我们用代理就是为了隐藏自身IP，防止自身的IP被封锁。

  - **根据协议划分**

    - FTP代理服务器**：主要用于访问FTP服务器，一般有上传、下载的功能以及缓存的功能，端口号一般为21，2121等。**

    - HTTP代理服务器**：主要用于访问网页，一般有内容过滤和缓存的功能，端口号一般为80、8080、3128等**

    - **SSL/TLS代理**：主要能用于访问加密的网站，一般有SSL或者TLS加密**

    - **SOCKS代理**：只是单纯的用于传输数据包，不关心具体的协议用法，速度快、有缓存功能，端口号一般为1080

      

  -  **根据匿名内容划分**

    -  **高度匿名代理**：会将数据包原封不动的转发，在服务器看来就好像真的是一个普通的用户短在访问，而记录的IP就是代理服务器的IP

    - **普通匿名代理**：会在数据包上做一些改动，服务端上有可能发现这个是代理服务器，也有一定的几率追查到客户端的真实IP.

    - **透明代理**：不但改动了数据包，还会告诉服务器客户端的真实IP，这种代理除了用缓存技术提高浏览器速度。能用内容过滤提高安全性之外，并没有其他作用。

    - **使用代理IP**这是爬虫/反爬虫的第二大招，通常也是最好用的。

-  **代理网站**
  - 西刺免费代理IP
  - 快代理免费代理

```python
from urllib import request,error
#构建支持代理的handler
proxy = {
    'http':'61.138.33.20:808',
    'https':'120.69.82.110:44693',
}
proxy_handler = request.ProxyHandler(
    proxies=proxy
)
# 构建一个私密代理Handler，需要加上私密代理账户的用户名和密码
# authproxy = {
#    "http" :"username:password@61.135.217.7:80"
#}
# authproxy_handler=urllib.request.ProxyHandler(
#    proxies=authproxy
#)
#根据proxy_handler实例化一个opener对象
opener = request.build_opener(proxy_handler)
url = 'http://www.baidu.com/'
# 使用https://httpbin.org/get接口验证使用了代理
# url = 'https://httpbin.org/get'
try:
    response = opener.open(url,timeout=5)
    print(response.status)
except error.HTTPError as err:
    print(err.reason)
except error.URLError as err:
    print(err.reason)
# 1. 如果按照上面代码，只有使用opener.open()方法发送
请求才使用自定义的代理，而urlopen()则不使用自定义代理。
response = opener.open(request)
# 2. 将自定义的opener设置为全局的opener，之后所有的，不管是
opener.open()还是urlopen() 发送请求，都将使用自定义代理。
# request.install_opener(opener)
# response = urlopen(request)

```

