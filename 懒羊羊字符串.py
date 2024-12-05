import os
import sys

i = int(input())
k = 0
for j in range(i):
    s = input()
    if ord(s[1]) == ord(s[2]) and ord(s[0]) != ord(s[1]):
        k += 1
print(k)
