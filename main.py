import random
from art import stages
from word import word_list
from art import logo

print(logo)

word = random.choice(word_list)
word_length=len(word)
lives=6
list=[]
for _ in range(word_length):
  list +="_"
print(list)
end_of_game=False
while not end_of_game:
  guess_word = input("\n Guess a letter of the word: ").lower()
  for position in range(word_length):
    letter=word[position]
    if(list[position]==guess_word):
      print("Word already in the list !")
    if(letter==guess_word):
      list[position]=guess_word
  print(list)
  if guess_word not in word:
    lives-=1
    print(stages[lives])
    if lives==0:
      end_of_game=True
      print("You LOSE...\n GAME OVER!!!!!")
      print(f"The word was {word}")
  if "_" not in list:
    end_of_game = True
    print("You WIN..\n GAME OVER!!!!!")
