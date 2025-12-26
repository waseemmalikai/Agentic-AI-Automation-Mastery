### Day 4: Control Flow – Conditional Statements (if, elif, else) & Comparison Operators

**Live Session Timings (9:30 - 10:30 PST / ~9:30 - 10:30 PM PKT/IST)**  
- **0-5 mins**: Welcome + recap Day 3 + shoutouts to homework (budget calculator screenshots – highlight creative ones).  
- **5-20 mins**: Theory – Comparison operators + logical operators.  
- **20-45 mins**: if / elif / else deep dive with live examples.  
- **45-55 mins**: Nested conditions + mini project.  
- **55-60 mins**: Q&A, common errors, homework.


1. **Welcome & Recap (5 mins)**  
   - "Assalam-o-Alaikum everyone!  
   - Yesterday we mastered variables, data types, and operations. Many of you built awesome budget calculators with percentages and motivational messages – fantastic work!  
   - Today: We make our programs SMART. We teach Python how to make decisions using conditional statements – the brain of every agent we'll build later."

2. **Comparison Operators – The Foundation of Decisions**  
   Show in new file: `day4_conditions.py`

   | Operator | Meaning              | Example            | Result    |
   |----------|----------------------|--------------------|-----------|
   | ==       | Equal to             | 10 == 10           | True      |
   | !=       | Not equal            | 10 != 5            | True      |
   | >        | Greater than         | 15 > 10            | True      |
   | <        | Less than            | 5 < 10             | True      |
   | >=       | Greater or equal     | 10 >= 10           | True      |
   | <=       | Less or equal        | 8 <= 10            | True      |

   Live demo:
   ```python
   age = 20
   print(age == 20)    # True
   print(age > 18)     # True
   print(age != 25)    # True
   ```

   Important: `==` vs `=` (assignment) – most common beginner mistake!

3. **Logical Operators – Combining Conditions**  
   | Operator | Meaning              | Example                        | Result    |
   |----------|----------------------|--------------------------------|-----------|
   | and      | Both true            | (age > 18) and (age < 65)      | True if both |
   | or       | At least one true    | (income > 50000) or (savings > 100000) | True if one |
   | not      | Reverse truth        | not (age < 18)                 | True if adult |

   Example:
   ```python
   income = 60000
   experience = 2
   eligible = (income > 50000) and (experience >= 1)
   print("Eligible for loan:", eligible)
   ```

4. **if / elif / else Statements – Decision Making**  
   Syntax reminder (show indentation matters!):
   ```python
   if condition:
       # code runs if True
   elif another_condition:    # optional, can have many
       # code runs if first false and this true
   else:                      # optional
       # code runs if all above false
   ```

   **Example 1: Simple Age Checker**
   ```python
   age = int(input("Enter your age: "))
   
   if age < 13:
       print("You're a kid – enjoy cartoons!")
   elif age < 20:
       print("Teenager – focus on studies!")
   elif age < 60:
       print("Adult – time to build your career!")
   else:
       print("Senior – wisdom era!")
   ```

   **Example 2: Grade Calculator**
   ```python
   marks = float(input("Enter your marks (0-100): "))
   
   if marks >= 90:
       grade = "A+"
   elif marks >= 80:
       grade = "A"
   elif marks >= 70:
       grade = "B"
   elif marks >= 60:
       grade = "C"
   elif marks >= 50:
       grade = "D"
   else:
       grade = "F"
       print("Better luck next time!")
   
   print(f"Your grade: {grade}")
   ```

   **Example 3: Using and/or**
   ```python
   temperature = 35
   is_raining = False
   
   if temperature > 30 and not is_raining:
       print("Perfect weather for cricket!")
   elif temperature > 30 and is_raining:
       print("Too hot and rainy – indoor day")
   else:
       print("Good weather – go out!")
   ```

5. **Nested Conditions + Mini Project: Smart Discount Calculator**  
   Let’s build a practical e-commerce discount system (like Daraz/Amazon sales):

   ```python
   print("🛒 Smart E-Commerce Discount Calculator\n")
   
   amount = float(input("Enter your cart amount (PKR): "))
   is_prime = input("Are you a Prime/VIP member? (yes/no): ").strip().lower() == "yes"
   coupon = input("Do you have a coupon code? (yes/no): ").strip().lower() == "yes"
   
   discount = 0
   
   if amount >= 5000:
       discount += 10  # 10% base for big order
       if is_prime:
           discount += 15  # extra for prime
           if coupon:
               discount += 20  # max discount
       elif coupon:
           discount += 10
   elif amount >= 2000:
       discount = 5
       if coupon:
           discount += 10
   else:
       print("Add more items to get discount!")
   
   final_amount = amount - (amount * discount / 100)
   
   print(f"\n🎉 Original: PKR {amount}")
   print(f"   Discount Applied: {discount}%")
   print(f"   Final Amount: PKR {final_amount:.2f}")
   
   if discount > 0:
       savings = amount - final_amount
       print(f"   You saved: PKR {savings:.2f} – Great deal!")
   ```

6. **Common Mistakes to Avoid**  
   - Forgetting colon `:` after if/elif/else  
   - Wrong indentation  
   - Using `=` instead of `==`  
   - Not handling user input properly (we’ll improve with error handling later)

#### Homework for Day 4
1. Run all examples from today.
2. Build an enhanced version of the Discount Calculator:
   - Add festival bonus: If user types "eid" or "diwali" as occasion, give extra 10% discount.
   - Add free shipping if final amount > 3000.
   - Show a fun message like "Super Saver!" if total discount > 30%.
3. Comment “Day 4 Done ✅” with screenshot of your enhanced calculator (at least two different scenarios).
4. (Bonus): Create a simple BMI calculator with health advice based on ranges.
