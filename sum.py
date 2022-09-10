a = True
b = False
print(a or a and b and a)

x = 5
def cg():
    global x
    return x+1
print(cg())

l = list("1234")
l[0] = l[1] = 5
print(l)

x = 20
while x<20:
    x = x+3
print(x)