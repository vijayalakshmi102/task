s = input("Enter a value: ")

vowels = 0
consonants = 0

for i in range(len(s)):
    ch = s[i]

    if ch.lower() in "aeiou":
        vowels = vowels + 1

    elif ch.isalpha():
        consonants = consonants + 1

print("Vowels:", vowels)
print("Consonants:", consonants)