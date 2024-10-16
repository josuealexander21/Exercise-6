print("hello!")
print("goodbye")
def check_number(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
number = 12
result = check_number(number)
print(f"{number} is {result}")
