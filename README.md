### Day 15: Inheritance & Polymorphism – Building Hierarchies and Reusable OOP Code

**Live Session Plan (9:30 - 10:30 PST / ~9:30 - 10:30 PM PKT/IST)**  
- **0-5 mins**: Welcome + recap Day 14 + shoutouts to homework (enhanced contact books with validation, class counters, beautiful __str__, bank accounts).  
- **5-25 mins**: Inheritance basics – single inheritance, super(), method overriding.  
- **25-45 mins**: Multiple inheritance, polymorphism, isinstance()/issubclass().  
- **45-55 mins**: Live project: Build a Cricket Team hierarchy (Player → Batsman/Bowler/AllRounder).  
- **55-60 mins**: Q&A, design tips, homework, teaser for Day 16.

1. **Welcome & Recap**  
   - "Assalam-o-Alaikum everyone! Day 15 – two weeks completed, mashAllah! Your OOP code is now professional grade.  
   - Yesterday we polished our classes with class variables, different method types, encapsulation, and special methods. Stunning contact books with validation, nice printing, total counters – and bank accounts that feel real!  
   - Today: Inheritance and Polymorphism – the most powerful features of OOP. Inheritance lets us build hierarchies (like real life: Player → Batsman), avoid code duplication, and make code super reusable. This is heavily used in frameworks like Django models, LangChain agents, and game development."

2. **Inheritance Basics – “is-a” Relationship (15 mins)**  
   New folder: `day15_inheritance_polymorphism`  
   File: `day15_inheritance.py`

   - Concept: Child class (subclass) inherits attributes and methods from parent class (superclass).

   ```python
   class Player:                                   # Parent/Base class
       def __init__(self, name, age):
           self.name = name.capitalize()
           self.age = age
       
       def display_info(self):
           print(f"Player: {self.name}, Age: {self.age}")
       
       def train(self):
           print(f"{self.name} is training hard!")
   
   
   class Batsman(Player):                          # Inherits from Player
       def __init__(self, name, age, runs=0, centuries=0):
           super().__init__(name, age)             # Call parent __init__
           self.runs = runs
           self.centuries = centuries
       
       def score_runs(self, runs):
           self.runs += runs
           if runs >= 100:
               self.centuries += 1
           print(f"{self.name} scored {runs} runs!")
       
       def display_info(self):                         # Override
           super().display_info()                      # Call parent version
           print(f"Runs: {self.runs}, Centuries: {self.centuries}")
   
   
   # Usage
   babar = Batsman("babar azam", 30, 5000, 15)
   babar.display_info()
   babar.train()                   # inherited method
   babar.score_runs(150)
   babar.display_info()
   ```

   Key points:
   - `super().__init__()` to initialize parent
   - Method overriding: Child provides its own version
   - Child can still call parent method with `super()`

3. **More Inheritance Examples + Bowler Class (10 mins)**  

   ```python
   class Bowler(Player):
       def __init__(self, name, age, wickets=0):
           super().__init__(name, age)
           self.wickets = wickets
       
       def take_wicket(self):
           self.wickets += 1
           print(f"{self.name} took a wicket! Total: {self.wickets}")
       
       def display_info(self):
           super().display_info()
           print(f"Wickets: {self.wickets}")
   
   
   shaheen = Bowler("shaheen afridi", 25, 200)
   shaheen.display_info()
   shaheen.take_wicket()
   shaheen.train()                 # inherited
   ```

4. **All-Rounder – Multiple Inheritance**  
   - Python supports multiple inheritance (carefully!)

   ```python
   class AllRounder(Batsman, Bowler):               # Inherits from both!
       def __init__(self, name, age, runs=0, centuries=0, wickets=0):
           Batsman.__init__(self, name, age, runs, centuries)
           Bowler.__init__(self, name, age, wickets)
           # Note: We called both parents explicitly
       
       def display_info(self):
           Batsman.display_info(self)              # or super() if MRO allows
           Bowler.display_info(self)               # show both stats
   
   
   shadab = AllRounder("shadab khan", 27, 2000, 2, 100)
   shadab.display_info()
   shadab.score_runs(80)
   shadab.take_wicket()
   shadab.train()
   ```

   Mention Method Resolution Order (MRO): `AllRounder.mro()` to see order.

5. **Polymorphism – “Many Forms”**  
   - Same method name works differently based on object type

   ```python
   def player_summary(player):                     # works for any Player subclass
       player.display_info()                       # polymorphic call
   
   players = [
       Batsman("rizwan", 32, 3000, 5),
       Bowler("haris rauf", 28, 150),
       AllRounder("imad wasim", 35, 1500, 1, 80)
   ]
   
   for p in players:
       player_summary(p)                           # same function, different output!
       p.train()                                   # all can train
   ```

   - Built-in checks:
     ```python
     print(isinstance(babar, Batsman))      # True
     print(isinstance(babar, Player))       # True (inheritance chain)
     print(issubclass(Batsman, Player))     # True
     ```

6. **Live Project: Cricket Team Management System**  
   Bring it all together:

   ```python
   class CricketTeam:
       def __init__(self, name):
           self.name = name
           self.players = []                       # list of Player objects
       
       def add_player(self, player):
           self.players.append(player)
           print(f"{player.name} added to {self.name}")
       
       def team_summary(self):
           print(f"\n--- {self.name} Team Summary ---")
           for player in self.players:
               player.display_info()
           print(f"Total Players: {len(self.players)}")
   
   
   # Create team
   pakistan = CricketTeam("Pakistan")
   
   pakistan.add_player(babar)
   pakistan.add_player(shaheen)
   pakistan.add_player(shadab)
   
   pakistan.team_summary()
   
   # Polymorphism in action
   print("\nTraining Session:")
   for p in pakistan.players:
       p.train()
   ```

   Run live – show hierarchy, polymorphism, team management.

#### OOP Design Tips
- Favor composition over inheritance when possible (has-a vs is-a).  
- Keep inheritance depth shallow (2-3 levels max).  
- Use inheritance for true “is-a” relationships (Batsman is a Player).  
- Polymorphism makes code flexible – write functions that accept base class.

#### Homework for Day 15
1. Run all examples – create Player hierarchy.
2. Build a full Cricket Team Management OOP system:
   - Base Player class.
   - At least Batsman, Bowler, AllRounder subclasses.
   - Team class that holds list of players, with methods: add_player, remove_player, team_summary, training_session (calls train on all).
   - Add a Captain designation (maybe a class variable or separate method).
3. Bonus Project: Bank system with inheritance:
   - Base Account → SavingsAccount (with interest), CurrentAccount (with overdraft).
   - Bank class to manage multiple accounts.
4. Comment “Day 15 Done ✅” with screenshot of your team summary showing different player types.
5. (Advanced Bonus): Implement multiple inheritance carefully for a WicketKeeperBatsman class.
