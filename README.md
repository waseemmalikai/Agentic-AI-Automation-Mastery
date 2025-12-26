### Day 14: OOP Continued – Instance vs Class Variables, Class Methods, Encapsulation & Special Methods

**Live Session Plan (9:30 - 10:30 PST / ~9:30 - 10:30 PM PKT/IST)**  
- **0-5 mins**: Welcome + recap Day 13 + shoutouts to homework (OOP contact books, BankAccount classes with transfers).  
- **5-25 mins**: Instance vs class variables + class methods (@classmethod) + static methods (@staticmethod).  
- **25-45 mins**: Encapsulation (private attributes, name mangling) + special methods (__str__, __repr__, __len__, etc.).  
- **45-55 mins**: Live project: Enhance OOP Contact Book with class variables, better printing, and validation.  
- **55-60 mins**: Q&A, common pitfalls, homework, teaser for Day 15.

#### Detailed Session Script / Talking Points

1. **Welcome & Recap**  
   - "Assalam-o-Alaikum everyone! Day 14 – mashAllah your OOP skills are growing fast!  
   - Yesterday we started modeling real-world entities with classes. So many beautiful OOP contact books and bank account systems with transfers – you’re already thinking like object-oriented developers!  
   - Today: We go deeper into OOP. We’ll learn the difference between instance and class data, different types of methods, how to protect data (encapsulation), and make our objects print nicely with special methods."

2. **Instance Variables vs Class Variables (15 mins)**  
   New folder: `day14_oop_advanced`  
   File: `day14_variables_methods.py`

   - **Instance variables**: Unique to each object (what we used yesterday)
   - **Class variables**: Shared across all objects of the class

   ```python
   class Cricketer:
       total_players = 0                    # class variable (shared)
       
       def __init__(self, name, age):
           self.name = name                 # instance variable
           self.age = age
           Cricketer.total_players += 1     # increment shared counter
   
   # Usage
   print(Cricketer.total_players)   # 0
   
   babar = Cricketer("Babar Azam", 30)
   rizwan = Cricketer("Mohammad Rizwan", 32)
   
   print(Cricketer.total_players)   # 2
   print(babar.total_players)       # 2 (accessed via instance but same value)
   print(rizwan.total_players)      # 2
   ```

   Real use: Tracking total contacts, bank interest rate shared by all accounts, etc.

3. **Different Types of Methods**  

   - **Instance methods**: Take `self` – work on specific object (most common)
   - **Class methods**: Take `cls` – work on the class itself (@classmethod)
   - **Static methods**: No `self` or `cls` – just utility functions (@staticmethod)

   ```python
   class ContactManager:
       total_contacts_created = 0
       
       def __init__(self):
           self.contacts = {}
       
       def add_contact(self, contact):              # instance method
           self.contacts[contact.name] = contact
           ContactManager.total_contacts_created += 1
       
       @classmethod
       def get_total_created(cls):                  # class method
           return cls.total_contacts_created
       
       @classmethod
       def from_file(cls, filename):                # alternative constructor
           manager = cls()                          # create new instance
           # ... load from file logic later ...
           return manager
       
       @staticmethod
       def validate_phone(phone):                   # static utility
           import re
           pattern = r"^\d{11}$"                    # simple PK format
           return bool(re.match(pattern, phone))
   
   # Usage
   print(ContactManager.get_total_created())        # 0
   
   # Validate without creating object
   print(ContactManager.validate_phone("03001234567"))  # True
   print(ContactManager.validate_phone("abc"))          # False
   ```

   - @classmethod often used for factory/alternative constructors  
   - @staticmethod for helper functions that belong logically to the class

