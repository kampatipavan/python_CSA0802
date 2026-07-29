n = input()

result = ""

for digit in n:
    if digit == '9':
        result += '0'
    else:
        result += str(int(digit) + 1)

print(result)