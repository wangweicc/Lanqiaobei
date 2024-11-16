"""
(编写一个小程序，运行后提示:请输入您的姓名:输入姓名XX后返回信息:您好!XX)
"""
# a = input("请输入您的姓名：")
# print(f"您好！{a}")

"""
(编写一个小程序，运行后提示:请输入A值:输入A的数值回车后
继续提示:请输入B值:输入B的数值后后返回信息:A+B的结果为:X)
"""
# a = int(input("请输入A的值："))
# b = int(input("请输入B的值："))
# c = a + b
# print(c)

"""
(输入姓名、年龄、身高，按照“姓名-年龄-身高”格式,且不换行的输出)
"""
# a = input("请输入您的姓名：")
# b = input("请输入您的年龄：")
# c = input("请输入您的身高：")
# print(f"{a}-{b}-{c}")

"""
(通过键盘输入两个值，完成交换输出 3种方法)
"""
# a = int(input("请输入一个值:"))
# b = int(input("请输入一个值:"))

# a,b = b,a

# c = a
# a = b
# b = c

# a = a+b
# b = a-b
# a = a-b
# print(f"交换后的值为：{a},{b}")

""" 
汇率计算器(输入美元数量，计算可兑换的人民币数量并输出)
"""
# a = float(input("请输入美元数："))
# b = 7*a
# print(f"可兑换的人民币数量为：{b}")

"""
将输入的两数转换为斤两数(1斤为16两)
"""
# a = float(input("请输入两数："))
# b = a//16
# c = a%16
# print(f"{a}两是{b}斤{c}两")

"""
让用户输入一个四位整数，计算每一位相加的结果并输出 如输入1234 输出10
"""
# a = int(input("请输入一个四位整数："))
# ge = a%10
# shi = a//10%10
# bai = a//100%10
# qian = a//1000
# sum = ge+shi+bai+qian
# print(f"和为{sum}")

"""
闰年的判断(布尔值这里暂不使用IF函数)
"""
# a = int(input("请输入一个年份："))
# if a%400 == 0:
#     print(f"{a}是世纪闰年")
# elif a%4 == 0 and a%100 != 0:
#     print(f"{a}是闰年")
# else:
#     print(f"{a}是平年")

# a = int(input("请输入一个年份,判断是否为闰年，闰年返回true,平年返回false:"))
# print(a%400 == 0 or a%4 == 0 and a%100 != 0)

"""
输入三条边的数值，判断是否能构成三角形(这里暂不使用IF函数)
"""
# a = int(input("请输入第一条边："))
# b = int(input("请输入第二条边："))
# c = int(input("请输入第三条边："))
# q = a+b>c and a+c>b and b+c>a
# print("构成三角形的结果为",q)

"""
日期格式替换(字符串 2024-9-23->2024年9月23日)
"""
# a = input("请输入日期，格式为yyyy-mm-dd:")
# a2 = a.replace("-","年",1)
# a3 = a.replace("-","月")
# a4 = a3+"日"
# print(a4)

# a = input("请输入一个字符串，是浮点数返回Ture,否则返回False:")
# print(a.count(".")==1 and a.replace(".","").isdigit())

# shi1 = int(input("请输入起始时数："))
# fen1 = int(input("请输入起始分数："))
# miao1 = int(input("请输入起始秒数："))
# time1 = shi1*3600+fen1*60+miao1
# shi2 = int(input("请输入结束时数："))
# fen2 = int(input("请输入结束分数："))
# miao2 = int(input("请输入结束秒数："))
# time2 = shi2*3600+fen2*60+miao2
# print(f"相隔时间秒数为:{abs(time2-time1)}秒")

# a = input("请输入一个四位数：")
# b = int(a[0])+int(a[1])+int(a[2])+int(a[3])
# print("相加结果为：",b)

# a = input("请输入一个字符串,是回文返回True,否则返回False：")
# b = a[::-1]
# print(a==b)

# a = input("请输入一个小数：")
# b = a.find(".")
# c = a[0:b]
# print(c)

# import math
# a = input("请输入一个小数：")
# b = float(a)
# c = round(b)
# print(c)
# 四舍五入

