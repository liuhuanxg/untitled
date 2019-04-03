import numpy as np
#自定义类型
#属性名，类型，长度
new_type=np.dtype([('name',np.str_,40),('num',np.int64,),('price',np.float64)])
print(new_type)
print(new_type['name'])


goodsinfo=np.array([('大白菜',100,0.56),('土豆',200,1.0),('萝卜',200,0.3)],dtype=new_type)
print(goodsinfo)
