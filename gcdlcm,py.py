a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

num1 = a
num2 = b

while num2 != 0:
    temp = num2
    num2 = num1 % num2
    num1 = temp

gcd = num1
lcm = (a * b) // gcd

print("GCD =", gcd)
print("LCM =", lcm)