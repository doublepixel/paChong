- 什么是xpath?
  XPath (XML Path Language) 是一门在 XML 文档中查找信息的语言，可用来在 XML 文档中对元素和属性进行遍历。
- 什么是xml?[W3School](http://www.w3school.com.cn/xml/xml_intro.asp)
  - XML 指可扩展标记语言（EXtensible Markup Language）
  - XML 是一种标记语言，很类似 HTML
  - XML 的设计宗旨是传输数据，而非显示数据
  - XML 标签没有被预定义。您需要自行定义标签。
  - XML 被设计为具有自我描述性。
  - XML 是 W3C 的推荐标准
- XML和 HTML 的区别

| 数据格式 | 描述           | 作用               |
| -------- | -------------- | ------------------ |
| XML      | 可扩展标记语言 | 用来传输和存储数据 |
| HTML     | 超文本标记语言 | 用来显示数据       |

- 常见语法

| 表达式 | 含义               |
| ------ | ------------------ |
| /      | 从根节点开始       |
| //     | 从任意节点         |
| .      | 从当前节点         |
| ..     | 从当前节点的父节点 |
| @      | 选取属性           |
| text() | 选取文本           |

- 常用用法

```python
from lxml import etree
data = """
        <div>
            <ul>
                 <li class="item-0"><a href="link1.html">first item</a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1" id="1" ><a href="link4.html">fourth item</a></li>
                 <li class="item-0" data="2"><a href="link5.html">fifth item</a>
             </ul>
         </div>
        """

html = etree.HTML(data)#构造了一个XPath解析对象。etree.HTML模块可以自动修正HTML文本。

li_list = html.xpath('//ul/li')#选取ul下面的所有li节点
#li_list = html.xpath('//div/ul/li')#选取ul下面的所有li节点

a_list = html.xpath('//ul/li/a')#选取ul下面的所有a节点
herf_list = html.xpath('//ul/li/a/@href')#选取ul下面的所有a节点的属性herf的值
text_list = html.xpath('//ul/li/a/text()')#选取ul下面的所有a节点的值
print(li_list)
print(a_list)
print(herf_list)
print(text_list)

#打印
[<Element li at 0x1015f4c48>, <Element li at 0x1015f4c08>, <Element li at 0x1015f4d08>, <Element li at 0x1015f4d48>, <Element li at 0x1015f4d88>]
[<Element a at 0x1015f4dc8>, <Element a at 0x1015f4e08>, <Element a at 0x1015f4e48>, <Element a at 0x1015f4e88>, <Element a at 0x1015f4ec8>]
['link1.html', 'link2.html', 'link3.html', 'link4.html', 'link5.html']
['first item', 'second item', 'third item', 'fourth item', 'fifth item']
```

- 通配符

| 通配符 | 含义               |
| ------ | ------------------ |
| *      | 选取任何元素节点   |
| @*     | 选取任何属性的节点 |

- 常见用法

```python
from lxml import etree
data = """
        <div>
            <ul>
                 <li class="item-0"><a href="link1.html">first item</a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1" id="1" ><a href="link4.html">fourth item</a></li>
                 <li class="item-0" data="2"><a href="link5.html">fifth item</a>
             </ul>
         </div>
        """

html = etree.HTML(data)

li_list = html.xpath('//li[@class="item-0"]')#选取class为item-0的li标签
text_list = html.xpath('//li[@class="item-0"]/a/text()')#选取class为item-0的li标签 下面a标签的值
li1_list  = html.xpath('//li[@id="1"]')#选取id属性为1的li标签
li2_list  = html.xpath('//li[@data="2"]')#选取data属性为2的li标签
print(li_list)
print(text_list)
print(li1_list)
print(li2_list)

#打印
[<Element li at 0x101dd4cc8>, <Element li at 0x101dd4c88>]
['first item', 'fifth item']
[<Element li at 0x101dd4d88>]
[<Element li at 0x101dd4c88>]

```

- 表达式

| 表达式       | 含义               |
| ------------ | ------------------ |
| [?]          | 选取第几个节点     |
| last()       | 选取最后一个节点   |
| last()-1     | 选取倒数第二个节点 |
| position()-1 | 选取前两个         |

- 常见用法

```python
from lxml import etree

data = jiayuan

html = etree.HTML(data)

li_list = html.xpath('//ul/li[1]')  # 选取ul下面的第一个li节点
li1_list = html.xpath('//ul/li[last()]')  # 选取ul下面的最后一个li节点
li2_list = html.xpath('//ul/li[last()-1]')  # 选取ul下面的最后一个li节点
li3_list = html.xpath('//ul/li[position()<= 3]')  # 选取ul下面前3个标签
text_list = html.xpath('//ul/li[position()<= 3]/a/@href')  # 选取ul下面前3个标签的里面的a标签里面的href的值
print(li_list)
print(li1_list)
print(li2_list)
print(li3_list)
print(text_list)

#打印
[<Element li at 0x1015d3cc8>]
[<Element li at 0x1015d3c88>]
[<Element li at 0x1015d3d88>]
[<Element li at 0x1015d3cc8>, <Element li at 0x1015d3dc8>, <Element li at 0x1015d3e08>]
['link1.html', 'link2.html', 'link3.html']

```

- 函数

| 函数名      | 含义                   |
| ----------- | ---------------------- |
| starts-with | 选取以什么开头的元素   |
| contains    | 选取包含一些信息的元素 |
| and         | 并且的关系             |
| or          | 或者的关系             |

```python
from lxml import etree

data = """
        <div>
            <ul>
                 <li class="item-0"><a href="link1.html">first item</a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1" id="1" ><a href="link4.html">fourth item</a></li>
                 <li class="item-0" data="2"><a href="link5.html">fifth item</a>
             </ul>
         </div>
        """

html = etree.HTML(data)

li_list = html.xpath('//li[starts-with(@class,"item-1")]')#获取class包含以item-1开头的li标签
li1_list = html.xpath('//li[contains(@class,"item-1")]')#获取class包含item的li标签
li2_list = html.xpath('//li[contains(@class,"item-0") and contains(@data,"2")]')#获取class为item-0并且data为2的li标签
li3_list = html.xpath('//li[contains(@class,"item-1") or contains(@data,"2")]')#获取class为item-1或者data为2的li标签
print(li_list)
print(li1_list)
print(li2_list)
print(li3_list)

#打印
[<Element li at 0x101dcac08>, <Element li at 0x101dcabc8>]
[<Element li at 0x101dcac08>, <Element li at 0x101dcabc8>]
[<Element li at 0x101dcacc8>]
[<Element li at 0x101dcac08>, <Element li at 0x101dcabc8>, <Element li at 0x101dcacc8>]
```

- 插件
  - Chrome插件 XPath Helper
  - Firefox插件 XPath Checker