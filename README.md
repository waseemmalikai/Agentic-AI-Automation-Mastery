### Day 7: Advanced List Operations, List Comprehensions & Introduction to Tuples and Sets

**Live Session Plan (9:30 - 10:30 PST / ~9:30 - 10:30 PM PKT/IST)**  
- **0-5 mins**: Welcome + recap Day 6 + shoutouts to homework (patterns, enhanced grocery managers with quantities and costs).  
- **5-25 mins**: Advanced list operations (slicing tricks, comprehensions, copying pitfalls).  
- **25-45 mins**: Tuples – immutable lists (when and why to use).  
- **45-55 mins**: Sets – unique collections + set operations.  
- **55-60 mins**: Q&A, mini comparison, homework.

1. **Welcome & Recap (5 mins)**  
   - "Assalam-o-Alaikum everyone! Day 7 – Alhamdulillah we’re one week in and already building real apps!  
   - Yesterday nested loops + lists blew minds – beautiful patterns and smart grocery managers with quantities, sorting, estimated costs. You’re turning into serious coders!  
   - Today: We master lists completely (including the super-powerful list comprehensions), then meet two new data structures: Tuples and Sets. These three (List, Tuple, Set) are the foundation for everything – databases, APIs, agent memory, ML datasets."

2. **Advanced List Operations**  
   Continue in `day7_advanced_collections.py`

   - **Advanced Slicing Tricks**
     ```python
     numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
     
     print(numbers[::2])     # even indices: [0, 2, 4, 6, 8]
     print(numbers[::-1])    # reverse list: [9, 8, ..., 0]
     print(numbers[1:8:3])   # start:stop:step
     ```

   - **List Comprehensions – Python’s Most Elegant Feature**
     "Short, powerful way to create/transform lists."
     
     Normal way:
     ```python
     squares = []
     for i in range(1, 11):
         squares.append(i ** 2)
     ```
     
     Comprehension way (one line!):
     ```python
     squares = [i ** 2 for i in range(1, 11)]
     print(squares)
     ```
     
     With condition:
     ```python
     even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
     print(even_squares)     # [4, 16, 36, 64, 100]
     
     # Convert prices PKR to USD (rate 278)
     prices_pkr = [5000, 8000, 12000, 3000]
     prices_usd = [round(p / 278, 2) for p in prices_pkr]
     print(prices_usd)
     ```

   - **Common Pitfall: List Copying**
     ```python
     list1 = [1, 2, 3]
     list2 = list1          # NOT a copy! Both point to same list
     list2.append(4)
     print(list1)           # [1, 2, 3, 4] → surprise!
     
     # Correct ways:
     list3 = list1.copy()          # or list1[:] or list(list1)
     ```

   - **Nested Lists (2D Lists) – Like Tables**
     ```python
     matrix = [
         [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]
     ]
     print(matrix[1][2])    # 6
     
     # Print like table
     for row in matrix:
         for val in row:
             print(val, end=" ")
         print()
     ```

3. **Tuples – Immutable Sequences (15 mins)**  
   - "Tuples are like lists but cannot be changed – perfect for fixed data."
   
   Creation:
   ```python
   coordinates = (24.8607, 67.0011)   # Karachi lat, long
   fruits = ("apple", "banana", "mango")
   single = (42,)                     # note comma for single item
   empty = ()
   
   print(type(coordinates))           # <class 'tuple'>
   ```

   - Why use tuples?
     - Faster than lists
     - Safe (can't accidentally modify)
     - Can be used as dictionary keys (later)
     - Function returns multiple values as tuple

   - Operations (similar to lists but no modification)
     ```python
     print(fruits[1])       # "banana"
     print(fruits.count("apple"))
     print(fruits.index("mango"))
     
     # Unpacking – super useful!
     lat, long = coordinates
     print(f"Latitude: {lat}, Longitude: {long}")
     
     # Swap variables easily
     a = 10
     b = 20
     a, b = b, a
     print(a, b)            # 20 10
     ```

4. **Sets – Unique Unordered Collections (10 mins)**  
   - "Sets store unique items only – great for removing duplicates, membership testing, math operations."
   
   Creation:
   ```python
   unique_numbers = {1, 2, 2, 3, 3, 4}   # duplicates removed → {1,2,3,4}
   empty_set = set()                    # {} is dict, not set!
   
   fruits_set = {"apple", "banana", "mango"}
   ```

   - Key features:
     - No duplicates
     - No indexing (unordered)
     - Very fast lookup

   - Common methods:
     ```python
     fruits_set.add("orange")
     fruits_set.remove("banana")          # error if not exists
     fruits_set.discard("grapes")         # safe remove
     
     print("apple" in fruits_set)         # True – very fast!
     ```

   - Set operations (like math):
     ```python
     set_a = {1, 2, 3, 4}
     set_b = {3, 4, 5, 6}
     
     print(set_a | set_b)     # union: {1,2,3,4,5,6}
     print(set_a & set_b)     # intersection: {3,4}
     print(set_a - set_b)     # difference: {1,2}
     print(set_a ^ set_b)     # symmetric difference: {1,2,5,6}
     ```

5. **Quick Comparison Table (Show on Screen)**
   | Feature         | List              | Tuple             | Set                  |
   |-----------------|-------------------|-------------------|----------------------|
   | Mutable         | Yes               | No                | Yes                  |
   | Duplicates      | Yes               | Yes               | No                   |
   | Ordered         | Yes               | Yes               | No                   |
   | Indexing        | Yes               | Yes               | No                   |
   | Use case        | Ordered data      | Fixed records     | Unique items, math   |

#### Mini Project Idea (If Time)
Remove duplicates from a list using set.
```python
 messy = [1, 2, 2, 3, 3, 4, 1, 5]
 clean = list(set(messy))
 print(clean)   # order may vary
```

#### Homework for Day 7
1. Practice all examples.
2. Build a "Cricket Team Manager":
   - Use list for players (with names).
   - Use set for unique skills (e.g., "batting", "bowling").
   - Use tuple for fixed player info (name, age, role).
   - Features: Add player, show unique skills, find common skills between two teams.
3. Alternative: Create a currency converter using list comprehensions for multiple amounts.
4. Comment “Day 7 Done ✅” with screenshot of your team manager or unique skills output.
5. (Bonus): Use list comprehension to generate first 20 Fibonacci numbers.
