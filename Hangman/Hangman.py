from pickle import FALSE, TRUE
import random
import re
fname = input("Enter a file name: ")
fhand = open(fname)
wordList = list()
for word in fhand:
    wordList.append(word)

word_to_find = random.choice(wordList)
if word_to_find.isalnum() == FALSE:
    while word_to_find.isalnum() == FALSE:
        word_to_find = random.choice(wordList)
print(word_to_find)

space = len(word_to_find) - 1
underscore = ('_' * space)
print(underscore)
lives = 5
word = list()
won = FALSE
for char in range(0, space):
    word.append('_')
while lives != 0 and won == FALSE:
    guess = input('Input your guess: ')
    if(guess == "quit()"):
        break
    if guess in word_to_find and len(guess) == 1:
        print("Guess found!")
        index_list = [m.start() for m in re.finditer(guess, word_to_find)]
        for i in index_list:
            word[i] = guess
    elif guess in word_to_find and len(guess) == len(word_to_find) - 1:
        print("Guess found!")
        won = TRUE
    else:
        print("Guess not found")
        lives = lives - 1
    for char in range(0, space):
        won = TRUE
        if word[char] == "_":
            won = FALSE
    if won == FALSE:
        for char in range(len(word)):
            print(word[char], end=" ")
    if won == TRUE:
        print(word_to_find)
        print("You won! Congratulations")
    if lives == 0:
        print("You lost! Loser!")