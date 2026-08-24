n = int(input())

array = []
for i in range(n):
    a = int(input())
    array.append(a)

sorted(array, reverse=True)
for i in array:
    print(i,end=" ")
