# import re
#
# contents = '''
# ruby
# rube
# Ruby on Rails
# Rube on Rails
# rubb on rails
# ruyye on rails
# ruee
# hello world
# '''
#
# # 正则表达式匹配以 ruby 或 rube 开头的行，不区分大小写
# p = re.compile(r'[Rr]ub[ye]\b')
#
# for line in contents.splitlines():
#     if p.match(line):
#         print(line)


# import re
#
# contents = '''
# 01234
# 1234567890
# ABCDEFG
# CODEJIAONANG123
# []
# +_)(91283)
# -*/124566ABV
# ab
# abc
# abcd
# www
# codejiaonang
# com
# pythonregext
# '''
#
# # 正则表达式匹配不包含小写字母的行
# p = re.compile(r'^[^a-z]*$')
#
# for line in contents.splitlines():
#     if p.match(line):
#         print(line)


# import re
#
# contents = '''
# abc01
# ddd02
# afcf01
# acac11
# 321
# acef33
# bbc000
# ABCDEFG789654
# CODEJIAONANG
# ghjkloiqwtq
# poiuy98765
# msstgr4567
# gg8888888
# 88888888999
# '''
#
# # 正则表达式匹配符合条件的字符串
# p = re.compile(r'^[a-zA-Z]{1,4}[0-9]{0,3}$|^([0-9]{1,3})$')
#
# for line in contents.splitlines():
#     if p.match(line):
#         print(line)


import re
# def correct_i(input_str):
#     # 正则表达式匹配单词中的大写 "I"
#     pattern = r'\B[I]\B'
#     # 替换匹配到的大写 "I" 为小写的 "i"
#     corrected_str = re.sub(pattern, 'i', input_str)
#     return corrected_str
# # 输入样例
# input_str = "I am a teacher,I am man, and I am 38 years old.I am not a busInessman."
# # 调用函数进行纠正
# output_str = correct_i(input_str)
# # 输出结果
# print(output_str)
#
#
# import re
# def correct_i(input_str):
#     pattern = r'\B[I]\B'
#     corrected_str = re.sub(pattern,'i',input_str)
#     return corrected_str
# input_str = "I am a teacher,I am man, and I am 38 years old.I am not a busInessman."
# output_str = correct_i(input_str)
# print(output_str)