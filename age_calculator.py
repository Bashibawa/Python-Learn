from datetime import date

inp = int(input("Enter your birth year: "))

def age(year):
    return date.today().year - year

print(f"Your age is: {age(inp)}")