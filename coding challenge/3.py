s = input()

print("Compressed:")

count = 1
compressed = ""

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        compressed += s[i - 1]
        if count > 1:
            compressed += str(count)
        count = 1

compressed += s[-1]
if count > 1:
    compressed += str(count)

print(compressed)

decompressed = ""
i = 0

while i < len(compressed):
    ch = compressed[i]
    i += 1
    num = ""

    while i < len(compressed) and compressed[i].isdigit():
        num += compressed[i]
        i += 1

    if num == "":
        decompressed += ch
    else:
        decompressed += ch * int(num)

print("Decompressed:", decompressed)