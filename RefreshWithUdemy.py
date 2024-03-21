
#Function

def greeting(name, surname):
  print(f"Hello, {name} {surname}!")

greeting("Bob", "Potter")
greeting(surname = "Potter", name="Bob")


'''
#dictionary
friend_ages = {
  "Rolf":24,
  "Adam": 30,
  "Anne": 27
}

for friend_name, friend_age in friend_ages.items():
  print(f"{friend_name}'s age is {friend_age}.")

#print(friend_ages["Adam"])
friend_ages["Anne"] = 21
#print(friend_ages)
print(sum(friend_ages.values()))
print(sum(friend_ages.values())/len(friend_ages))
'''

'''
#using for loop to calculate average number of a list
grades = [35, 67, 88, 93, 100, 45]
total = 0
amount = len(grades)

for grade in grades:
  total += grade
  #print(total)

#total = sum(grades)
average_grade = total/amount
print(f"The average score is {average_grade}")

'''


'''
#while loop
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
'''
