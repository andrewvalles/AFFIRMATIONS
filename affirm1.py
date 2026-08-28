#Verision 1 of Daily Affirmation Script
#This version opens up the affirmation.txt, picks one, and then prints the randomly picked one. 




#opens and returns affirmation list
def open_affirmation():
  affirmations_file = open('affirmations.txt', 'r')
  affirmations = []
  for line in affirmations_file:
    clean_line =  line.strip()
    affirmations.append(clean_line)
  print(affirmations)
  return affirmations

#exits program
def exit_affirmation():
  choice = input('Would you like to e(X)it: ').upper()
  if choice == 'E' or choice == 'X':
    exit = False
    return exit
  else:
    return print("ERROR")

exit = True


#main loop
while exit:
  affirmations = open_affirmation()
#  pick_affirmation(affirmations)
  exit = exit_affirmation()

