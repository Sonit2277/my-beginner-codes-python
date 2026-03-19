from datetime import datetime

def add_entry():
    """
    Captures a new text entry from the user and archives it 
    with a persistent, sortable timestamp.
    """
    entry = input("Enter your diary entry: ")
    
    # Generate timestamp in Year-Month-Day Hour:Minute format for chronological clarity
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Open in 'append' mode to ensure new entries are added to the end of the file 
    # without over-writing previous history.
    with open("diary.txt", "a") as f:
        f.write(f"[{timestamp}] {entry}\n")

def view_entries():
    """
    Retrieves and displays the full history of archived entries from the local text file.
    """
    try:
        # Open in 'read' mode to output the entire log to the console
        with open("diary.txt", "r") as f:
            content = f.read()
            print("\n--- Past Entries ---")
            print(content if content else "No entries found.")
            print("--------------------\n")
    except FileNotFoundError:
        print("\n[System] No diary file found yet. Create an entry first!\n")

# --- Main Application Loop ---
# This serves as the User Interface (UI) controller for the program
while True:
    print("1. Add Entry  2. View All  3. Quit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        add_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        print("Closing diary. Goodbye!")
        break
    else:
        # Fallback for handling unexpected user input
        print("Invalid choice. Please select 1, 2, or 3.")