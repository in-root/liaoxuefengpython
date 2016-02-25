# ! /usr/bin/env python 
# encoding: utf-8

classmates=['tom','jim','lili']

print '获取最后一个对象'
print classmates[-1]

print '在索引位置1插入liming'
classmates.insert(1,'liming')
print classmates

print "删除末尾元素"
classmates.pop()
print classmates

print "删除第二个位置的元素"
classmates.pop(1)
print classmates

print '替换第一个位置的内容'
classmates[1]='cjj'
print classmates


