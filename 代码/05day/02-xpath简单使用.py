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

li_list = html.xpath('//li[@class="item-0"]')  # 选取class为item-0的li标签
text_list = html.xpath('//li[@class="item-0"]/a/text()')  # 选取class为item-0的li标签 下面a标签的值
li1_list = html.xpath('//li[@id="1"]')  # 选取id属性为1的li标签
li2_list = html.xpath('//li[@data="2"]')  # 选取data属性为2的li标签
href_list = html.xpath('//li[@class="item-0"]/a/@href')  # 取属性
print(li_list)
print(text_list)
print(li1_list)
print(li2_list)
print(href_list)

'//div[@class="col-sm-9 center-wrap"]//a'
'//div[@class="col-sm-9 center-wrap"]//a/div[@class="random_title"]/text()'
'//div[@class="col-sm-9 center-wrap"]//a//div[@class="random_article"]//img/@src'
