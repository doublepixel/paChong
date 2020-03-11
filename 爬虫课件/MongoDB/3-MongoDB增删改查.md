### 一、Mongo支持的数据类型

| 类型        | 解释                                 |
| ----------- | ------------------------------------ |
| String      | 字符串                               |
| Integer     | 整型数值                             |
| Boolean     | 布尔值                               |
| Double      | 双精度浮点值                         |
| Array       | 用于将数组或列表或多个值存储为一个键 |
| Timestamp   | 时间戳                               |
| Object      | 用于嵌入式的文档，即一个值为一个文档 |
| Null        | 用于创建空值                         |
| Date        | 日期时间                             |
| Object ID   | 对象 ID                              |
| Binary Data | 二进制数据                           |

### 二、主键

ObjectId 类似唯一主键

1. 每个文档都有一个属性，为_id，保证每个文档的唯一性
2. 可以自己去设置_id插入文档
3. 如果没有提供，那么MongoDB为每个文档提供了一个独特的_id，类型为objectID
4. objectID是一个12字节的十六进制数 前4个字节为当前时间戳 接下来3个字节的机器ID 接下来的2个字节中MongoDB的服务进程id 最后3个字节是简单的增量值

### 三、插入文档

> db.集合名称.insert(document)

1. db.stu.insert({name:'郑程峰',gender:1})
2. db.stu.insert({_id:'20180819',name:'郑程峰2',gender:1})
3. db.stu.insert([{name:'王明',gender:1},{name:'王玲玲',gender:0}])

### 四、查询文档

> db.集合名称.find({条件文档})

1. db.stu.find({name:'李某某'})

### 五、比较运算符

1. 小于$lt
2. 小于或等于$lte
3. 大于$gt
4. 大于或等于$gte
5. 不等于$ne

1. db.stu.find({age:{$gte:18}})

### 六、逻辑运算符

1. db.stu.find({age:{$gte:18},gender:1})
2. db.stu.find({$or:[{age:{$gt:18}},{gender:1}]})
3. db.stu.find({age:{$in:[18,28]}})
4. db.stu.find({"title" : {$type : 'string'}})

### 七、Limit与Skip方法

1. db.stu.find().skip(5).limit(4)

### 八、排序

- 升序
  1. db.集合名称.find().sort({要排序的字段:1})
- 降序
  1. db.集合名称.find().sort({要排序的字段:-1})

> skip(), limilt(), sort()三个放在一起执行的时候，执行的顺序是先 sort(), 然后是 skip()，最后是显示的 limit()

### 九、去重

1. db.集合名称.distinct('name',{age:{$gt:20}})

### 十、计数

1. db.集合名称.count({age:{$gt:20},gender:1})

### 十一、更新

- 全部更新
  1.  db.stu.update({"name":"xiaowang"},{$set:{"name":"xiao"}},{"multi":true})
- 指定更新
  1. db.stu.update({name:'李自成'},{$set:{name:'闯王李自成'}})

### 十二、删除

- 删除一个
  1. db.集合名称.remove(document,{justOne:true})
- 删除全部
  1. db.集合名称.remove({})