# a = int(input("请输入月份："))
# if a==3 or a==4 or a==5:
#     print("春天")
# elif a==6 or a==7 or a==8:
#     print("夏天")
# elif a==9 or a==10 or a==11:
#     print("秋天")
# elif a==12 or a==1 or a==2:
#     print("冬天")
# else:
#     print("请输入正确的月份！")

# a = int(input("请输入年份："))
# if a%400==0:
#     print(a,"年是世纪闰年")
# elif a%4==0 and a%100 !=0:
#     print(a,"年是普通闰年")
# else:
#     print(a,"年是平年")

# a = input("请输入一个同学的体重：")
# b = input("请输入一个同学的体重：")
# c = input("请输入一个同学的体重：")
# d = input("请输入一个同学的体重：")
# e = max(a,b,c,d)
# print(e)

# a = input().split(" ")
# c = max(a)
# print(c)

# a = int(input("请输入公里数："))
# if a<=0:
#     print("输入错误！")
# elif a<=3:
#     print("花费13元")
# elif a<=15:
#     b = 13+(a-3)*2.3
#     print("花费",round(b),"元")
# elif a>15:
#     b = 13+(15-3)*2.3+(a-15)*1.5
#     if b>=100:
#         b=100
#     print("花费",round(b),"元")


# a = int(input("请输入公里数："))
# if a<=0:
#     print("输入错误！")
# elif a<=3:
#     b = 13
# elif a<=15:
#     b = 13+(a-3)*2.3
# elif a>15:
#     b = 13+(15-3)*2.3+(a-15)*1.5
#     if b>=100:
#         b=100
# print("花费",round(b),"元")

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# for i in range(1,6):
#     print("*"*i)

# d = {'a':1,'b':2,'c':3}
# c = d.items()
# print(c)
# for k,v in c:
#     print(k,v,end=" ")

# lis = [1,2,3,4,1,2,5]
# p = list(set(lis))
# print(p)

# dicta = {'a':1,'b':2,'c':3,'d':4,'f':'Hello'}
# dictb = {'b':3,'d':5,'e':7,'m':9,'k':'World'}
# dictc = {}
# for ia in dicta:
#     if ia in dictb:
#         dictc[ia] = dicta[ia]+dictb[ia]
#     else:
#         dictc[ia] = dicta[ia]
# for ib in dictb:
#     if ib not in dicta:
#         dictc[ib] = dictb[ib]
# print(dictc)

# 求1-2+3-4+5...99的所有数的和
# sum = 0
# count = 1
# while count <100:
#     if count%2==0:
#         sum = sum-count
#     else:
#         sum = sum+count
#     count +=1
# print(sum)

# li = ['xiaobai ','aldxC','AdC ','dgon',' Gitian','Xusir',' aqc']
# b =[]
# for i in li:
#     a=i.strip()
#     if a[0].upper()=="A" and a[-1]=='c':
#         b.append(a)
# for x in b:
#     print(x)


# def sum(a,b):
#     c=a+b
#     return c
# a=1
# b=2
# d = sum(a,b)
# print(d)


"""练习1：请将下述程序补充完整并上机调试，将列表中的全部元素值修改为其值的平方。程序的期望输出为:[1, 4, 9, 16]"""

# def squ(lst):
#     for i in range(len(lst)):
#         lst[i]=lst[i]**2
#     return lst
# m = [1,2,3,4]
# squ(m)
# print(m)

"""编写函数pay()，带两个输入参数：小时工资和上周员工工作了的小时数。函数计算并返回员工的工资。
加班工资的计算方法如下：大于40小时但小于或等于60小时按平时小时薪酬的1.5倍给薪；
大于60小时则按平时小时薪酬的2倍给薪。"""

def pay(s,h):
    if 0<=h<=40:
        c=s*h
    elif 40<h<=60:
        c=(h-40)*1.5*s+40*s
    else:
        c=(h-60)*2*s+20*1.5*s+40*s
    return c
s = int(input("小时工资："))
h = int(input("小时数："))
print(pay(s,h))