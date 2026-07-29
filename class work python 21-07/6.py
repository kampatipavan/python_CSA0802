n = input()

even = []

for digit in n:
    if int(digit) % 2 == 0:
        even.append(digit)

even = even[::-1]

j = 0
result = ""

for digit in n:
    if int(digit) % 2 == 0:
        result += even[j]
        j += 1
    else:
        result += digit

print(result)