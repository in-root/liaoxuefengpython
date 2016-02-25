#! /usr/bin/env python 
# encoding: utf-8
print "hello, world!"

print "hello,tom","jim","lili"

name=raw_input()
print "my name is :",name

age=int(raw_input("please imput your age: "))
print "my age is :", age

sex=raw_input("亲，输入你的性别： ")
print "I am a ",sex

print '欢迎新成员%s,他是一个%d岁的%s' % (name,age,sex)
print '多行显示：'
print  '''line1
line2
lien3'''

print ' 添加r 不转义'
print r'\\\n\\'
print '\\\n\\'

print '单引号作为一个字符'
print " I'm tom！"

print "单双引号都作为一个字符"
print 'I\'m \"OK\"'


#print '布尔值： True 和 False 可以直接来表示 布尔值  
#布尔值是可以用来进行 与 或 非！'

print " 看看 输入一个字符串 或者一个数字 有什么方法。"
print "下面你需要进行三次的输入！"
name1=raw_input()
print name1
print type(name1)
name2=int(raw_input())
print name2
print type(name2)
name3=input()
print name3
print type(name3)
print "以上的几点要特别引起注意！"
