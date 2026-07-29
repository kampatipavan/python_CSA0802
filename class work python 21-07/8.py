n = input()

odd = []

for digit in n:
    if int(digit) % 2 != 0:
        odd.append(digit)

odd = odd[::-1]

print("".join(odd))