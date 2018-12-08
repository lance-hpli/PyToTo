#-*- coding:utf-8 -*-
import multipro

#Py输入输出
print("ddd")
print(100+200)
# print()函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出，遇到逗号“,”会输出一个空格
print("100+200 = ",100+200) 
print("hello","world")

print('##input###################################')
#name = input('place input your name:')
#print("name:",name)
#print("license")
#print("您输入",input("请输入："))

#Py基础
print('##Py基础###################################')
a = 100
if a >= 0:    
    print(a)
else:
    print(-a)

print("#####整数#####")
a = 99999999999999999999    
print(a+a)

print("#####浮点数#####")
a = 1.23
if (a == 0.123e1) and 1 == 1:#e用于代替10
    print(True)
else:
    print(False)

print(2/3) #浮点数  
print(9/3) 
print(10//3)    #地板除，两个整数仍然为整数
print(9//2)
print(10%3)

print("#####字符串#####")
print('abc')  #abc
print("abc")  #abc
print('"abc"')  #"abc"
print("'abc'")  #'abc'
print("\"abd\'") #"abc'
print("\\") #\
print("\n\\") #换行+\
print("\\\n\\") #\+换行+\
print(r'\\\n\\') #\\\n\ #r表示
print('''line1
line2
line3''') #多行
True
False
3 > 2
True

x = 1
x= x +1
print(x)

a = 'ABC'
b = a
a = 'XYZ'
print(b)

print('##字符串编码###################################')
#py3.x,字符串以Unicode编码的，故支持多语言
print('包含中文的str')
print(ord('A'))   #获取字符整数部分
print(ord('中'))
print(chr(66))  #编码转换为字符
print(chr(25991))
print('\u4e2d\u6587','等价于',"中文")   #十六进制
x = b'ABC'   #bytes类型数据,显示内容与ABC一样，但每个字符只占一个字节
print('ABC的bytes:',x)
print("'中文'的bytes:",b'\xe4\xb8\xad\xe6\x96\x87')
print('ABC'.encode('ascii'))    #Unicode表示的str编码为字节bytes
#print('中文'.encode('ascii')) #超出范围
print('中文'.encode('utf-8'))
print(b'ABC'.decode('utf-8'))   #字节流转为str
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\xff'.decode('utf-8',errors='ignore')) #忽略错误字节
print(len('ABC'),len('中文'))   #字符个数
print(len(b'ABC'),len('中文'.encode('utf-8')))   #字节数

print('##格式化###################################')
print('Hello,%s Yes'%'world')
print('Hi, %s,you have $%d.,I have $%f' %('Michael',1000,1234.12))
print('%d-%02d' %(300,10))   #前补0至两位
print('%.2f' % 3.1415926) #四舍五入至两位小数
print('%.2f' % 3.145)
print('Age: %s. Gender: %s' % (25,True))   #%s永远有效
print('%d%%%d = %f' % (10,4,10%4))   #%%转义为%
print('Hello,{0},成绩提升了{1:.1f}%'.format('you',17.125))
s1=72
s2=85
r = s2/s1
print('%.1f' % r,r)

print('##list###################################')
classmates = ['M','B','T']
print(classmates,'的元素个数',len(classmates))

#multipro.run_proc('hell test')