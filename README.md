### Day 9: Functions in Python – Reusable Code Blocks (The Key to Clean & Professional Code)

**Live Session Plan (9:30 - 10:30 PST / ~9:30 - 10:30 PM PKT/IST)**  
- **0-5 mins**: Welcome + recap Day 8 + shoutouts to homework (enhanced contact books with address, reverse search, cricket databases).  
- **5-25 mins**: What are functions? Defining, calling, parameters vs arguments.  
- **25-45 mins**: Return statements, default parameters, keyword arguments, variable arguments (*args, **kwargs).  
- **45-55 mins**: Scope (local vs global) + live mini project refactoring with functions.  
- **55-60 mins**: Q&A, best practices, homework.


1. **Welcome & Recap (5 mins)**  
   - "Assalam-o-Alaikum everyone! Day 9 – we’re officially pros at handling data now!  
   - Yesterday dictionaries changed everything – amazing contact books with reverse lookup, addresses, export options, and detailed cricket player databases. You’re building real-world apps already!  
   - Today: We learn FUNCTIONS – the secret to writing clean, reusable, professional code. Without functions, your agentic AI code will become messy and unmanageable. With functions, everything becomes modular, testable, and powerful."

2. **What is a Function? Why Do We Need It? (8 mins)**  
   New file: `day9_functions.py`

   - A function is like a mini-program inside your program. You give it input (ingredients), it does work, and gives back output (dish). 
   - Without functions → repeat same code (DRY violation – Don’t Repeat Yourself).  
   - With functions → write once, use anywhere.

   Basic structure:
   ```python
   def function_name(parameters):
       # code block
       # optional return
       return something
   ```

3. **Defining & Calling Functions**  

   **Example 1: Simple Greeting**
   ```python
   def greet():
       print("Assalam-o-Alaikum! Welcome to your AI Agent Course!")
   
   # Call the function
   greet()
   greet()   # call multiple times
   ```

   **Example 2: With Parameters**
   ```python
   def greet_person(name):
       print(f"Hello {name}! Ready to build agents today?")
   
   greet_person("Ahmed")
   greet_person("Sara")
   ```

   **Example 3: Multiple Parameters**
   ```python
   def calculate_zakat(wealth, nisab=85000, rate=0.025):
       if wealth >= nisab:
           zakat_amount = wealth * rate
           print(f"Zakat due: PKR {zakat_amount:.2f}")
       else:
           print("No Zakat due this year.")
   
   calculate_zakat(500000)                    # uses defaults
   calculate_zakat(1000000, rate=0.025)       # override rate
   ```

   - Parameters (in definition) vs Arguments (when calling)  
   - Default parameters – very useful!

4. **Return Statement**  

   ```python
   def add(a, b):
       result = a + b
       return result     # sends value back
   
   # or shorter
   def multiply(x, y):
       return x * y
   
   sum_result = add(10, 20)
   print("Sum:", sum_result)
   
   total = add(5, 3) * multiply(2, 4)
   print("Combined:", total)   # 64
   ```

   - Functions without return → return None by default.

   **Real Example: Discount Calculator as Function**
   ```python
   def apply_discount(amount, is_prime=False, has_coupon=False):
       discount = 0
       if amount >= 5000:
           discount = 10
           if is_prime:
               discount += 15
           if has_coupon:
               discount += 10
       elif amount >= 2000 and has_coupon:
           discount = 15
       
       final = amount - (amount * discount / 100)
       return final, discount   # return multiple values (as tuple)
   
   final_price, disc_percent = apply_discount(8000, is_prime=True, has_coupon=True)
   print(f"Final Price: PKR {final_price}, Discount: {disc_percent}%")
   ```

5. **Advanced Arguments: *args and **kwargs (8 mins)**  

   ```python
   def print_items(*args):        # any number of positional args
       for item in args:
           print(item)
   
   print_items("rice", "oil", "sugar", 5, True)
   
   def player_info(**kwargs):     # keyword arguments
       for key, value in kwargs.items():
           print(f"{key}: {value}")
   
   player_info(name="Babar Azam", runs=5000, average=55.5, team="Pakistan")
   
   # Combine everything
   def super_function(a, b, *args, default=10, **kwargs):
       print(a, b, args, default, kwargs)
   
   super_function(1, 2, 3, 4, 5, extra="hello", mode="advanced")
   ```

6. **Scope: Local vs Global Variables**  

   ```python
   x = 100   # global
   
   def test():
       x = 50   # local – different from global
       print("Inside function:", x)
   
   test()
   print("Outside:", x)   # 100
   
   # To modify global
   y = 200
   def modify_global():
       global y
       y = 300
   
   modify_global()
   print(y)   # 300
   ```

   Best practice: Avoid global variables – pass as parameters.

7. **Mini Project Refactor Contact Book Using Functions**  

   ```python
   def add_contact(contacts, name, phone, email="N/A"):
       contacts[name] = {"phone": phone, "email": email}
       print(f"✅ {name} added!")
   
   def view_all_contacts(contacts):
       if not contacts:
           print("No contacts!")
           return
       print("\n📋 All Contacts:")
       for name, info in contacts.items():
           print(f"   {name}: {info['phone']} ({info['email']})")
   
   # Main program
   contacts = {}
   add_contact(contacts, "Ali", "03001234567", "ali@example.com")
   add_contact(contacts, "Sara", "03331234567")
   view_all_contacts(contacts)
   ```

#### Best Practices Quick List
- Function names: snake_case, descriptive (e.g., `calculate_discount` not `cd`)
- One function = one job
- Keep functions short (under 30 lines ideally)
- Use meaningful parameter names
- Add comments/docstrings (we’ll cover later)

#### Homework for Day 9
1. Run all examples.
2. Refactor your Day 8 Contact Book completely using functions:
   - Separate functions for add, search, update, delete, view.
   - Main menu in a loop calling these functions.
3. Bonus Project: Build a "Cricket Score Calculator" with functions:
   - Functions for calculate_average(runs_list), calculate_strike_rate(runs, balls), etc.
   - Input player stats and show summary.
4. Comment “Day 9 Done ✅” with screenshot of your refactored contact book or cricket calculator.
5. (Advanced Bonus): Write a function that takes *args of numbers and returns mean, median, max, min.
