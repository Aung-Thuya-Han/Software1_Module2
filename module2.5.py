user_choice_talent = float(input("Enter talents:\n"))
print()
user_choice_pound = float(input("Enter pounds:\n"))
print()
user_choice_lot = float(input("Enter lots:\n"))

total_pounds = (user_choice_talent * 20) + user_choice_pound
total_lots = (total_pounds * 32) + user_choice_lot
total_grams = total_lots * 13.3

print()
weight_in_kg = int(total_grams / 1000)

weight_in_g = float(total_grams % 1000)
print(f"The weight in modern units:\n{weight_in_kg} kilograms and {round(weight_in_g, 2)} grams.")