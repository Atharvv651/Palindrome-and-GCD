print("PALINDROME CHECKER")

word = input("Enter A Word: ")

reversed_word = ""

for letter in word:
    reversed_word = reversed_word + word[-(word.index(letter)+1)] 

if reversed_word == word:
    print("This is a palindrome")
else:
    print("This is not palindrome")