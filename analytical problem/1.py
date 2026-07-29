def is_harshad(n):
    temp = n
    digit_sum = 0

    while temp > 0:
        digit_sum += temp % 10
        temp //= 10

    return n % digit_sum == 0


n = int(input("Enter a number: "))

if is_harshad(n):
    print(n, "is a Harshad Number")
else:
    print(n, "is NOT a Harshad Number")

print("\nHarshad Numbers from 1 to 500:")

for i in range(1, 501):
    if is_harshad(i):
        print(i, end=" ")