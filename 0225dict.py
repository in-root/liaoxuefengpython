# !/usr/bin/env python 
# encoding:utf-8
#字典在其他的语言中称之为 map  通过K：V 的形式，便于快速的查找。
#这种 K：V 的存储方法，再放入的时候，必须要根据key算出 value 的存放位置。

# 判断一个K是否存在 1: 通过 in 的方式。
#                   2：通过dict 提供的 get 方法，

d={'jim':11,'bob':12,'kim':13}

print 'jim' in d

d.get('bob')     #如果对应的key不存在，返回 none 

d.get('bob',-1)  # 或者是自己指定的value 此处为 -1

print '删除一个key'
pop(key)

#dict  占用的内存多，浪费内存空间  常常用于高速查找。

# dict 中的key 必须是不可变的对象。
#因为每一次dict 根据key 来哈希计算value的存储位置，如果key在变化，那么就会出现混乱。    
#字符串 和整数 都是不可变对象  可以作为 key  但是list 不能。
