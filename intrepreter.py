#ask the user to write math
math = (input("Expression: "))
x, z, y = math.split(" ")
x = float(x)
y = float(y)
if z == "+":
    print(x+y)
elif z == "-":
    print(x-y)

elif z == "*":
    print(x*y)
elif z =="/":
    print(x/y)
elif z== "%":
    print(x%y)
