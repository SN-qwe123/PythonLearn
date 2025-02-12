from database import entries, add_entry, get_entries

def prompt_new_entry():
  entry_content = input("What have you learnt today?")
  entry_date = input("Input today's date:")
  add_entry(entry_content, entry_date)

def view_entries(entries):
  for entry in entries:
    print(f"{entry['date']}\n{entry['content']}\n\n")

menu="""
1, Add a new entry
2, View current entries
3, Exit
"""
welcome = "Welcome to the Journal App!"
print(welcome)

userInput=input(menu + "Enter your option:")



while userInput != 3:
  if userInput == "1":
    prompt_new_entry() #collect content and date then store into database
    userInput=input(menu + "Enter your option:")
  elif userInput == "2":
    view_entries(get_entries()) #retrieve entries from the database. display entries
    userInput=input(menu + "Enter your option:")
  elif userInput == "3":
    print("Exiting program.")
    break
  else:
    print("Wrong input!")
    userInput = input(menu + "Enter your option:")


