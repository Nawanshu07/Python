vowels = ['a', 'e', 'i', 'o', 'u',
          'A', 'E', 'I', 'O', 'U']

word = input("Enter any word: ")

v = 0
for letter in word:
    if letter in vowels:
        v +=1 

print(f"Your word contains {v} number of vowels")

