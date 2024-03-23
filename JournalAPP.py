menu="""
1, Add a new entry
2, View current entries
3, Exit
"""


welcome = "Welsome to the Journal App!"
print(welcome)

userInput=input(menu + "Enter your option:")
Entry = []

while userInput != 3:
  if userInput == "1":
    Entry.append(input("Enter your new entry:"))
    userInput=input(menu + "Enter your option:")
  elif userInput == "2":
    print(Entry)
    userInput=input(menu + "Enter your option:")
  elif userInput == "3":
    print("Exiting program.")
    break
  else:
    print("Wrong input!")
    userInput = input(menu + "Enter your option:")

