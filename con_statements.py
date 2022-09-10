phone_balance = 7
bank_balance = 100

if  phone_balance <5:
    phone_balance += 10
    bank_balance -= 10

    print(phone_balance, bank_balance)

n = 15
if  n%2 == 0:
    print("Number " + str(n) + " is even.")
else:
    print("Number " + str(n) + " is odd.")
    print(n)

a = 7
b = 2
print(a%b)

n = 5
if  n%2 != 0:
    print("Number " + str(n) + " is odd.")
else:
    print("Number " + str(n) + " is even.")
    print(n)

for number in range(1, 10):
    if(number % 2 != 0):
        print(number)