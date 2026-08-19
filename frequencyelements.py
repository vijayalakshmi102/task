n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

for i in range(n):
    count = 0

    for j in range(n):
        if arr[i] == arr[j]:
            count = count + 1
    already = 0

    for k in range(i):
        if arr[i] == arr[k]:
            already = 1
            break

    if already == 0:
        print(arr[i], ":", count)