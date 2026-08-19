s = input("Enter a string: ")

words = s.split()
result = ""

for word in words:
    result = result + word[::-1] + " "

print("Output:", result)