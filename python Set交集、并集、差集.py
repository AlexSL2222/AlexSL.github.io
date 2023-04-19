s = set([3,5,9,10,20,40])      #创建一个数值集合 
t = set([3,5,9,1,7,29,81])      #创建一个数值集合 

a = t | s          # t 和 s的并集 ,等价于t.union(s)
b = t & s          # t 和 s的交集 ,等价于t.intersection(s) 
c = t - s          # 求差集（项在t中，但不在s中）  ,等价于t.difference(s) 
d = t ^ s          # 对称差集（项在t或s中，但不会同时出现在二者中）,等价于t.symmetric_difference(s)