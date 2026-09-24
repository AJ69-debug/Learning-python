vowels = ['a', 'e', 'i', 'o', 'u']
consonants = [
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 
    'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

text = "Hello, World! Python is fun."
vowels_Inword = []
consonants_Inword = []

for letter in text.lower():
    if letter in vowels:
        vowels_Inword.append(letter)
    if letter in consonants:
        consonants_Inword.append(letter)
    else:
        continue

print(len(vowels_Inword))
print(len(consonants_Inword))