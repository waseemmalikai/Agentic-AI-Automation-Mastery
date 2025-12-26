### Day 12: Modules, Packages & Organizing Large Projects (Code Like a Professional Developer)

**Live Session Plan (9:30 - 10:30 PST / ~9:30 - 10:30 PM PKT/IST)**  
- **0-5 mins**: Welcome + recap Day 11 + shoutouts to homework (persistent contact books that save/load from JSON/CSV, daily journals).  
- **5-25 mins**: What are modules? Importing (import, from...import, aliases), built-in modules demo.  
- **25-45 mins**: Creating your own modules + intro to packages (__init__.py, relative imports).  
- **45-55 mins**: Live project: Split Contact Book into multiple modules (utils.py, storage.py, main.py).  
- **55-60 mins**: Q&A, best practices, homework.


1. **Welcome & Recap**  
   - "Assalam-o-Alaikum everyone! Day 12 – we're now organizing code like real software engineers!  
   - Yesterday file handling made our apps truly useful – persistent contact books, journals that remember everything after restart. Mind-blowing progress!  
   - Today: Modules and Packages. As our agentic AI projects grow (hundreds/thousands of lines), putting everything in one file becomes chaos. Modules let us split code logically, reuse across projects, and collaborate easily."

2. **What is a Module? + Importing Basics**  
   New project folder: `day12_modules_demo`

   - "A module is simply a Python file (.py) containing functions, classes, variables."  
   - Built-in modules example:

   ```python
   # day12_builtins.py
   import random
   import math
   import datetime
   import os
   
   print(random.randint(1, 100))                    # random number
   print(math.pi)                                   # 3.14159...
   print(math.sqrt(16))                             # 4.0
   
   today = datetime.date.today()
   print("Today:", today)
   
   print("Current folder:", os.getcwd())
   print("Files here:", os.listdir("."))
   ```

   - Different import styles:
     ```python
     from random import randint, choice
     from math import pi as MATH_PI
     from datetime import datetime as dt
   
     print(randint(1, 6))                  # dice roll
     print(MATH_PI)
     print(dt.now())
     ```

   - Useful built-in modules we’ll use a lot:
     | Module       | Use Case                              |
     |--------------|---------------------------------------|
     | random       | Simulations, games, agent decisions   |
     | math         | Calculations                          |
     | datetime     | Timestamps, scheduling                |
     | os           | File/folder operations                |
     | sys          | Command-line args, exit               |
     | json         | Already used – data storage           |
     | itertools    | Advanced looping (later)              |
     | collections  | Advanced data structures              |

3. **Creating Your Own Modules**  
   Create multiple files in the same folder.

   **File 1: utils.py** (helper functions)
   ```python
   # utils.py
   def print_header(title):
       print("\n" + "=" * 50)
       print(title.center(50))
       print("=" * 50)
   
   def get_valid_input(prompt, type_func=int):
       while True:
           try:
               return type_func(input(prompt))
           except ValueError:
               print("❌ Invalid input – try again.")
   ```

   **File 2: main.py** (uses the module)
   ```python
   # main.py
   import utils
   # or: from utils import print_header, get_valid_input
   
   utils.print_header("My Agentic App")
   
   age = utils.get_valid_input("Enter your age: ")
   print(f"You are {age} years old!")
   ```

   Run `main.py` live – show how clean separation is.

   - If module not found → check same folder or PYTHONPATH.

4. **Packages – Grouping Related Modules (10 mins)**  
   - Package = folder with modules + `__init__.py` file (can be empty in Python 3.3+)

   Folder structure:
   ```
   contact_book_package/
   ├── __init__.py
   ├── storage.py          # file handling functions
   ├── ui.py               # display functions
   └── operations.py       # add/delete/update logic
   ```

   **Example: storage.py**
   ```python
   # contact_book_package/storage.py
   import json
   import os
   
   FILE_PATH = "data/contacts.json"
   
   def load_contacts():
       if os.path.exists(FILE_PATH):
           with open(FILE_PATH, "r") as f:
               return json.load(f)
       return {}
   
   def save_contacts(contacts):
       os.makedirs("data", exist_ok=True)
       with open(FILE_PATH, "w") as f:
           json.dump(contacts, f, indent=4)
   ```

   **In main.py (outside package)**
   ```python
   from contact_book_package import storage
   # or: from contact_book_package.storage import load_contacts
   
   contacts = storage.load_contacts()
   print("Loaded contacts:", contacts)
   ```

   - `__init__.py` can expose functions:
     ```python
     # __init__.py
     from .storage import load_contacts, save_contacts
     from .operations import add_contact
     ```

     Then: `from contact_book_package import load_contacts`

5. **Refactor Persistent Contact Book into Modules/Package**  
   Create proper structure:

   ```
   contact_book/
   ├── main.py
   ├── data/contacts.json
   └── contact_manager/
       ├── __init__.py
       ├── storage.py      # load/save
       ├── ui.py           # print menus, headers
       └── operations.py   # add/search/delete
   ```

   - Move functions to appropriate files.
   - Import and run from main.py.
   - Demonstrate how easy it is to reuse `storage.py` in another project.

   Result: Clean, scalable, professional code base.

#### Best Practices
- One module = one responsibility (Single Responsibility Principle).  
- Name modules lowercase (no capitals).  
- Use meaningful names: `data_handler.py` not `stuff.py`.  
- Add docstrings to modules too.  
- Never use `from module import *` in production (pollutes namespace).

#### Homework for Day 12
1. Run all examples – create utils.py and use it in a small script.
2. Fully refactor your persistent Contact Book into a proper package:
   - At least 3 modules: storage, ui, operations.
   - main.py only handles menu loop and calls package functions.
   - Add a header using ui module.
3. Bonus Project: Create a "Cricket Stats Package":
   - Modules for player data, calculations (average, strike rate), display.
   - Load/save player stats from JSON.
4. Comment “Day 12 Done ✅” with screenshot of your folder structure + running refactored app.
5. (Advanced Bonus): Add a `config.py` module with settings (file paths, constants).
