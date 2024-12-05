total_amount = 1000000
sum_of_digits = 0

while total_amount > 0:
    remainder = total_amount % 7
    total_amount = total_amount // 7
    sum_of_digits += remainder
    print(remainder)
    print(total_amount)
print(sum_of_digits)