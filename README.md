### Day 13: Object-Oriented Programming (OOP) Basics – Classes, Objects, __init__ & Attributes

**Live Session Plan (9:30 - 10:30 PST / ~9:30 - 10:30 PM PKT/IST)**  
- **0-5 mins**: Welcome + recap Day 12 + shoutouts to homework (refactored contact books with packages, cricket stats packages).  
- **5-20 mins**: Why OOP? Introduction to classes and objects (real-world analogy).  
- **20-45 mins**: Defining classes, __init__, instance attributes, methods, creating objects.  
- **45-55 mins**: Live project: Convert Contact Book to OOP (Contact class + ContactManager class).  
- **55-60 mins**: Q&A, common mistakes, homework.


1. **Welcome & Recap**  
   - "Assalam-o-Alaikum everyone! Day 13 – Alhamdulillah we're almost two weeks in and your code is already looking professional!  
   - Yesterday modules and packages turned our messy scripts into clean, organized projects. Amazing folder structures, reusable storage/ui modules – this is exactly how real Python projects (Django, Flask, LangChain agents) are built!  
   - Today: We start Object-Oriented Programming (OOP). OOP is the foundation of almost all modern Python code – web frameworks, data science libraries, AI tools. It lets us model real-world entities (like a Contact, Player, AI Agent) naturally and write cleaner, more maintainable code."

2. **Why OOP? Real-World Analogy (10 mins)**  
   - Procedural code (what we’ve done so far): Good for small scripts, but data and functions are separate → hard to manage as project grows.  
   - OOP: Groups data + behavior together into "objects" – just like real life.

   - Think of a **Cricketer** in real life:
     - Properties (data): name, age, runs, average
     - Behaviors (actions): bat(), bowl(), field(), calculate_average()
   - In OOP, we create a blueprint (class) called `Cricketer`, then make actual players (objects) like babar = Cricketer("Babar Azam", 30)

   Benefits:
   - Reusability
   - Easier maintenance
   - Natural modeling
   - Used in Flask/Django models, LangChain agents, Pygame games, etc.

3. **Defining a Class & Creating Objects**  
   New folder: `day13_oop_basics`  
   File: `day13_classes.py`

   **Basic Class Syntax**
   ```python
   class Cricketer:        # class name – PascalCase
       pass                # empty class for now
   
   # Create objects (instances)
   player1 = Cricketer()
   player2 = Cricketer()
   
   print(player1)          # <__main__.Cricketer object at 0x...>
   print(player2)          # different memory address
   ```

   **Adding Attributes (Data)**
   ```python
   class Cricketer:
       pass
   
   babar = Cricketer()
   babar.name = "Babar Azam"      # instance attribute
   babar.age = 30
   babar.runs = 5000
   
   rizwan = Cricketer()
   rizwan.name = "Mohammad Rizwan"
   rizwan.age = 32
   rizwan.runs = 3000
   
   print(f"{babar.name} has {babar.runs} runs")
   ```

   Problem: We repeat this for every player → use `__init__`

   **The __init__ Method – Constructor**
   ```python
   class Cricketer:
       def __init__(self, name, age, runs=0):   # called automatically
           self.name = name         # instance attribute
           self.age = age
           self.runs = runs
           self.average = 0.0       # default
   
   # Create objects – much cleaner!
   babar = Cricketer("Babar Azam", 30, 5000)
   rizwan = Cricketer("Mohammad Rizwan", 32, 3000)
   
   print(babar.name, babar.runs)
   ```

   - `self`: Refers to the current object (required as first parameter)

4. **Adding Methods (Behaviors)**  
   ```python
   class Cricketer:
       def __init__(self, name, age, runs=0, matches=0):
           self.name = name
           self.age = age
           self.runs = runs
           self.matches = matches
   
       def display_info(self):                     # method
           print(f"Player: {self.name}")
           print(f"Age: {self.age}")
           print(f"Runs: {self.runs}")
           if self.matches > 0:
               avg = self.runs / self.matches
               print(f"Average: {avg:.2f}")
           else:
               print("Average: N/A")
       
       def add_runs(self, new_runs):               # modify data
           self.runs += new_runs
           self.matches += 1
           print(f"{self.name} scored {new_runs} runs!")
   
   # Usage
   shaheen = Cricketer("Shaheen Afridi", 25, matches=50)
   shaheen.display_info()
   
   shaheen.add_runs(5)        # wicket maiden or something :)
   shaheen.display_info()
   ```

   - Methods always take `self` as first parameter

5. **Live Project: OOP Contact Book**  
   Refactor our contact book using classes:

   **File: contact.py**
   ```python
   class Contact:
       def __init__(self, name, phone, email="N/A"):
           self.name = name.capitalize()
           self.phone = phone
           self.email = email
   
       def display(self):
           print(f"\n📇 {self.name}")
           print(f"   Phone: {self.phone}")
           print(f"   Email: {self.email}")
   
       def update_phone(self, new_phone):
           self.phone = new_phone
           print("✅ Phone updated!")
   
   
   class ContactManager:
       def __init__(self):
           self.contacts = {}    # name → Contact object
   
       def add_contact(self, name, phone, email="N/A"):
           if name in self.contacts:
               print("❌ Contact already exists!")
           else:
               self.contacts[name] = Contact(name, phone, email)
               print("✅ Contact added!")
       
       def view_all(self):
           if not self.contacts:
               print("No contacts yet!")
               return
           print(f"\n📋 Total Contacts: {len(self.contacts)}")
           for contact in self.contacts.values():
               contact.display()
       
       def search(self, name):
           name = name.capitalize()
           if name in self.contacts:
               self.contacts[name].display()
           else:
               print("❌ Not found!")
   ```

   **File: main.py**
   ```python
   from contact import ContactManager
   
   manager = ContactManager()
   
   manager.add_contact("Ali", "03001234567", "ali@example.com")
   manager.add_contact("Sara", "03331234567")
   
   manager.view_all()
   manager.search("ali")
   ```

#### Key OOP Terms Quick Summary (Show on Screen)
| Term              | Meaning                                      |
|-------------------|----------------------------------------------|
| Class             | Blueprint/template                                   |
| Object/Instance   | Actual created entity from class             |
| Attribute         | Data/variable inside object                  |
| Method            | Function inside class                        |
| self              | Reference to current object                  |
| __init__          | Constructor – runs on object creation        |

#### Common Mistakes
- Forgetting `self` as first parameter in methods.  
- Forgetting to use `self.` when accessing attributes inside class.  
- Creating attributes outside __init__ inconsistently.

#### Homework for Day 13
1. Run all examples – create Cricketer and Contact classes.
2. Convert your persistent Contact Book to full OOP:
   - Contact class (with attributes + methods like update, display).
   - ContactManager class (with add, delete, search, save/load using previous file handling).
   - Keep storage in separate module if you want extra credit.
3. Bonus Project: Create a `BankAccount` class:
   - Attributes: account_number, holder_name, balance
   - Methods: deposit(), withdraw(), check_balance(), transfer(to_account, amount)
   - Create multiple accounts and test transfers.
4. Comment “Day 13 Done ✅” with screenshot of your OOP Contact Book running (show at least 2 contacts).
5. (Advanced Bonus): Add a `Player` class for cricket with inheritance teaser (Batsman and Bowler classes coming soon).
