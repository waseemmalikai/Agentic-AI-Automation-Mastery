### Day 7: Introduction to Lists (Python’s Most Important Data Structure)

**Live Session Plan (9:30 - 10:30 PST / ~9:30 - 10:30 PM PKT/IST)**  

1. **Welcome & Recap**  
   - "Assalam-o-Alaikum everyone! Day 6 – we're flying through the basics and getting stronger every day!  
   - Yesterday loops unlocked automation power.
   - Today: we finally meet Python Lists – the #1 data structure we'll use in every agent, database, and ML project."

3. **Introduction to Lists – The Superhero Data Structure**  

   - "A list is an ordered collection that can hold anything – numbers, strings, even other lists!"  
   - Creation:
     ```python
     fruits = ["apple", "banana", "mango", "orange"]
     numbers = [10, 20, 30, 40]
     mixed = [1, "hello", True, 3.14]
     empty = []
     
     print(fruits)
     print(type(fruits))    # <class 'list'>
     ```

   - **Indexing & Slicing** (very important)
     ```python
     print(fruits[0])       # "apple"  (0-based indexing)
     print(fruits[-1])      # "orange" (negative = from end)
     print(fruits[1:3])     # ["banana", "mango"] (slice)
     print(fruits[:2])      # first two
     print(fruits[2:])      # from index 2 to end
     ```

   - **Modifying Lists** (mutable!)
     ```python
     fruits[1] = "grapes"           # change
     fruits.append("watermelon")    # add to end
     fruits.insert(0, "kiwi")       # insert at position
     fruits.remove("mango")         # remove by value
     popped = fruits.pop()          # remove and return last
     print(popped)
     ```

   - **Common List Methods Cheat Sheet** (show on screen)
     | Method          | What it does                     | Example                     |
     |-----------------|----------------------------------|-----------------------------|
     | append()        | Add to end                       | list.append("new")          |
     | extend()        | Add multiple                     | list.extend(["a","b"])      |
     | insert()        | Insert at index                  | list.insert(0, "first")     |
     | remove()        | Remove first occurrence          | list.remove("item")         |
     | pop()           | Remove and return by index       | list.pop(2)                 |
     | index()         | Find position                    | list.index("item")          |
     | count()         | Count occurrences                | list.count("item")          |
     | sort()          | Sort in place                    | list.sort()                 |
     | reverse()       | Reverse in place                 | list.reverse()              |
     | len()           | Length                           | len(list)                   |

   - **Looping Through Lists**
     ```python
     shopping = ["rice", "oil", "sugar", "flour"]
     
     for item in shopping:
         print(f"Buy {item}")
     
     for i in range(len(shopping)):
         print(f"{i+1}. {shopping[i]}")
     ```

4. **Mini Project Live Build: Grocery List Manager**  

   ```python
   print("🛍️  Smart Grocery List Manager\n")
   
   grocery = []
   
   while True:
       print("\nOptions: 1=Add, 2=Remove, 3=View, 4=Clear, 5=Exit")
       choice = input("Choose: ")
       
       if choice == "1":
           item = input("Enter item: ").strip()
           if item:
               grocery.append(item.capitalize())
               print(f"✅ {item} added!")
       elif choice == "2":
           item = input("Remove item: ").strip()
           if item in grocery:
               grocery.remove(item.capitalize())
               print("❌ Removed!")
           else:
               print("Not in list!")
       elif choice == "3":
           if grocery:
               print("\n🛒 Your Grocery List:")
               for i, item in enumerate(grocery, 1):
                   print(f"   {i}. {item}")
               print(f"Total items: {len(grocery)}")
           else:
               print("List is empty!")
       elif choice == "4":
           grocery.clear()
           print("🗑️  List cleared!")
       elif choice == "5":
           print("Thanks for using! See you at the market!")
           break
       else:
           print("Invalid choice!")
   
   # Bonus: Save for tomorrow (we'll add file handling later)
   ```

   Run live – add/remove items, show how powerful lists + loops are.

#### Common Mistakes
- Forgetting `end=" "` in print for patterns → stars go vertical.  
- IndexError: list index out of range.  
- Using `==` instead of `in` for checking existence.

#### Homework for Day 7
2. Build an enhanced Grocery Manager:
   - Add quantity: store as list of lists or dicts (e.g., ["Rice", 5], ["Oil", 2]).
   - Show total estimated cost (assign fake prices).
   - Sort list alphabetically.
3. Alternative: Create a Cricketer scorecard list and calculate average runs.
4. Comment “Day 7 Done ✅” with screenshot of your pattern + grocery manager.
5. (Bonus): Print Floyd's Triangle (1, 2 3, 4 5 6, etc.).
