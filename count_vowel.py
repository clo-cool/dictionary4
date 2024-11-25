vowels = {
    "a":0, 
    "e":0,
    "i":0,
    "o":0,
    "u":0
  }
sen = input("Tell me a silly sentence: ")
print(sen)
print(type(sen))

for letter in sen:
    print(letter)
    if letter in vowels:
        vowels[letter] += 1

print(vowels)

#cheching if a sentence is a pangram - a sentence that has all the letters

letters = {
    "a":0,
    "b":0,
    "c":0,
    "d":0,
    "e":0,
    "f":0,
    "g":0,
    "h":0,
    "i":0,
    "j":0,
    "k":0,
    "l":0,
    "m":0,
    "n":0,
    "o":0,
    "p":0,
    "q":0,
    "r":0,
    "s":0,
    "t":0,
    "u":0,
    "v":0,
    "w":0,
    "x":0,
    "y":0,
    "z":0
}

sen2 = input("Tell me a cool sentence")
print(sen2)

is_pangram = True
for letter in sen2:
    if letter in letters:
        letters[letter] +=1

for key in letters:
  if letters[key] == 0:
      is_pangram = False

if is_pangram == True:
    print("Sentence is a pangram")
        
else:
    print("Sentence is not a pangram")
    

