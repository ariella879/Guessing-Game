from random import randint 

def choose_random_number():
  return randint(0,20)
  

def take_input(number):
  player_input = int(input("Guess a number between 0 and 20 "))
  if player_input > number:
    print("Try again: Your guess is too high!")
  elif player_input < number:
    print("Try again: Your guess is too low")
  elif player_input == number:
    print("You guessed it!")
  return player_input

def did_the_player_guess_right(the_correct_number, player_number):
  if player_number == the_correct_number:
    return False
  else:
    return True


Computer_Number_Chosen = choose_random_number()
print(Computer_Number_Chosen)

while True:
  player_number = take_input(Computer_Number_Chosen)
  while did_the_player_guess_right(Computer_Number_Chosen,player_number):
    take_input(Computer_Number_Chosen)
    player_number = take_input(Computer_Number_Chosen)
  break