4. **Encapsulation & Private Attributes**  
   - Python doesn’t have true private, but convention: _single underscore = protected, __double = "private"

   ```python
   class BankAccount:
       def __init__(self, holder, balance=0):
           self.holder = holder
           self._balance = balance              # protected
           self.__pin = 1234                    # "private" (name mangled)
       
       def deposit(self, amount):
           if amount > 0:
               self._balance += amount
       
       def get_balance(self):
           return self._balance
       
       def change_pin(self, old, new):
           if old == self.__pin:
               self.__pin = new
               print("PIN changed!")
           else:
               print("Wrong PIN!")
   
   acc = BankAccount("Ahmed", 5000)
   print(acc.get_balance())         # 5000
   print(acc._balance)              # 5000 (works, but don't do it!)
   # print(acc.__pin)               # AttributeError
   print(acc._BankAccount__pin)     # 1234 (name mangling – not truly private)
   ```

   Message: Use _ for "don’t touch unless you know what you’re doing", provide getters/setters.

5. **Special (Dunder) Methods – Make Objects Behave Nicely**  

   ```python
   class Contact:
       def __init__(self, name, phone):
           self.name = name.capitalize()
           self.phone = phone
       
       def __str__(self):                       # for print()
           return f"{self.name} ({self.phone})"
       
       def __repr__(self):                      # for developers/debugging
           return f"Contact('{self.name}', '{self.phone}')"
       
       def __len__(self):                       # len(obj)
           return len(self.phone)
       
       def __add__(self, other):                # obj1 + obj2
           return f"{self.name} & {other.name}"
   
   c1 = Contact("ali", "03001234567")
   c2 = Contact("sara", "03331234567")
   
   print(c1)                    # Ali (03001234567)   thanks to __str__
   print([c1, c2])              # [Contact('Ali', '...'), ...]   __repr__
   print(len(c1))               # 11
   print(c1 + c2)               # Ali & Sara
   ```

   Other useful: __eq__, __lt__ (for sorting), __getitem__ (for indexing)

6. **Live Project: Enhanced OOP Contact Book**  
   Update our Contact and ContactManager:

   ```python
   import re
   
   class Contact:
       def __init__(self, name, phone, email="N/A"):
           self.name = name.capitalize()
           if self._validate_phone(phone):
               self.phone = phone
           else:
               raise ValueError("Invalid phone number!")
           self.email = email
       
       @staticmethod
       def _validate_phone(phone):
           pattern = r"^\d{11}$"
           return bool(re.match(pattern, phone))
       
       def __str__(self):
           return f"{self.name} | {self.phone} | {self.email}"
       
       def __repr__(self):
           return f"Contact('{self.name}', '{self.phone}', '{self.email}')"
   
   
   class ContactManager:
       total_created = 0
       
       def __init__(self):
           self.contacts = {}
       
       def add(self, contact):
           self.contacts[contact.name] = contact
           ContactManager.total_created += 1
       
       def view_all(self):
           print(f"\nTotal Contacts: {len(self.contacts)} "
                 f"(Created ever: {ContactManager.total_created})")
           for contact in self.contacts.values():
               print(contact)    # uses __str__
   
   # Usage
   manager = ContactManager()
   try:
       c1 = Contact("Ali", "03001234567", "ali@example.com")
       c2 = Contact("Sara", "03331234567")
       manager.add(c1)
       manager.add(c2)
       manager.view_all()
   except ValueError as e:
       print(e)
   ```

#### Common Pitfalls
- Forgetting @classmethod/@staticmethod decorators.  
- Accessing class variables via self instead of ClassName.  
- Overusing __private when _protected is enough.

#### Homework for Day 14
1. Run all examples – play with __str__, class variables, validation.
2. Fully enhance your OOP Contact Book:
   - Add class variable for total_contacts_ever_created.
   - Add proper __str__ and __repr__ to Contact.
   - Add phone validation using static method.
   - Add a class method to create Contact from string like "Ali,03001234567,ali@example.com".
   - Use encapsulation for sensitive data (e.g., make email _protected).
3. Bonus Project: Enhance BankAccount:
   - Add class variable for bank_name and interest_rate.
   - Add class method to change interest rate for all accounts.
   - Implement __str__ and __add__ (combine balances).
4. Comment “Day 14 Done ✅” with screenshot showing nice printing and total counter.
5. (Advanced Bonus): Implement __eq__ so two contacts with same phone are considered equal.
