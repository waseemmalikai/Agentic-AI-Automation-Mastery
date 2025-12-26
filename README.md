### Day 8: Dictionaries in Python – The Most Powerful Data Structure (Key-Value Magic)

**Live Session Plan (9:30 - 10:30 PST / ~9:30 - 10:30 PM PKT/IST)**  
- **0-5 mins**: Welcome + recap Day 7 + shoutouts to homework (cricket team managers, Fibonacci with comprehensions).  
- **5-25 mins**: Introduction to Dictionaries – creation, access, modification.  
- **25-45 mins**: Dictionary methods, looping, nesting + real-world examples.  
- **45-55 mins**: Live mini project: Personal Contact Book / Phone Directory.  
- **55-60 mins**: Q&A, common mistakes, homework.

1. **Welcome & Recap (5 mins)**  
   - "Assalam-o-Alaikum  everyone! Day 8 – we're powering through and getting closer to real automation every day!  
   - Yesterday we mastered list comprehensions, tuples, and sets. Amazing cricket team managers with unique skills and player records – you're already handling complex data like pros!  
   - Today: We meet the KING of Python data structures – Dictionaries! Almost every real-world program (APIs, databases, agent memory, config files, ML datasets) uses dictionaries. Once you learn dicts, you'll feel unstoppable."

2. **What is a Dictionary?**  
   New file: `day8_dictionaries.py`

   - "A dictionary stores data as key-value pairs. Like a real dictionary: word (key) → meaning (value)."  
   - Analogy: Phone contacts – Name (key) → Number (value)

   Creation:
   ```python
   # Empty dict
   empty_dict = {}
   # or
   empty_dict = dict()
   
   # With data
   student = {
       "name": "Ahmed Khan",
       "age": 20,
       "city": "Lahore",
       "grade": "A"
   }
   
   contact = {"Ali": "03001234567", "Sara": "03331234567"}
   
   print(student)
   print(type(student))    # <class 'dict'>
   ```

   - Keys: Usually strings or numbers (must be immutable & unique)  
   - Values: Anything – strings, numbers, lists, even other dicts!

3. **Accessing, Modifying & Adding Items (10 mins)**  
   ```python
   print(student["name"])      # "Ahmed Khan"
   print(student.get("age"))   # 20  (safer – returns None if key missing)
   
   # Modify
   student["age"] = 21
   student["grade"] = "A+"
   
   # Add new
   student["university"] = "NUST"
   
   # Delete
   del student["city"]
   # or
   popped = student.pop("grade")
   print(popped)               # "A+"
   
   print(student)
   ```

   - `.get()` advantage:  
     ```python
     print(student.get("email", "Not available"))  # safe default
     ```

4. **Dictionary Methods – Must Know (15 mins)**  
   Show cheat sheet on screen:

   | Method              | What it does                              | Example                              |
   |---------------------|-------------------------------------------|--------------------------------------|
   | keys()              | Returns all keys                          | student.keys()                       |
   | values()            | Returns all values                        | student.values()                     |
   | items()             | Returns (key, value) pairs                | student.items()                      |
   | update()            | Merge another dict                        | student.update({"email": "a@example.com"}) |
   | clear()             | Empty the dict                            | student.clear()                      |
   | len()               | Number of items                           | len(student)                         |
   | in                  | Check if key exists                       | "name" in student                    |

   Looping through dictionaries:
   ```python
   # Keys (default)
   for key in student:
       print(key)
   
   # Keys explicitly
   for key in student.keys():
       print(key, "→", student[key])
   
   # Values
   for value in student.values():
       print(value)
   
   # Key-Value pairs (most useful!)
   for key, value in student.items():
       print(f"{key.capitalize()}: {value}")
   ```

   Real example: Cricketer stats
   ```python
   babar = {
       "runs": 5000,
       "average": 55.5,
       "centuries": 15,
       "fifties": 30,
       "team": "Pakistan"
   }
   
   print(f"Babar Azam has {babar['centuries']} ODI centuries!")
   ```

5. **Nested Dictionaries – Real Power (5 mins)**  
   ```python
   class_room = {
       "student1": {"name": "Ali", "age": 18, "marks": [85, 90, 88]},
       "student2": {"name": "Fatima", "age": 19, "marks": [92, 95, 91]},
   }
   
   print(class_room["student1"]["marks"][1])   # 90
   ```

6. **Smart Contact Book / Phone Directory**  
   ```python
   print("📱 Smart Contact Book Manager\n")
   
   contacts = {}   # name → details dict
   
   while True:
       print("\nOptions: 1=Add, 2=Search, 3=Update, 4=Delete, 5=View All, 6=Exit")
       choice = input("Choose: ").strip()
       
       if choice == "1":
           name = input("Enter name: ").strip().capitalize()
           if name in contacts:
               print("Already exists! Use update.")
           else:
               phone = input("Phone number: ").strip()
               email = input("Email (optional): ").strip()
               contacts[name] = {"phone": phone, "email": email or "N/A"}
               print(f"✅ {name} added!")
       
       elif choice == "2":
           name = input("Search name: ").strip().capitalize()
           if name in contacts:
               info = contacts[name]
               print(f"\n📇 {name}")
               print(f"   Phone: {info['phone']}")
               print(f"   Email: {info['email']}")
           else:
               print("❌ Not found!")
       
       elif choice == "3":
           name = input("Enter name to update: ").strip().capitalize()
           if name in contacts:
               phone = input(f"New phone (current: {contacts[name]['phone']}): ").strip()
               email = input(f"New email (current: {contacts[name]['email']}): ").strip()
               if phone:
                   contacts[name]["phone"] = phone
               if email:
                   contacts[name]["email"] = email
               print("✅ Updated!")
           else:
               print("Not found!")
       
       elif choice == "4":
           name = input("Delete name: ").strip().capitalize()
           if name in contacts:
               del contacts[name]
               print("🗑️ Deleted!")
           else:
               print("Not found!")
       
       elif choice == "5":
           if contacts:
               print("\n📋 All Contacts:")
               for name, info in contacts.items():
                   print(f"   {name}: {info['phone']} ({info['email']})")
           else:
               print("No contacts yet!")
       
       elif choice == "6":
           print("Thanks for using your Smart Contact Book!")
           break
       
       else:
           print("Invalid choice!")
   ```
#### Common Mistakes
- Forgetting quotes around string keys.  
- Trying to access missing key without `.get()`.  
- Using `==` instead of `in` to check key existence.

#### Homework for Day 8
1. Run all examples.
2. Build an enhanced Contact Book:
   - Add address field.
   - Add search by phone number (reverse lookup).
   - Show total contacts count.
   - Add option to export to simple text format (we’ll improve with files later).
3. Alternative: Create a "Cricket Player Database" with multiple players (nested dict) and show stats summary.
4. Comment “Day 8 Done ✅” with screenshot of your contact book (at least 3 contacts + one search).
5. (Bonus): Count frequency of letters in a sentence using dictionary (word/letter counter).
