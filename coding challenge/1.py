s = input()
count = {}

for ch in s.lower():
    if ch != ' ':
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

for ch in sorted(count):
    print(ch, ":", count[ch])