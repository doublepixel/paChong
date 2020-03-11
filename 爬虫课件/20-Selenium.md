### 一、Selenium

Selenium是一款自动化测试工具，支持Chrome，Safari，Firefox 等主流界面式浏览器；支持多种语言开发，比如Java，C，Python等

### 二、文档地址

-  https://selenium-python-zh.readthedocs.io/en/latest/

### 三、安装

```python
pip install selenium
```

### 四、驱动下载

```
http://npm.taobao.org/mirrors/chromedriver
```

### 五、使用

```python
#导入 webdriver
from selenium import webdriver
    
# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys
import time
#无界面浏览器相关设置
# 创建chrome参数对象
opt = webdriver.ChromeOptions()
#把chrome设置成为无界面模式
opt.set_headless()
#创建chrome无界面对象
driver = webdriver.Chrome(
    options=opt, executable_path='/Users/ljh/Desktop/chromedriver'
)
#创建chrome有界面对象
#调用Chrome浏览器创建浏览器对像(指定一下位置)
driver = webdriver.Chrome(
    executable_path='/Users/ljh/Desktop/chromedriver'
)
#打开浏览器，模拟浏览器请求页面
driver.get('http://www.baidu.com/')
#获取页面的信息
html = driver.page_source
print(html)
# 获取页面名为 wrapper的id标签的文本内容
data = driver.find_element_by_id("wrapper").text
#获取标签的属性
attrvaule = driver.find_element_by_id("wrapper").get_attribute('class')
#打印数据内容
print(data)
#打印标题数据
print(driver.title)
#向百度的搜索框输入搜索关键字
driver.find_element_by_id('kw').send_keys('美女')
#百度搜索按钮，click() 是模拟点击
driver.find_element_by_id('su').click()
#获取当前页面的cookies()
cookies = driver.get_cookies()
cookie = ''
for item in cookies:
    cookie += item['name']+item['value']+' ;'
    print(cookie[:-1])
#全选输入框中的内容ctrl+a 
print(driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a'))
# ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
#清空输入框内容
driver.find_element_by_id('kw').clear()
#输入框重新输入内容
driver.find_element_by_id('kw').send_keys('风景')
#模拟回车键
driver.find_element_by_id('su').send_keys(Keys.RETURN)
#获取当前的url
currentUrl = driver.current_url
print(currentUrl)
#截取网页页面（生成当前的页面快照并保存）
driver.save_screenshot('baidu.png')
#睡眠7秒
time.sleep(7)
# 关闭浏览器
driver.quit()
# 关闭当前页面，如果只有一个页面，会关闭浏览器
driver.close()


```



### 六、设置代理

```python
opt = webdriver.ChromeOptions()
opt.add_argument("--proxy-server=http://118.20.16.82:9999")
```

### 七、添加Cookie

```
self.browser.add_cookie({
        'domain': '.xxxx.com',  
        'name': cookie['name'],
        'value': cookie['value'],
        'path': '/',#哪个页面添加Cookie
        'expires': None
    })
```



### 八、显示等待

显式等待是你在代码中定义等待一定条件发生后再进一步执行你的代码。 最糟糕的案例是使用time.sleep()，它将条件设置为等待一个确切的时间段。 这里有一些方便的方法让你只等待需要的时间。WebDriverWait结合ExpectedCondition 是实现的一种方式。

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://somedomain/url_that_delays_loading")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()
```

### 九、隐式等待

如果某些元素不是立即可用的，隐式等待是告诉WebDriver去等待一定的时间后去查找元素。 默认等待时间是0秒，一旦设置该值，隐式等待是设置该WebDriver的实例的生命周期。

```
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10) # seconds
driver.get("http://somedomain/url_that_delays_loading")
myDynamicElement = driver.find_element_by_id("myDynamicElement")
```



### 十、执行JS

```python
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
```



### 十一、设置无页面

```python
options = webdriver.ChromeOptions()
# 添加无界面参数
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
```



### 十二、切换页面

```
# 获取当前所有句柄（窗口）
all_handles = browser.window_handles
# 切换browser到新的窗口，获取新窗口的对象
browser.switch_to.window(all_handles[1])

```

