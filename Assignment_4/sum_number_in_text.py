import re

def sum_numbers(text):
    numbers = re.findall(r'\d+', text)
    total = sum(int(num) for num in numbers)
    return total

text = input("please type your sentences(contain as least 1 number):")
print("the sum of the numbers is :",sum_numbers(text) )