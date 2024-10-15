# random code for exercise 6 Github

def check_number(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = 21
result = check_number(number)
print(f"{number} is {result}")
