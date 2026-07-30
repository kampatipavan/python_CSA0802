s = input().lower()

vowels = "aeiou"
vowel_count = {}
consonant_count = {}

total_vowels = 0
total_consonants = 0

for ch in s:
    if ch.isalpha():
        if ch in vowels:
            total_vowels += 1
            if ch in vowel_count:
                vowel_count[ch] += 1
            else:
                vowel_count[ch] = 1
        else:
            total_consonants += 1
            if ch in consonant_count:
                consonant_count[ch] += 1
            else:
                consonant_count[ch] = 1

print("Vowels:", total_vowels)
print("Consonants:", total_consonants)

if vowel_count:
    mv = max(vowel_count, key=vowel_count.get)
    print("Most Frequent Vowel:", mv, "(", vowel_count[mv], ")")
else:
    print("Most Frequent Vowel: None")

if consonant_count:
    lc = min(consonant_count, key=consonant_count.get)
    print("Least Frequent Consonant:", lc, "(", consonant_count[lc], ")")
else:
    print("Least Frequent Consonant: None")

if total_consonants != 0:
    ratio = total_vowels / total_consonants
    print("Vowel-to-Consonant Ratio:", round(ratio, 2))
else:
    print("Vowel-to-Consonant Ratio: Undefined")