import os
import sys
import math
n = int(input())
a = []
sum2 = 0
sum3 = 0
for i in range(n):
    m = int(input())
    a.append(m)

for j in a:
    if j >= 60:
        sum2 += 1

for k in a:
    if k >= 85:
        sum3 += 1

baifen1 = round((sum2 / n) * 100)
baifen2 = round((sum3 / n) * 100)
print(f"{baifen1}%")
print(f"{baifen2}%")