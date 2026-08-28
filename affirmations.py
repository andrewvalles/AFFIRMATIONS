import os
import random

#opening affirmation
def open_affirmation(affirmations):
  affirmations = open('affirmations.txt', 'r')
  for line in affirmtaion:
    affirmations = affirmations.readline())
  return affirmations

#AFFIRMATION
def picking_affirmation(affirmations):
  affirmation = affirmations.readline()
  picked_affimation = random.choice(affirmation)
  return picked_affirmation

#EDIT LIST
def edit_list_func(affirmations):
  edit_affirmation = input("Would you like to (A)dd/(D)elete Affirmation List?: ").upper()
  affirmation = open('affirmation.txt', 'a')
  if edit_affirmation == 'A':
    new_phrase = input()
    print("Please enter affirmation: ")
    affirmation.write(new_phrase)
    print(affirmations.txt())
    print('UPDATED!')
    affirmation = close()
  else:
    print("ERROR EDIT_FUNC")
  return


while True:
  print("Here is your daily affirmation: ")
  open_affirmation(affirmations)
  print(picking_affirmation(affirmations))

  edit_list = input("Would you like to (E)dit the affirmations list?").upper()
  if "E" == edit_list or 'e' == edit_list:
    edit_list_func(affirmations)
  else:
    print("ERROR MAIN FUNC")
