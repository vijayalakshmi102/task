number = int(input("Enter a number: "))

count = 0

while number > 0:
    count = count + 1
    number = number // 10

print("Number of digits =", count)