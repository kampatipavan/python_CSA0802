n = input()

odd = ""
even = ""

for digit in n:
    if int(digit) % 2 == 0:
        even += digit
    else:
        odd += digit

print(odd + even)