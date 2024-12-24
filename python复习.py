# 1. 导入标准库math中的所有对象。
# from math import *


# 2. 导入标准库math中对象sin，并给对象sin取个别名a
# from math import sin as a


# 3. x=3+4j
# 计算负数的模：
# x=3+4j
# x_mo = abs(x)
# print(x_mo)

# 输出x的虚部
# x=3+4j
# imag = x.imag
# print(imag)

# 输出x的实部
# x=3+4j
# real = x.real
# print(real)


# 4.
# print(-11/3)
# print(-11//3)
# print(-11%3)

# 5.
# print(2**3**2)    //512

# 6.
# print([1,2,3]<[1,2,4])    //True
# print({1,2,3}<{1,2,4})    //False
# print(5 in range(1,10,2))    //True

# 7.
# print({1,2,3}&{3,4,5})  # {3}
# print({1,2,3}|{2,3,4})  # {1,2,3,4}
# print({1,2,3}^{3,4,5})  # {1,2,4,5}
# print({1,2,3}-{4,5,6})  # {1,2,3}

# 8.
# print(3<5 and 5 or 4<2)     # 5
# print(3>5 or 5 and 4>2)     # True

# 9.
# print(int('111',2))
# print(max(['1','22','111'],key=len))
# print(sorted([12,3,5,1],reverse=True))

# 10.使用enumerate()函数返回列表list1=[11,12,13,14]的索引和元素。
# list1=[11,12,13,14]
# for index, value in enumerate(list1,start=0):
#     print(f'{index}:{value}')

# 11. list(map(lambda x,y:x+y,range(5),range(5,10)))结果是多少？
# print(list(map(lambda x,y:x+y,range(5),range(5,10))))

# 12.
# from functools import reduce
# reduce(lambda x,y:x+y,range(1,10))结果是多少
# from functools import reduce
# print(reduce(lambda x,y:x+y,range(1,10)))

# 13. list(filter(lambda x:x%2==1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))的结果是多少
# print(list(filter(lambda x:x%2==1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

# 14. list(filter(lambda x: x[0].lower() in 'aeiou', ['Sammy', 'Ashley', 'Jo', 'Olly', 'Jackie', 'Charlie']))结果是多少？
# print(list(filter(lambda x: x[0].lower() in 'aeiou', ['Sammy', 'Ashley', 'Jo', 'Olly', 'Jackie', 'Charlie'])))

# 15.
# print(list(range(1,10,2)))
# print(list(range(9,0,-2)))

# 16.
# print(list(zip([1,2,3],['a','b'],['.','!','#'])))

# 17.
# x=[1,2,3]
# x.append(0)
# x.insert(0,4)
# x.reverse()
# x.extend([5,6,7])
# print(x)

# 18.
# x=[0,1,2,0,1,2,3]
# x.pop()
# x.pop(0)
# x.remove(0)
# x.reverse()
# 请输出x,x.count(1),x.index(2)

# x=[0,1,2,0,1,2,3]
# x.pop()
# x.pop(0)
# x.remove(0)
# x.reverse()
# print(x)
# print(x.count(1))
# print(x.index(2))

# 19.
# print([1,2,4]>[1,2,3,5])
# x=[1,2,3]
# x=x+[4]
# print(x)
# x=x*2
# print(x)

# 20.
# x=[1,2,3,4,5,6]
# print(max(x))
# print(min(x))
# print(sum(x)/len(x))
# print(any(x))


# 21.
# print(list(zip(range(4))))
# print(list(enumerate(range(4))))

# 22.
# print(len([i for i in 'Today is very beautiful' if i in 'aeiou']))

# 23.
# sum([num for i in [[1,2,3],[4,5,6],[7,8,9]] for num in i])

# 24.import os
# list([a for a in['beautiful','excited','found','greatful','successed']
# if a.endswith(('ful','ed'))])

# 25.
# x=[1,2,3,4,5]
# 请问x[::-1]、x[::2]、x[3:10]结果是？
# x[len(x):]=[5]
# x[:0]=[0]
# x[5:5]=[0]请输出x的结果。

# 26.
# x=[1,2,3,4,5,6]
# x[:3]=[1]*3
# x[3:]=[2]*2
# x[::2]=[0]*3
# print(x)

# 27.
# sum(1 for i in 'Today is very beautiful' if i in 'aeiou')

# 28.
# g=((i+2)**2 for i in range(5))
# g.__next__()
# g.__next__()
# next(g)

# 29.
# d=dict(zip(['a','b','c','d'],[1,2
# ,3,4]))
# d.keys()
# d.items()
# d.values()
# d.get('e',5)

# 30.
# d=dict(zip(['a','b','c','d'],[1,2,3,4]))
# d.update({'a':0,'d':5})
# print(d)
# d.popitem()
# d.pop('a')
# print(d)

# 31.编程统计‘aabbbccbddbccaa’字符串中每个字符出现的次数。

# 32.
# s={1,2,3,4,5}
# s.update({4,5,6})
# s.discard(7)
# s.remove(2)
# s.pop()
# print(s)

# 33.
# a={1,2,3,4}
# b={5,4,3}
# 请问a|b、a-b、a&b、 a^b
# 各是多少？

# 34.
# x,y,z=zip(['a','b','c'],[1,2,3])

# 35.
# 输入使用空格分隔的两个整数，然后按升序输出。

# 36.用三元运算符书写a，b两个数比大小的代码。

# 37.
# count = 0
# while count<12:
# count += 1
# else:
# print(count,'No')
# 以上输出的内容是什么？

# 38.
# count = 0
# for i in [0,1,2,3]:
# count=count+i
# else:
# print(count)
# 以上输出的内容是什么？

# 39．
# def df(a,b,c):
# print(a+b+c)
# d={'a': 4, 'b': 5, 'c': 4}
# df(*d.values())
# df(**d)

# 40．
# 定义一个Person类，三个属性name age和身高，一个方法
# show,该方法输出姓名、年龄和身高，要求输出的身高保留两
# 个小数。在 Person 类定义的基础上，定义 Student 类，继承
# Person 类，实例化Student类的对象，姓名李小龙，年龄20，身高1米8。

# 41.
# print(len("hello\tworld"))
# print("张三和李四的身高分别是{1:.2f}m，
# {0:.2f}m".format(1.8,2))

# 42. s="My hometown is very beautiful"
# print(s.find("e"))
# print(s.find("e",7))
# print(s.rfind("e"))
# print(s.index("e"))
# print(s.count("e"))

# 43.
# s=" \nMy hometown is very beautiful "
# print(s.split())
# s.strip()

# 44.
# s="Hello python"
# s.lower()
# s.upper()
# s.capitalize()
# s.title()
# s.swapcase()

# 45.
# s="Python is a simply language"
# print(re.sub(r's+\w+','good',s))

# 46.
# s="Python is a simply language"
# print(re.sub(r's+\w+','good',s))

# 47.
# 使用列表推导式列出D盘文件夹下所有扩展名为“.bmp”“.jpg”或“.gif”的图片。

# 48.
# 将s=“abcdefg”中的“e”替换成“0”输出s.

# 49.
# 用上下文管理语句with写出读取1.txt文件的内容的代码。

# 50.
# 遍历1.txt文本文件的所有行内容。

# 请说出以下代码的含义
# 51.
# os.listdir()
# os.getcwd()

# 52.
# os.path.basename(path)
# os.path.split(path)