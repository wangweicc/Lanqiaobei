import os
import sys

word = input()
a = 0
b = []
for i in word:
    c = word.count(i)
    if c >= a:
        a = c
for j in word:
    if word.append(j) == a:
        b.append(j)
b.sort()
print(b[0])
print(a)