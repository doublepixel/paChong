## pyecharts

### 一、安装

```python
pip install pyecharts
```

### 二、绘制柱形图

```python
  from pyecharts import options as opts
  from pyecharts.charts import Bar, Page
  from pyecharts.faker import Faker

  d = {'1000000': 0, '500000': 11, '100000': 20, '10000': 0, '5000': 757, '2000': 296, '500': 0}
  print(list(d.keys()))
  c = Bar().add_xaxis(list(d.keys())).add_yaxis("商家A", list(d.values())).set_global_opts(
    title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))

  Page().add(c).render()
   
```

