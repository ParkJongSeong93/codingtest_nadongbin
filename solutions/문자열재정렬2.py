alpha = input()

alphabet = []
numbers = 0

for a in alpha:
    if a.isalpha():
        alphabet.append(a)
    else:
        numbers += int(a)

alphabet.sort()

for a in alphabet:
    print(a, end='')
print(numbers)