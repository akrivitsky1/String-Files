## constant that stores vowels 
vowels = [ "a" , "e" , "i" , "o" , "u"]
###asks user for a word 
word = input("Enter a word to translate:")
## turns word lowercase and creates variable for first pos of word
word = word.lower()
first_pos = word[0]
### if the first letter of the word is a vowel, adds way to it
if first_pos in vowels:
     translated = word + "way"     
### goes through each letter in the word searching for vowels, adds "ay" to it
else:
    position_let = 0
    for i in range(len(word)):
        if word[i] in vowels:
            posisition_let = i
            break
    translated = word[i:] + word[:i]+"ay"
###prints answer from if or the else loop
print("Pig latin:",translated)
