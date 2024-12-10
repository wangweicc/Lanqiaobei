# import math
#
#
# class Rect:
#     def __init__(self, l, h, z):
#         if l <= 0 or h <= 0 or z <= 0:
#             raise ValueError("Invalid dimensions")
#         self.l = l
#         self.h = h
#         self.z = z
#
#     def length(self):
#         return 2 * (self.l + self.h)
#
#     def area(self):
#         return self.l * self.h
#
#
# class Cubic(Rect):
#     def __init__(self, l, h, z):
#         super().__init__(l, h, z)
#
#     def surface_area(self):
#         return 2 * (self.l * self.h + self.l * self.z + self.h * self.z)
#
#     def volume(self):
#         return self.l * self.h * self.z
#
#
# class Pyramid(Rect):
#     def __init__(self, l, h, z):
#         super().__init__(l, h, z)
#
#     def surface_area(self):
#         slant_height = math.sqrt((self.z / 2) ** 2 + self.h ** 2)
#         lateral_area = 2 * (self.l * slant_height + self.h * slant_height)
#         return self.area() + lateral_area
#
#     def volume(self):
#         return (1 / 3) * self.area() * self.z
#
#
# class ShapeTest:
#     @staticmethod
#     def test_shapes():
#         import sys
#         input = sys.stdin.read
#         data = input().strip().split('\n')
#
#         for line in data:
#             numbers = list(map(float, line.split()))
#             cubic_surface_area = 0.0
#             cubic_volume = 0.0
#             pyramid_surface_area = 0.0
#             pyramid_volume = 0.0
#             try:
#                 cubic = Cubic(*numbers)
#                 cubic_surface_area = cubic.surface_area()
#                 cubic_volume = cubic.volume()
#
#                 pyramid = Pyramid(*numbers)
#                 pyramid_surface_area = pyramid.surface_area()
#                 pyramid_volume = pyramid.volume()
#             except ValueError:
#                 pass
#
#             print(f"{cubic_surface_area:.2f} {cubic_volume:.2f} {pyramid_surface_area:.2f} {pyramid_volume:.2f}")
#
#
# if __name__ == "__main__":
#     ShapeTest.test_shapes()


# def abbreviate_journal_name(journal_name):
#     # 将期刊名转换为小写
#     journal_name = journal_name.lower()
#     # 按空格分割成单词
#     words = journal_name.split()
#     # 处理每个单词
#     abbreviated_words = []
#     for word in words:
#         if len(word) <= 4:
#             abbreviated_words.append(word)
#         else:
#             abbreviated_words.append(word[:4] + '.')
#     # 将处理后的单词重新组合成一个字符串
#     return ' '.join(abbreviated_words)
#
# # 读取输入
# T = int(input())
# for _ in range(T):
#     journal_name = input().strip()
#     result = abbreviate_journal_name(journal_name)
#     print(result)


# def format_string(s):
#     # 使用 rjust 方法将字符串右对齐，不足部分用星号 * 补足
#     formatted_string = s.rjust(8, '*')
#     return formatted_string
#
# # 读取输入
# input_string = input().strip()
#
# # 格式化字符串
# output_string = format_string(input_string)
#
# # 输出结果
# print(output_string)


# def extract_info(id_number):
#     # 检查身份证号是否为18位
#     if len(id_number) != 18:
#         return "输入的身份证号位数错"
#
#     # 提取出生日期
#     birth_year = id_number[6:10]
#     birth_month = id_number[10:12]
#     birth_day = id_number[12:14]
#     birth_date = f"{birth_year}年{birth_month}月{birth_day}日"
#
#     # 提取性别
#     gender_digit = int(id_number[16])
#     gender = "男" if gender_digit % 2 != 0 else "女"
#
#     return f"{gender}\n出生于{birth_date}"
#
#
# # 读取输入
# id_number = input().strip()
#
# # 输出结果
# print(extract_info(id_number))


"""
1.定义一个汽车类(Car),属性有颜色，品牌，车牌号，价格，并实例化两个对象，给属性赋值，并输入属性值。
比如：属性：“红色”，”奔驰“，”黑A00000“，15000000
"""
# class Car:
#     def __init__(self, color, brand, license_plate, price):
#         self.color = color
#         self.brand = brand
#         self.license_plate = license_plate
#         self.price = price
#
#     def display_info(self):
#         print(f"汽车信息: 颜色 - {self.color}, 品牌 - {self.brand}, 车牌号 - {self.license_plate}, 价格 - {self.price}")
#
# car1 = Car("红色", "奔驰", "黑A00000", 15000000)
# car1.display_info()
#
# car2 = Car("蓝色", "宝马", "京B12345", 12000000)
# car2.display_info()


