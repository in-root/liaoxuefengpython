# !/usr/bin/snv python
# encoding:utf-8

#元组是一种有序列表，只是一旦初始化  他便不能被修改。
#形式：classmate('jim','tom','lili')
#没有append insert  以及赋值的方法。


#定义元组的时候必须初始化
#当元组只有一个元素的时候 初始化的方式： t=(1,) 必须要有逗号 用来区分括号与元组。

我们常说元组是不可以变得，这里的不变指的是他们的指向，而并不是说内容不变。
譬如说下面的代码也是正确的
>>>t=('a','b',['A','B'])
>>>t[2][0]='X'
>>>t[2][1]='Y'
>>>t
('a','b',['X','Y'])

变化的是list而不是 元组本身，tuple一开始指向的list并没有变为别的list  。

t=('a',['a','b'])
print id(t[1])
t[1][0]=2
print id(t[1])






