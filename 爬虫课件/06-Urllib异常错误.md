-  **URLError**
  - 来自urllib库的error模块，继承自OSError,由request模块产生的异常都可以通过捕捉这个类来处理．
    - 没有网络连接
    - 服务器连接失败
    - 找不到指定的服务器

- HTTPError

  - HTTPError是URLError的子类，我们发出一个请求时，服务器上都会对应一个response应答对象，其中它包含一个数字"响应状态码"。

  - 专门用来处理ＨTTP请求错误，比如未认证，页面不存在等

  - 有三个属性：

    - code:返回HTTP的状态码

    - reason:返回错误原因
    - headers:返回请求头

    

    ```python
    from urllib import request,error
    def check_error():
        """
        因为HTTPError的父类是URLError，所以我们更好的处理顺序应该是
        先捕获子类的错误，再捕获父类的错误
        """
        req_url = 'https://www.baiduxxx.com/'
        try:
            response = request.urlopen(url=req_url)
            print(response.status)
        except error.HTTPError as err:
            print(err.code,err.reason,err.headers)
        except error.URLError as err:
            print('===', err.reason)
    
    ```

    

    

    

    

    

    