"""
2．创建一个学生类stu，属性包括姓名、性别和年龄以及爱好，并实例化对象stuA.
"""
# class Stu:
#     def __init__(self, name, gender, age, hobbies):
#         self.name = name
#         self.gender = gender
#         self.age = age
#         self.hobbies = hobbies
#     def display_info(self):
#         print(f"学生信息: 姓名 - {self.name}, 性别 - {self.gender}, 年龄 - {self.age}, 爱好 - {', '.join(self.hobbies)}")
# stuA = Stu("张三", "男", 20, ["阅读", "篮球", "编程"])
# stuA.display_info()


"""
3. 自定义类，计算java，sql，web三门课的总成绩和平均分
"""
# class StudentGrades:
#     def __init__(self, java_score, sql_score, web_score):
#         self.java_score = java_score
#         self.sql_score = sql_score
#         self.web_score = web_score
#     def calculate_total(self):
#         return self.java_score + self.sql_score + self.web_score
#     def calculate_average(self):
#         total = self.calculate_total()
#         return total / 3
#     def display_results(self):
#         total = self.calculate_total()
#         average = self.calculate_average()
#         print(f"总成绩: {total}")
#         print(f"平均分: {average:.2f}")
# java_score,sql_score,web_score = map(int,input().split())
# grades = StudentGrades(java_score, sql_score, web_score)
# grades.display_results()



"""
1.判断字符串 a = “welcome to my world” 是否包含单词 b = “world”，包含返回 True，不包含返回 False。
"""
# a = "welcome to my world"
# b = "world"
# if b in a:
#     print(True)
# else:
#     print(False)


"""
2. 编写一个 Python 程序，接收用户输入的字符串，然后输出该字符串反转后的结果。
"""
# user_input = input("请输入一个字符串: ")
# reversed_string = user_input[::-1]
# print("反转后的字符串:", reversed_string)


"""
3. s = 'foo'
t = 'bar'
print('barf' in 2 * (s + t))结果是：
"""
# s = 'foo'
# t = 'bar'
# print('barf' in 2 * (s + t))       # 2 * (s + t) -> foobarfoobar


"""
4.生成无数字的全字母的字符串
"""
# import random
# import string
# def random_string(length):
#     letters = string.ascii_letters
#     random_string = ''.join(random.choices(letters, k=length))
#     return random_string
#
# length_of_string = int(input("请输入你想要生成的字符串长度: "))
# generated_string = random_string(length_of_string)
# print("生成的随机字符串:", generated_string)



# import os

# def list_mp3_files(directory):
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             if file.endswith(".mp3"):
#                 print(os.path.join(root, file))

# # 指定目录路径
# directory = "d:/test"

# # 调用函数
# list_mp3_files(directory)



# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)

# # 实例化 Rectangle 类
# rect = Rectangle(5.2, 3.4)

# # 输出矩形的面积和周长，保留两位小数
# print(f"矩形的面积是: {rect.area():.2f}")
# print(f"矩形的周长是: {rect.perimeter():.2f}")


# s = 'This reference manual describes the syntax and “core semantics” of the language. It is terse, but attempts to be exact and complete.'

# # 定义元音字母集合
# vowels = set('aeiouAEIOU')

# # 使用列表推导式生成元音字母列表
# vowel_count = len([char for char in s if char in vowels])

# print(f"字符串中元音字母的个数是: {vowel_count}")



# s = 'This reference manual describes the syntax and “core semantics” of the language. It is terse, but attempts to be exact and complete.'

# # 将字符串转换成列表
# s_list = list(s)

# # 使用正向切片从第二位开始，隔两位取到n-1位
# s_list = s_list[1:-1:2]

# # 使用反向切片让列表倒序
# s_list = s_list[::-1]

# print(s_list)




# s = 'This reference manual describes the syntax and “core semantics” of the language. It is terse, but attempts to be exact and complete.'

# # 使用find函数获取syntax的位置信息
# syntax_index_find = s.find('syntax')
# print(f"使用find函数获取syntax的位置信息: {syntax_index_find}")

# # 使用index函数获取syntax的位置信息
# syntax_index_index = s.index('syntax')
# print(f"使用index函数获取syntax的位置信息: {syntax_index_index}")

# # 使用正则表达式将language单词替换成python
# import re
# s_replaced = re.sub(r'\blanguage\b', 'python', s)
# print(f"替换后的字符串: {s_replaced}")


import random

# 使用列表推导式生成一个包含100个随机整数的列表
data_list = [random.randint(1, 1000) for _ in range(100)]

# 添加元素
new_element = 1000
data_list.append(new_element)

# 删除元素
element_to_remove = data_list[0]
data_list.remove(element_to_remove)

# 修改元素
index_to_modify = 10
new_value = 2000
data_list[index_to_modify] = new_value

# 获取最大值、最小值、平均值
max_value = max(data_list)
min_value = min(data_list)
average_value = sum(data_list) / len(data_list)

# 输出列表元素及位置信息
print("列表元素及位置信息:")
for index, element in enumerate(data_list):
    print(f"位置 {index}: {element}")

# 输出最大值、最小值、平均值
print(f"最大值: {max_value}")
print(f"最小值: {min_value}")
print(f"平均值: {average_value:.2f}")
