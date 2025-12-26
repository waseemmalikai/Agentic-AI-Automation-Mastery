### Day 3: Python Fundamentals – Variables, Data Types, and Basic Operations

**Live Session Plan (9:30 - 10:30 PST / ~9:30 - 10:30 PM PKT/IST)**  
- **0-5 mins**: Welcome + recap Day 2 + shoutouts to homework (especially screenshots of goal tracker).  
- **5-20 mins**:  What are variables, naming rules, and basic data types.  
- **20-45 mins**: Live coding + interactive examples (numbers, strings, booleans).  
- **45-55 mins**: Basic operations (arithmetic, string concatenation, type conversion).  
- **55-60 mins**: Q&A, common mistakes, homework.


1. **Welcome & Quick Recap (5 mins)**  
   - "Assalam-o-Alaikum ! Day 3 of our Agentic AI Mastery Course – great to see so many of you back!  
   - Yesterday we nailed Python installation, virtual environments,
   - Amazing homework submissions! I saw many customized versions with extra advice – keep it up!  
   - Today: We start actual Python programming. Variables, data types, and operations – the building blocks of every agent we’ll build."

2. **What is a Variable? (Theory – 8 mins)**  
   - "A variable is like a labeled box where you store something (data). You can change what’s inside anytime."  
   - Example:  
     ```python
     name = "Ahmed"        # box labeled 'name' contains "Ahmed"
     age = 25              # box labeled 'age' contains 25
     ```  
   - Rules for naming variables (very important – show common errors):  
     | Rule                  | Good Example       | Bad Example          | Why Bad?                  |
     |-----------------------|--------------------|----------------------|---------------------------|
     | Start with letter or _| user_name          | 1name                | Can't start with number   |
     | Letters, numbers, _   | total_price_2025   | total-price          | No hyphens                |
     | Case-sensitive        | Age vs age         |                      | Different variables       |
     | No Python keywords    | class = 10         | (error)              | 'class' is reserved       |
     | Meaningful names      | monthly_salary     | ms                   | Hard to read later        |

   - Best practice: Use snake_case (lowercase with underscores) – standard in Python.

3. **Basic Data Types**  
   Create a new file: `day3_datatypes.py`

   - **Integers (int)** – whole numbers  
     ```python
     age = 22
     siblings = 4
     print(age, type(age))          # <class 'int'>
     ```

   - **Floats (float)** – decimal numbers  
     ```python
     height = 5.9
     salary = 85000.50
     print(height, type(height))     # <class 'float'>
     ```

   - **Strings (str)** – text  
     ```python
     name = "Waseem"
     city = 'Karachi'                # single or double quotes
     message = """Multi-line
     string for longer text"""
     print(name, type(name))
     ```

   - **Booleans (bool)** – True or False  
     ```python
     is_student = True
     has_job = False
     print(is_student, type(is_student))   # <class 'bool'>
     ```

   - `type()` function – super useful for debugging.

4. **Basic Operations – Hands-On Coding**  

   - **Arithmetic Operations** (with int/float)  
     ```python
     a = 10
     b = 3
     
     print(a + b)   # 13    Addition
     print(a - b)   # 7     Subtraction
     print(a * b)   # 30    Multiplication
     print(a / b)   # 3.333 Division (always float)
     print(a // b)  # 3     Floor division (integer result)
     print(a % b)   # 1     Modulus (remainder)
     print(a ** b)  # 1000  Exponent (10^3)
     ```

   - **String Operations**  
     ```python
     first_name = "Ali"
     last_name = "Khan"
     full_name = first_name + " " + last_name   # Concatenation
     print(full_name)                           # Ali Khan
     
     greeting = "Hello " * 3
     print(greeting)                            # Hello Hello Hello 
     
     city = "lahore"
     print(city.upper())                        # LAHORE
     print(city.capitalize())                   # Lahore
     ```

   - **Type Conversion (Casting)** – Common source of bugs  
     ```python
     age = 25
     print("My age is " + str(age))              # Convert int to str
     
     user_input = "30"
     future_age = int(user_input) + 5
     print("In 5 years:", future_age)
     
     # Dangerous – will crash if not number:
     # int("hello") → ValueError
     ```

5. **Mini Project Simple Budget Calculator**  
   Let’s build it live together:

   ```python
   print("🧮 Simple Monthly Budget Calculator\n")
   
   income = float(input("Enter your monthly income (PKR): "))
   rent = float(input("Rent/House expense: "))
   food = float(input("Food expense: "))
   transport = float(input("Transport: "))
   other = float(input("Other expenses: "))
   
   total_expenses = rent + food + transport + other
   savings = income - total_expenses
   
   print("\n📊 Summary:")
   print(f"Total Income:    PKR {income}")
   print(f"Total Expenses:  PKR {total_expenses}")
   print(f"Savings:         PKR {savings}")
   
   if savings > 0:
       print("✅ Great! You're saving money.")
   elif savings == 0:
       print("⚠️  Break even – no savings.")
   else:
       print("❌ Overspending – plan better next month!")
   ```
   
#### Homework for Day 3
1. Run all examples from today in your VS Code.
2. Build an improved version of the Budget Calculator:
   - Add at least two more expense categories.
   - Calculate and show savings percentage: `(savings / income) * 100`
   - Add a motivational message based on savings percentage.
3. Comment “Day 3 Done ✅” with a screenshot of your improved calculator output.
4. (Bonus): Make a small script that converts PKR to USD (use fixed rate 1 USD = 278 PKR).


