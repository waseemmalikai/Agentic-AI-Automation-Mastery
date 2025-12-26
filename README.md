### Day 2: Python Installation, Environment Setup & Your First Real Python Script

**Live Session Timings (9:30 - 10:30 PST / ~9:30 - 10:30 PM PKT/IST)**  
- **0-5 mins**: Quick recap of Day 1 + shoutouts to homework completers .  
- **5-35 mins**: Step-by-step Python installation & environment setup (with common troubleshooting).  
- **35-50 mins**: Write and explain your first meaningful Python script 
- **50-60 mins**: Q&A, debugging help, homework announcement

1. **Welcome Back & Recap**  
   - "Assalam-o-Alaikum everyone! Welcome to Day 2 of our 100+ day Agentic AI Mastery journey.  
   - Yesterday we understood what Agentic AI and Automation really mean, and ran our first 'Hello' script.  
   - Shoutout to everyone who commented their automation idea – I saw ideas like 'automate Upwork proposals', 'track Daraz prices', 'cricket score alerts' – we’ll build all these and more by the end!  
   - Today: We make sure EVERYONE has Python perfectly set up, and we write our first real script."

2. **Python Installation – Step by Step**  
   - **Windows Users**:
     - Go to python.org → Downloads → Latest Python (3.12 or 3.13 as of Dec 2025).
     - IMPORTANT: Check the box “Add Python to PATH” at the bottom before clicking Install.
     - After install, open Command Prompt → type `python --version` → should show version.
     - If not: Reinstall with “Add to PATH” checked.

   - **Mac Users**:
     - python.org installer OR use Homebrew (if comfortable): `brew install python`.
     - Open Terminal → `python3 --version`.

   - **Linux (Ubuntu/Debian)**:
     - `sudo apt update && sudo apt install python3 python3-pip python3-venv`.

   - **Verification**:
     - Open terminal/cmd → `python --version` and `pip --version`.
     - Live demo on your machine.

   - **Common Issues & Fixes ( Troubleshooting)**:
     - “python not recognized”: Add to PATH manually.
     - Multiple versions conflict: Use `py -3` on Windows or `python3` on Mac/Linux.

3. **Install VS Code – The Best Free Editor or Pycharm Community Addition**  
   - Download from code.visualstudio.com.
   - Install extensions (live):
     - Python (by Microsoft)
     - Pylance
     - Jupyter (for later notebooks)
     - Code Runner (optional for quick run)
   - Open a folder → create `day2.py` file.
   - Show how to run code: Right-click → Run Python File in Terminal.

4. **Virtual Environments – Why & How (Critical for Mastery)**  
   -  Projects should not share packages – virtual env keeps everything clean.
   - Create one:
     ```bash
     python -m venv .venv     # create
     # Windows:
     .venv\Scripts\activate
     # Mac/Linux:
     source .venv/bin/activate
     ```
   - Install first package: `pip install requests`.
   - Deactivate: `deactivate`

   Best Practice: Every project gets its own virtual environment.

#### Homework for Day 2
1. Successfully install Python + VS Code + run the goal tracker script.
2. Modify the script:
   - Add your own name and 3 real goals.
   - Add one more custom advice message.
3. Take a screenshot of your running script and comment “Day 2 Done ✅” with screenshot/link.
4. (Bonus): Create a virtual environment and run the script inside it.
