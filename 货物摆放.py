# import os
# import sys
# # 因素+背包（求因子）+遍历
# # 不到50毫秒！！！！！！！！！！
# # 请在此输入您的代码
# n=2021041820210418
# l=[]     # ！！！！用于存因数不是因子例如：10=2*5
# i=2
# x=n
# while i<pow(x,0.5)+1:
#     if x%i==0:
#         l.append(i)
#         x=x//i
#     else:
#         i+=1
# l.append(x)
# print(l)
# s=set()     # ！！！！用于存因子 如10=1*2*5*10
# s.add(1)
# for j in l:
#     p=set()
#     for k in s:
#         p.add(j*k)
#     for k in p:
#         s.add(k)
#         print(s)
# count=0
# for k1 in s:             # 遍历两层求解
#     for k2 in s:
#         if n%(k1*k2)==0:
#             count+=1
# print(count)


"""
a= [1, 2, 3, 99, 100, 6, 7] True
b= [1, 2, 3, 99, 100, 6, 7]
c= [1, 2, 3, 4, 5, 6, 7] False
"""
# a = [1,2,3,4,5,6,7]
# b = a
# c = a[:]
# a[3:5] = 99,100
# print("a=",a,id(a)==id(b))
# print("b=",b)
# print("c=",c,id(c)==id(a))



"""Enter a range of positive integers. After removing the integers containing duplicate digits, print the integers from smallest to largest in the form of 5 per line.

Input Specification:
Input the range of integers.

Output Specification:
Output the result. The data is arranged from small to large, with 5 in each line. Each number takes up 8 columns.

Sample Input :
87 123
Sample Output :
      87      89      90      91      92
      93      94      95      96      97
      98     102     103     104     105
     106     107     108     109     120
     123"""


# def amd(n):
#     return len(set(str(n))) == len(str(n))
# start, end = map(int, input().split())
# a = [n for n in range(start, end + 1) if amd(n)]
# a.sort()
# for i, num in enumerate(a):
#     print(f'{num:8}', end='')
#     if (i + 1) % 5 == 0:
#         print()

#
# def amd(n):
#     return len(set(str(n))) == len(str(n))
# start, end = map(int, input().split())
# a = [n for n in range(start, end + 1) if amd(n)]
# a.sort()
# for i,num in enumerate(a):
#     print(f"{num:8}",end='')
#     if (i + 1) % 5 == 0:
#         print()

