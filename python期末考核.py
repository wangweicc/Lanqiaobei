import re
import os
import jieba
from openpyxl import Workbook

# (1) 打开文本文件，读取文件内容
file_path = r'D:\develop\pycharm\pycharm2024.1.4\python-code\26_002096_2015.txt'
with open(file_path,'r',encoding='utf-8') as fp:
    content = fp.read()

# (2) 使用正则表达式替换掉文本中非汉字的字符
chinese_only = re.sub(r'[^\u4e00-\u9fff]', '', content)

# (3) 对处理后的汉字进行分词
words = jieba.lcut(chinese_only)

# (4) 统计词频（要求用字典做,不能用collections库中函数）
word_frequency = {}
for word in words:
    if word not in word_frequency:
        word_frequency[word] = 1
    else:
        word_frequency[word] += 1
print(word_frequency.items())

# (5) 统计结果排序，取出现次数最多的10个词及出现的次数
sorted_word_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)[:10]

# (6) 使用os库中的函数取文本文件的主文件名的股票代码和年份
base_name = os.path.splitext(os.path.basename(file_path))[0]
stock_code = base_name.split('_')[1]
year = base_name.split('_')[2]

# (7) 将统计结果存入学号_姓名.xlsx文件中
wb = Workbook()
ws = wb.active
ws.title = "Word Frequency"

# 表头
ws.append([f'股票代码 {stock_code}', f'年份 {year}'])

# 数据
for word, frequency in sorted_word_frequency:
    ws.append([word, frequency])

# 保存文件
output_file = '150923045_王伟.xlsx'
wb.save(output_file)

print(f"数据已成功写入{output_file}")

