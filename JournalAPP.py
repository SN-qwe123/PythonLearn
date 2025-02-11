from database import entries, add_entry, view_entries

menu="""
1, Add a new entry
2, View current entries
3, Exit
"""
print(entries)
welcome = "Welcome to the Journal App!"
print(welcome)

userInput=input(menu + "Enter your option:")



while userInput != 3:
  if userInput == "1":
    #collect content and date then store into database
    entry_content = input("What have you learnt today?")
    entry_date = input("Input today's date:")
    add_entry( entry_content, entry_date)

    userInput=input(menu + "Enter your option:")
  elif userInput == "2":
    #retrieve entries from the database
    entries = view_entries()

    #display entries
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")

    userInput=input(menu + "Enter your option:")
  elif userInput == "3":
    print("Exiting program.")
    break
  else:
    print("Wrong input!")
    userInput = input(menu + "Enter your option:")

    #test

