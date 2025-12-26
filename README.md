### Day 5: Loops in Python – while and for (Repeating Tasks Like an Automation Bot)

**Live Session Plan (9:30 - 10:30 PST / ~9:30 - 10:30 PM PKT/IST)**  
- **0-5 mins**: Welcome + recap Day 4 + shoutouts to homework (discount calculator enhancements – especially festival bonuses and free shipping).  
- **5-20 mins**: Introduction to loops + while loop deep dive.  
- **20-40 mins**: for loop + range() mastery with examples.  
- **40-55 mins**: Loop control (break, continue, else) + live mini project.  
- **55-60 mins**: Q&A, common pitfalls, homework.

1. **Welcome & Recap (5 mins)**  
   - "Assalam-o-Alaikum everyone! Day 5 – we're building momentum!  
   - Yesterday we made our programs intelligent with if/elif/else. So many creative discount calculators – Eid/Diwali specials, free shipping, super saver messages – you guys are already thinking like developers!  
   - Today: We teach Python to REPEAT tasks automatically. Loops are the heart of automation – think scraping prices daily, sending reminders, or processing 1000 job applications. This is where real agent power begins."

2. **Why Loops? + Introduction**  
   - Without loops: You’d have to write the same code 100 times.  
   - With loops: Tell Python “do this until condition met” or “do this for each item”.  
   - Two main types:  
     - `while` → repeat as long as condition is True (like waiting for user input).  
     - `for` → repeat for each item in a sequence (perfect for lists, ranges).

3. **while Loop – Deep Dive**  
   New file: `day5_loops.py`

   Syntax:
   ```python
   while condition:
       # code to repeat
   ```

   **Example 1: Simple Countdown**
   ```python
   print("🚀 Countdown to Automation Mastery!")
   count = 10
   while count > 0:
       print(count)
       count -= 1   # same as count = count - 1
   print("Blast off! You're now looping like a pro!")
   ```

   **Example 2: User Input Until Correct**
   ```python
   secret_password = "agent123"
   attempt = ""
   
   while attempt != secret_password:
       attempt = input("Enter password to access AI Agent: ")
       if attempt != secret_password:
           print("❌ Wrong! Try again.")
   
   print("✅ Access granted! Welcome to the Agentic World!")
   ```

   **Example 3: Savings Goal Tracker **
   ```python
   target = float(input("Enter your savings goal (PKR): "))
   current = 0
   months = 0
   
   while current < target:
       monthly_save = float(input(f"Month {months+1} - How much did you save? "))
       current += monthly_save
       months += 1
       print(f"Current savings: PKR {current}")
   
   print(f"🎉 Goal achieved in {months} months! Total: PKR {current}")
   ```

   Warning: Infinite loops! Show what happens if you forget to update the condition (e.g., remove `count -= 1`).

4. **for Loop + range()**  

   Syntax:
   ```python
   for variable in sequence:
       # code to repeat
   ```

   **range() function** – generates numbers  
   ```python
   for i in range(5):          # 0 to 4
       print(i)
   
   for i in range(1, 11):      # 1 to 10
       print(i)
   
   for i in range(0, 21, 2):   # step by 2 → even numbers
       print(i)
   
   for i in range(10, 0, -1):  # countdown
       print(i)
   ```

   **Example: Multiplication Table**
   ```python
   number = int(input("Enter number for table: "))
   
   print(f"\nMultiplication Table of {number}:")
   for i in range(1, 11):
       print(f"{number} x {i} = {number * i}")
   ```

5. **Loop Control Statements + Mini Project**  

   - `break` → exit loop immediately  
   - `continue` → skip to next iteration  
   - `else` on loops → runs if no break (rare but useful)

   **Mini Project, Number Guessing Game (Agent Training Simulation)**
   ```python
   import random
   
   print("🧠 AI Agent Training: Number Guessing Game")
   print("I'm thinking of a number between 1 and 100.\n")
   
   secret = random.randint(1, 100)
   attempts = 0
   max_attempts = 7
   
   for attempt in range(1, max_attempts + 1):
       guess = int(input(f"Attempt {attempt}/{max_attempts} - Your guess: "))
       attempts += 1
       
       if guess < secret:
           print("📈 Too low!")
       elif guess > secret:
           print("📉 Too high!")
       else:
           print(f"🎉 Correct! You guessed it in {attempts} attempts.")
           break
   else:  # only runs if loop completed without break
       print(f"😞 Game over! The number was {secret}.")
       print("Better luck next time – agents learn from failure!")
   ```

   - Run live multiple times. Show how it feels like training an agent.

#### Common Pitfalls
- Forgetting to increment/decrement in while → infinite loop (Ctrl+C to stop).  
- Off-by-one errors in range() (range(1,11) is 1 to 10).  
- Indentation errors.

#### Homework for Day 5
1. Run all examples from today.
2. Build an enhanced Number Guessing Game:
   - Add hints like "very close" if within 5 numbers.
   - Track and show best score (fewest attempts).
   - Let user play multiple rounds (ask "Play again?").
3. Alternative project: Create an automatic savings calculator that shows monthly growth until target (using while or for).
4. Comment “Day 5 Done ✅” with screenshot of your game in action (win and lose scenarios).
5. (Bonus): Print a pattern like pyramid of stars using nested loops (teaser for tomorrow).
