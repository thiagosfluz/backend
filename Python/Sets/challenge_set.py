text = set(input("Please, type a text: "))

print(text)

vowels = {"a", "e", "i", "o", "u"}

vowels_found = list(sorted(text.difference(vowels)))



print(vowels_found)
