### Day 11: File Handling in Python – Reading, Writing & Persistent Data (Save Your Agent’s Memory!)

**Live Session Plan (9:30 - 10:30 PST / ~9:30 - 10:30 PM PKT/IST)**  
- **0-5 mins**: Welcome + recap Day 10 + shoutouts to homework (robust contact books with error handling, lambda sorting, recursion).  
- **5-25 mins**: Opening files, reading (read(), readline(), readlines()), writing (write(), writelines()).  
- **25-45 mins**: Best practices with `with` statement, modes, CSV & JSON handling.  
- **45-55 mins**: Live project: Make Contact Book save/load to file permanently.  
- **55-60 mins**: Q&A, common issues, homework.

#### Detailed Session Script / Talking Points

1. **Welcome & Recap**  
   - "Assalam-o-Alaikum everyone! Day 11 – we're now building apps that remember data even after closing!  
   - Yesterday we made our code bulletproof with lambda, recursion, docstrings, and error handling. Incredible work on robust contact books that don’t crash on bad input – this is production-level quality!  
   - Today: File Handling – the bridge between your program and permanent storage. Without files, every time you close your contact book or agent, all data is lost. With files, your agents can save progress, load previous state, store scraped data, logs, and more."

2. **Basic File Operations – Open, Read, Write, Close**  
   New file: `day11_file_handling.py`  
   Create a folder `data` in your project for files.

   - **Writing to a File**
     ```python
     # 'w' = write mode (overwrites if exists)
     file = open("data/greeting.txt", "w")
     file.write("Hello from Day 11!\n")
     file.write("This line is added second.\n")
     file.close()   # ALWAYS close!
     ```

   - **Appending to a File**
     ```python
     file = open("data/greeting.txt", "a")  # 'a' = append
     file.write("This is appended later.\n")
     file.close()
     ```

   - **Reading from a File**
     ```python
     # 'r' = read mode (default)
     file = open("data/greeting.txt", "r")
     
     # Method 1: read all
     content = file.read()
     print(content)
     
     file.close()
     
     # Method 2: readline() – one line at a time
     file = open("data/greeting.txt", "r")
     line1 = file.readline().strip()
     line2 = file.readline().strip()
     print("First line:", line1)
     file.close()
     
     # Method 3: readlines() – list of lines
     file = open("data/greeting.txt", "r")
     lines = file.readlines()
     for i, line in enumerate(lines, 1):
         print(f"Line {i}: {line.strip()}")
     file.close()
     ```

   - **Common Modes Cheat Sheet** (show on screen)
     | Mode | Meaning                          | 
     |------|----------------------------------|
     | r    | Read (default)                   |
     | w    | Write (overwrite)                |
     | a    | Append                           |
     | r+   | Read + Write                     |
     | x    | Create new only (error if exists)|

3. **Best Practice: Using `with` Statement**  
   - Automatically closes file – no need to remember `close()`
     ```python
     with open("data/greeting.txt", "r") as file:
         content = file.read()
         print(content)
     # file automatically closed here even if error!
     
     # Writing with with
     with open("data/motivation.txt", "w") as f:
         f.write("Keep going – Day 100 is coming!\n")
         f.write("You’re building real AI agents.\n")
     ```

4. **Working with CSV Files – Tabular Data**  
   - Use built-in `csv` module (no install needed)
     ```python
     import csv
     
     # Writing CSV
     contacts_data = [
         ["Name", "Phone", "Email"],
         ["Ali", "03001234567", "ali@example.com"],
         ["Sara", "03331234567", "sara@example.com"]
     ]
     
     with open("data/contacts.csv", "w", newline="") as file:
         writer = csv.writer(file)
         writer.writerow(["Name", "Phone", "Email"])      # header
         writer.writerows(contacts_data[1:])               # data
     
     # Reading CSV
     with open("data/contacts.csv", "r") as file:
         reader = csv.reader(file)
         for row in reader:
             print(row)   # each row is a list
     
     # Better: DictReader for named columns
     with open("data/contacts.csv", "r") as file:
         reader = csv.DictReader(file)
         for row in reader:
             print(f"{row['Name']}: {row['Phone']}")
     ```

5. **Working with JSON Files – Perfect for Nested Data**  
   - JSON is the standard for APIs and saving complex Python objects (dicts, lists)
     ```python
     import json
     
     # Python dict to JSON file
     my_agent_memory = {
         "user_name": "Ahmed",
         "goals": ["Learn Python", "Build AI Agent", "Automate Upwork bids"],
         "progress": {"day": 11, "completed": True}
     }
     
     with open("data/agent_memory.json", "w") as file:
         json.dump(my_agent_memory, file, indent=4)   # indent for readable
     
     # Load JSON back to Python
     with open("data/agent_memory.json", "r") as file:
         loaded = json.load(file)
         print(loaded["goals"][1])   # Build AI Agent
     ```

6. **Persistent Contact Book (Save/Load from JSON)**  
   Upgrade our contact book so data survives restart:

   ```python
   import json
   import os
   
   FILE_PATH = "data/contacts.json"
   
   def load_contacts():
       if os.path.exists(FILE_PATH):
           with open(FILE_PATH, "r") as file:
               return json.load(file)
       else:
           return {}   # empty if no file
   
   def save_contacts(contacts):
       with open(FILE_PATH, "w") as file:
           json.dump(contacts, file, indent=4)
       print("✅ Contacts saved permanently!")
   
   # Main program
   contacts = load_contacts()
   print(f"Loaded {len(contacts)} existing contacts.\n")
   
   # Add one for demo
   contacts["Waseem"] = {"phone": "03009876543", "email": "waseem@example.com"}
   save_contacts(contacts)
   
   # Show all
   print("Current contacts:")
   for name, info in contacts.items():
       print(f"   {name}: {info['phone']}")
   ```

#### Common Issues & Fixes
- `FileNotFoundError` → check path, use `os.path.exists()`.
- Encoding issues (rare on modern Python) → add `encoding="utf-8"`.
- Forgetting `newline=""` in CSV on Windows → extra blank lines.
- Always use `with` to avoid file leaks.

#### Homework for Day 11
1. Run all examples – create greeting.txt, contacts.csv, agent_memory.json.
2. Upgrade your Contact Book to be fully persistent:
   - Load contacts from JSON at start.
   - Save automatically after every add/update/delete.
   - Use proper error handling if file missing/corrupted.
3. Bonus Project: Create a "Daily Journal Agent":
   - Save date + user’s goals/progress to JSON.
   - Load previous entries and show history.
4. Comment “Day 11 Done ✅” with screenshot showing contacts loaded from file after restart.
5. (Advanced Bonus): Add export to CSV option in your contact book.
