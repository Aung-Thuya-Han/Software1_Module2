import random

random_num1 = random.randint(0, 9)
random_num2 = random.randint(0, 9)
random_num3 = random.randint(0, 9)

three_digit_code = str(random_num1) + str(random_num2) + str(random_num3)

print("3-digit code is", three_digit_code)

random_num1 = random.randint(1, 6)
random_num2 = random.randint(1, 6)
random_num3 = random.randint(1, 6)
random_num4 = random.randint(1, 6)

four_digit_code = str(random_num1) + str(random_num2) + str(random_num3) + str(random_num4)

print("4-digit code is",four_digit_code)