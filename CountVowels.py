word = input("Enter a word: ").lower()

vowel_count = 0

for letter in word:
    if letter in "aeiou":
        vowel_count += 1
print(f"the word {word} contains {vowel_count} vowel(s)")
