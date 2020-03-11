### 一、管道文件

> item写入JSON文件以下pipeline将所有(从所有'spider'中)爬取到的item，存储到一个独立地items.json 文件，每行包含一个序列化为'JSON'格式的'item':

```python
import json
class JobboleprojectPipeline(object):
    
    def __init__(self):
        self.file = open(‘jobbole.json', 'w')
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(content)
        return item
    def close_spider(self, spider):
        self.file.close()

```

### 二、注册管道文件

```python
# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    #'mySpider.pipelines.SomePipeline': 300,
    "mySpider.pipelines.JobboleprojectPipeline":300
}

```

> 分配给每个类的整型值，确定了他们运行的顺序，item按数字从低到高的顺序，通过pipeline，通常将这些数字定义在0-1000范围内（0-1000随意设置，数值越低，组件的优先级越高）

### 三、图片管道

```python
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from scrapy.exceptions import DropItem
import os
from scrapy.utils.project import get_project_settings
#下载图片
image_store = get_project_settings().get('IMAGES_STORE')
class jobboleImagePipline(ImagesPipeline):
    def get_media_requests(self, item, info):
        #根据图片地址，构建请求
        yield scrapy.Request(item['coverImage'])
    def item_completed(self, results, item, info):
        print(results)
        #获取图片下载成功的请求路径
        image_paths = [x['path'] for ok, x in results if ok]
        #判断图片是否下载成功
        if not image_paths:
            #出现错误，例如没有图片，可以丢弃item
            raise DropItem("Item contains no images")
        else:
            #替换图片的名称，自定义图片名称
            os.rename(image_store+'/'+image_paths[0],
                    image_store+'/'+item['title']+'.jpg')
            #将图片地址赋值给item
            item['localImagePath'] = image_store+'/'+item['title']+'.jpg'
            return item

```

