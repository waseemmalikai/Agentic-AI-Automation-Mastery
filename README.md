### Day 16: Advanced OOP – Abstract Classes, @property, Dataclasses & Intro to Design Patterns

**Live Session Plan (9:30 - 10:30 PST / ~9:30 - 10:30 PM PKT/IST)**  
- **0-5 mins**: Welcome + recap Day 15 + shoutouts to homework (cricket team hierarchies, captains, bank inheritance).  
- **5-25 mins**: Abstract Base Classes (ABC) – forcing implementation in subclasses.  
- **25-40 mins**: @property decorator – getters/setters the Pythonic way + dataclasses for boilerplate reduction.  
- **40-55 mins**: Intro to Design Patterns – Singleton & Factory with practical examples.  
- **55-60 mins**: Q&A, when to use what, homework.


1. **Welcome & Recap**  
   - "Assalam-o-Alaikum everyone! Day 16 – we’re deep into professional Python territory now!  
   - Yesterday inheritance and polymorphism made our code incredibly reusable. Amazing cricket team systems with Batsmen, Bowlers, All-Rounders, captains, training sessions – you’re building real object hierarchies!  
   - Today: Advanced OOP tools that make code even cleaner, safer, and more maintainable. We’ll cover Abstract Classes (to enforce design), @property (for smart attributes), dataclasses (less boilerplate), and introduce Design Patterns – reusable solutions used in every major framework."

2. **Abstract Base Classes (ABC) – Enforcing Contracts**  
   New folder: `day16_advanced_oop_patterns`  
   File: `day16_abstract_dataclass.py`

   - Purpose: Define methods that MUST be implemented in subclasses (like an interface).

   ```python
   from abc import ABC, abstractmethod
   
   class Player(ABC):                              # Abstract base class
       def __init__(self, name, age):
           self.name = name.capitalize()
           self.age = age
       
       def display_info(self):
           print(f"{self.name}, Age: {self.age}")
       
       @abstractmethod                             # MUST be implemented by child
       def perform_role(self):
           pass                                     # no implementation here
   
       @abstractmethod
       def train(self):
           pass
   
   
   # This will cause error if instantiated directly
   # p = Player("test", 20)   # TypeError
   
   class Batsman(Player):
       def __init__(self, name, age, runs=0):
           super().__init__(name, age)
           self.runs = runs
       
       def perform_role(self):                     # Must implement
           print(f"{self.name} is batting elegantly!")
       
       def train(self):                            # Must implement
           print(f"{self.name} is practicing cover drives.")
       
       def display_info(self):
           super().display_info()
           print(f"Runs: {self.runs}")
   
   
   babar = Batsman("babar azam", 30, 5000)
   babar.display_info()
   babar.perform_role()
   babar.train()
   ```

   - If child forgets to implement abstract method → TypeError at class definition time.  
   - Great for ensuring all players have `perform_role()`.

3. **@property Decorator – Pythonic Getters/Setters + Validation**  

   ```python
   class BankAccount:
       def __init__(self, holder, balance=0):
           self.holder = holder
           self._balance = balance               # protected
   
       @property                                    # getter
       def balance(self):
           print("Balance accessed")
           return self._balance
       
       @balance.setter                              # setter
       def balance(self, amount):
           if amount < 0:
               raise ValueError("Balance cannot be negative!")
           print("Balance updated")
           self._balance = amount
       
       @balance.deleter
       def balance(self):
           print("Balance deleted – account closed")
           del self._balance
   
   
   acc = BankAccount("Ahmed", 5000)
   print(acc.balance)           # uses getter – Balance accessed → 5000
   acc.balance = 10000          # uses setter
   # acc.balance = -500         # ValueError
   ```

   - Feels like accessing attribute, but runs code (validation, logging).  
   - Also @property for read-only.

4. **Dataclasses – Less Boilerplate for Data-Heavy Classes (8 mins)**  

   ```python
   from dataclasses import dataclass
   
   @dataclass
   class Contact:
       name: str
       phone: str
       email: str = "N/A"                       # default value
       
       def __post_init__(self):                 # optional custom logic
           self.name = self.name.capitalize()
   
   # Auto-generates __init__, __repr__, __eq__, etc.
   c1 = Contact("ali", "03001234567", "ali@example.com")
   c2 = Contact("sara", "03331234567")
   
   print(c1)                    # Contact(name='Ali', phone='03001234567', email='ali@example.com')
   print(c1 == Contact("ali", "03001234567", "ali@example.com"))  # True
   ```

   - Perfect for models (contacts, players, API responses).  
   - Add methods normally.

5. **Design Patterns Intro – Singleton & Factory**  

   **Singleton Pattern** – Only one instance ever exists (e.g., database connection, config)

   ```python
   class DatabaseConnection:
       _instance = None                        # class variable
       
       def __new__(cls):                       # controls instance creation
           if cls._instance is None:
               print("Creating single DB connection...")
               cls._instance = super().__new__(cls)
           return cls._instance
       
       def __init__(self):
           # Init runs every time, but we protect
           if not hasattr(self, "initialized"):
               self.initialized = True
               self.connection = "Connected to Agent DB"
       
       def query(self, q):
           print(f"Executing: {q}")
   
   
   db1 = DatabaseConnection()
   db2 = DatabaseConnection()
   
   print(db1 is db2)            # True – same object!
   db1.query("SELECT * FROM agents")
   ```

   **Factory Pattern** – Create objects without specifying exact class

   ```python
   class PlayerFactory:
       @staticmethod
       def create_player(player_type, name, age, **kwargs):
           if player_type.lower() == "batsman":
               return Batsman(name, age, kwargs.get("runs", 0))
           elif player_type.lower() == "bowler":
               return Bowler(name, age, kwargs.get("wickets", 0))
           elif player_type.lower() == "allrounder":
               return AllRounder(name, age, 
                                kwargs.get("runs", 0), 
                                kwargs.get("wickets", 0))
           else:
               raise ValueError("Unknown player type")
   
   
   # Usage – no need to import specific classes
   player = PlayerFactory.create_player("batsman", "rizwan", 32, runs=3000)
   player.display_info()
   player.perform_role()
   ```

#### When to Use What
- ABC → when you want to force implementation (interfaces).  
- @property → when you need validation/logic on attribute access.  
- Dataclass → for simple data containers (90% of models).  
- Singleton → for global resources (DB, logger, config).  
- Factory → when object creation logic is complex or user chooses type.

#### Homework for Day 16
1. Run all examples – play with abstract classes, @property, dataclasses.
2. Upgrade your Cricket Team system:
   - Make Player abstract with @abstractmethod for perform_role() and train().
   - Use dataclass for a lightweight Stats class.
   - Add @property for calculated fields like batting_average (runs/matches).
   - Implement Singleton for TeamManager (only one team instance).
   - Add PlayerFactory to create players from string input (e.g., "batsman,Babar,30,5000").
3. Bonus Project: Create a simple ATM system:
   - Use singleton for ATM machine.
   - Dataclass for Transaction.
   - @property for balance with validation.
4. Comment “Day 16 Done ✅” with screenshot showing factory creation or singleton proof (id() same).
5. (Advanced Bonus): Implement a Logger singleton that writes to file.
