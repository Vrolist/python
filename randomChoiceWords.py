#_author_ = hus
import random

WORDS = ("python","jump","easy","answer")

word = random.choice(WORDS)

corrent = word

jumble = ""
#随机生成一个小于word长度的数，取出这个单词中对应数字的字母，添加到jumble中
#在word删除该字母
#重复上述步骤，直到word中没有字母了
#对比jumble和corrent
#while循环，直到猜对
while word:
    
    position = random.randrange(len(word))

    jumble += word[position]

    word = word[:position] + word[(position + 1):]

    

print(jumble)

guess = input("\nYour guess: ")
while True:
    if guess == "" :
        print("sorry, please enter one word:")
        guess = input("Your guess: ")
    elif guess != corrent:
        print("sorry, that's not it")
        guess = input("Your guess: ")
    else:
        print("Wooo, You Success~")
        break


print("\nThank You~")
