#_author_ = hus
import random

WORDS = ("python","jump","easy","answer")

word = random.choice(WORDS)

corrent = word

jumble = ""
while word:
    
    position = random.randrange(len(word))

    jumble += word[position]

    word = word[:position] + word[(position + 1):]

    

print(jumble)

guess = raw_input("\nYour guess: ")
while True:
    if guess == "" :
        print("sorry, please enter one word:")
        guess = raw_input("Your guess: ")
    elif guess != corrent:
        print("sorry, that's not it")
        guess = raw_input("Your guess: ")
    else:
        print("Wooo, You Success~")
        break


print("\nThank You~")
