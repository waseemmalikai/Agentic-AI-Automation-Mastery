### Day 10: Advanced Functions – Lambda, Recursion, Docstrings & Introduction to Error Handling

**Live Session Plan (9:30 - 10:30 PST / ~9:30 - 10:30 PM PKT/IST)**  
- **0-5 mins**: Welcome + recap Day 9 + shoutouts to homework (refactored contact books, cricket score calculators with multiple functions).  
- **5-25 mins**: Lambda functions + higher-order functions (map, filter, sorted).  
- **25-40 mins**: Docstrings + recursion with examples.  
- **40-55 mins**: Error handling (try/except/else/finally) + live robust code demo.  
- **55-60 mins**: Q&A, best practices, homework.

1. **Welcome & Recap**  
   - "Assalam-o-Alaikum everyone! Day 10 – double digits, mashAllah! We're turning into real Python developers.  
   - Yesterday functions made our code clean and professional. So many beautifully refactored contact books and cricket calculators – modular, readable, reusable. This is exactly how real agentic AI code is written!  
   - Today: We level up functions even more – lambda (anonymous functions), recursion (functions calling themselves), proper documentation with docstrings, and most importantly, error handling so our agents don’t crash on bad input."

2. **Lambda Functions – One-Line Anonymous Functions**  
   New file: `day10_advanced_functions.py`

   - "Lambda is a small anonymous function – no name, usually one expression."
   Syntax:
   ```python
   lambda parameters: expression
   ```

   **Example 1: Simple Lambda**
   ```python
   square = lambda x: x ** 2
   print(square(5))   # 25
   
   # Direct use
   print((lambda x: x ** 2)(7))   # 49
   ```

   **Example 2: With Multiple Parameters**
   ```python
   add = lambda a, b=10: a + b
   print(add(5))      # 15
   print(add(5, 20))  # 25
   ```

   **Real Power: With map(), filter(), sorted()**

   - `map()` – apply function to every item
     ```python
     numbers = [1, 2, 3, 4, 5]
     squares = list(map(lambda x: x ** 2, numbers))
     print(squares)     # [1, 4, 9, 16, 25]
     
     prices_pkr = [5000, 8000, 12000]
     prices_usd = list(map(lambda p: round(p / 278, 2), prices_pkr))
     print(prices_usd)
     ```

   - `filter()` – keep items where function returns True
     ```python
     ages = [15, 22, 17, 30, 19]
     adults = list(filter(lambda age: age >= 18, ages))
     print(adults)      # [22, 30, 19]
     ```

   - `sorted()` with key
     ```python
     players = [("Babar", 55.5), ("Rizwan", 52.3), ("Shaheen", 20.1)]
     sorted_by_avg = sorted(players, key=lambda player: player[1], reverse=True)
     print(sorted_by_avg)
     # [('Babar', 55.5), ('Rizwan', 52.3), ('Shaheen', 20.1)]
     ```

3. **Docstrings – Professional Documentation**  
   - "Triple quotes right after function definition – explains what it does, parameters, return."
   ```python
   def calculate_discount(amount, is_prime=False, has_coupon=False):
       """
       Calculate final price after applying discounts.
       
       Args:
           amount (float): Cart total in PKR
           is_prime (bool): Whether customer is Prime member
           has_coupon (bool): Whether coupon is applied
       
       Returns:
           tuple: (final_price, discount_percentage)
       """
       discount = 0
       # ... logic ...
       final = amount - (amount * discount / 100)
       return final, discount
   
   # View docstring
   print(calculate_discount.__doc__)
   help(calculate_discount)   # shows nicely in interactive
   ```

   Best practice: Always write docstrings for functions you’ll reuse.

4. **Recursion – Function Calling Itself**  
   - "Like a loop, but using function calls – useful for problems that break into smaller same problems."
   
   **Classic Example: Factorial**
   ```python
   def factorial(n):
       if n == 0 or n == 1:    # base case – MUST have!
           return 1
       else:
           return n * factorial(n - 1)   # recursive call
   
   print(factorial(5))   # 120
   print(factorial(0))   # 1
   ```

   **Another: Fibonacci**
   ```python
   def fib(n):
       if n <= 1:
           return n
       return fib(n-1) + fib(n-2)
   
   for i in range(10):
       print(fib(i), end=" ")   # 0 1 1 2 3 5 8 13 21 34
   ```

   Warning: Too deep recursion → RecursionError (Python limit ~1000). We’ll optimize later with memoization.

5. **Error Handling – Making Code Robust (try/except) (15 mins)**  
   - "Real agents deal with bad input, missing files, network issues – they shouldn’t crash!"
   
   Basic structure:
   ```python
   try:
       # risky code
   except ErrorType:
       # handle error
   else:
       # runs if no error
   finally:
       # always runs (cleanup)
   ```

   **Example: Safe Division**
   ```python
   def safe_divide(a, b):
       try:
           result = a / b
       except ZeroDivisionError:
           print("❌ Cannot divide by zero!")
           return None
       except TypeError:
           print("❌ Please enter numbers only!")
           return None
       else:
           return result
       finally:
           print("Division attempt completed.")
   
   print(safe_divide(10, 2))   # 5.0
   print(safe_divide(10, 0))   # None
   print(safe_divide(10, "5")) # None
   ```

   **Example: Safe Input Conversion**
   ```python
   while True:
       try:
           age = int(input("Enter your age: "))
           if age < 0:
               raise ValueError("Age cannot be negative!")
           break
       except ValueError as e:
           print(f"Invalid input: {e}. Try again.")
   
   print(f"You are {age} years old.")
   ```

   **Make Yesterday’s Contact Book Robust**
   Add try/except around input conversions and key access.


#### Best Practices Summary
- Use lambda for short, simple functions passed to map/filter/sorted.  
- Always have base case in recursion.  
- Write docstrings for reusable functions.  
- Handle expected errors gracefully – never let program crash on user input.

#### Homework for Day 10
1. Practice all examples (lambda with map/filter, recursion, error handling).
2. Enhance your Contact Book or Cricket Calculator:
   - Add proper docstrings to all functions.
   - Use lambda for sorting contacts alphabetically or players by average.
   - Add full error handling (invalid inputs, duplicate names, etc.).
3. Bonus Project: Create a "Recursive File Size Calculator" concept (explain directory tree) or a safe calculator app with all operations protected.
4. Comment “Day 10 Done ✅” with screenshot showing error handling in action (e.g., dividing by zero gracefully).
5. (Advanced Bonus): Write a recursive function to generate all possible combinations of a grocery list under a budget.
