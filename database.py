entries = [{"content": "sss", "date": "sssssss"}]

def add_entry(entry_content, entry_date):

    entries.append({"content": entry_content, "date": entry_date})

def view_entries():
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")
