n = int(input())

num = n + 1

while True:
    prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)
        break

    num += 1