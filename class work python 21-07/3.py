n = input()

if len(n) == 1:
    print(n)
else:
    result = n[-1] + n[1:-1] + n[0]
    print(result)