#Step 5

import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
wordlist=list(chosen_word)
word_as_list=list(chosen_word)
length_word=len(word_as_list)
for i in range (0, length_word):
  word_as_list[i]='_'
print(word_as_list)

end_of_game = False
stage=7
guess_list=[]
while(stage>0):
  #Check guessed letter
  while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if(guess in guess_list):
      print("You have already guessed this word. Choose again.")
    else:
      guess_list.append(guess)
      for i in range (0, length_word):
        if wordlist[i] == guess:
          word_as_list[i]=guess
      print(''.join(word_as_list))
      if "_" not in word_as_list:
        end_of_game = True
        print("You win.")
        stage=0
      if(guess not in wordlist):
        print(f"The character {guess} you chose is not in the word. You lose a life.")
        print(stages[stage-1])
        stage=stage-1
        if(stage==0):
          print("You lost.")
          print(f"Word is {chosen_word}")
          end_of_game = True

print("Game over.")
