n = input()

step = True

for i in range(len(n) - 1):
    if abs(int(n[i]) - int(n[i + 1])) != 1:
        step = False
        break

if step:
    print("Yes")
else:
    print("No")