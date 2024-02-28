number = 7

while True:
  user_input = input("Would you like to play? (Y/N)").lower()
  if user_input == "n":
    break
    
  user_num = int(input("Guess our number: "))
  if user_num == number:
    print("You guessed correctly!")
  elif abs(number - user_num) == 1:
    print("You were off by 1.")
  else:
    print("Sorry, it's wrong!")

