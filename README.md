### Day 18: Containerization with Docker – Run Your Agents Anywhere Consistently

**Live Session Plan (9:30 - 10:30 PST / ~9:30 - 10:30 PM PKT/IST)**  
- **0-5 mins**: Welcome + recap Day 17 + shoutouts to homework (live cricket simulators with observers, strategy switches, DI storage).  
- **5-20 mins**: What is Docker? Why containerization matters for agents & automation.  
- **20-45 mins**: Docker basics – images, containers, Dockerfile, docker run/build/compose intro.  
- **45-55 mins**: Live project: Dockerize your OOP Contact Book (or Cricket Simulator).  
- **55-60 mins**: Q&A, common issues, homework.


1. **Welcome & Recap**  
   - "Assalam-o-Alaikum  everyone! Day 18 – we're now making our apps production-ready and portable!  
   - Yesterday Observer, Strategy, and Dependency Injection took our design to architectural level. Mind-blowing live match simulators with real-time notifications, dynamic batting strategies, injectable storage – this is how professional agentic systems are built!  
   - Today: Docker! The tool that lets you package your Python agent with all dependencies and run it identically on your laptop, a cloud server, or even a Raspberry Pi in Pakistan. No more 'it works on my machine' problems."

2. **Why Docker? Real-World Problems It Solves**  
   - Common issues without Docker:
     - Different Python versions
     - Missing libraries (e.g., someone has numpy, someone doesn’t)
     - OS differences (Windows vs Linux)
     - Dependency conflicts
   - Docker solution: Package your code + exact environment into a container.
   - Benefits for our course:
     - Deploy your contact book/agent as a service
     - Share with friends – just send Dockerfile
     - Run multiple agents isolated
     - Prepare for cloud (AWS, Heroku, Vercel, Render.com free tiers)
     - Essential for production agentic AI (LangChain apps, automation bots)

   Analogy: "Docker is like a shipping container – same contents run anywhere with a Docker engine."

3. **Docker Installation & First Steps**  
   - Install Docker Desktop (free for personal use):
     - Windows/Mac: docker.com → Get Docker
     - Linux (Ubuntu): `sudo apt install docker.io` + add user to docker group
   - Verify: Open terminal → `docker --version` and `docker run hello-world`

   Key concepts:
   | Term       | Meaning                                      | Example                              |
   |------------|----------------------------------------------|--------------------------------------|
   | Image      | Read-only blueprint (like a CD)              | python:3.12-slim                     |
   | Container  | Running instance of image (like CD in player) | Your contact book app running        |
   | Dockerfile | Instructions to build your custom image      | We'll write one today                |
   | Volume     | Persistent data (like saving contacts)        | Map host folder to container         |

   First hands-on:
   ```bash
   # Run official Python image interactively
   docker run -it python:3.12-slim python
   # Inside container:
   >>> print("Hello from Docker container!")
   >>> exit()
   ```

   Show `docker ps` (running containers), `docker ps -a` (all), `docker images`.

4. **Writing Your First Dockerfile**  
   Create a simple project folder: `docker_contact_book`

   **File: Dockerfile**
   ```dockerfile
   # Use official slim Python image (small size)
   FROM python:3.12-slim
   
   # Set working directory inside container
   WORKDIR /app
   
   # Copy requirements first (for caching)
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   
   # Copy your code
   COPY . .
   
   # Expose port if web app (later)
   # EXPOSE 5000
   
   # Command to run your app
   CMD ["python", "main.py"]
   ```

   **File: requirements.txt** (empty for now, or add if you use external libs later)
   ```
   # Leave empty for pure stdlib projects
   ```

   **Build and run:**
   ```bash
   docker build -t my-contact-book:latest .
   docker run --rm my-contact-book:latest
   ```

   Show how it runs your app inside isolated container.

5. **Making It Interactive + Volumes for Persistence**  

   For interactive apps (like our contact book menu):
   ```bash
   docker run -it --rm my-contact-book:latest
   ```

   For persistent data (contacts.json):
   ```bash
   # Map host folder to container /app/data
   docker run -it --rm -v "$(pwd)/data:/app/data" my-contact-book:latest
   ```
   - Changes to contacts.json survive container restart!

6. **Live Project: Fully Dockerize OOP Contact Book**  
   Use your refactored OOP contact book from previous days.

   Folder structure:
   ```
   docker_contact_book/
   ├── main.py
   ├── contact_manager/          # your package
   │   ├── __init__.py
   │   ├── contact.py
   │   ├── storage.py
   │   └── ...
   ├── data/
   │   └── contacts.json (will be created)
   ├── requirements.txt          # empty or add re if needed
   └── Dockerfile
   ```

   Update Dockerfile as above.

   Live demo:
   - Build image
   - Run container interactively
   - Add contacts → exit → run again → contacts still there (thanks to volume)
   - Show `docker ps`, logs, etc.

   Bonus: Multi-stage or smaller image tip (use `python:3.12-alpine` for even smaller size).

#### Common Issues & Fixes
- Permission errors on volumes (Linux): Use `--user $(id -u):$(id -g)`
- Docker Desktop not starting (Windows/Mac): Enable virtualization in BIOS
- "port already in use": Use different host port mapping `-p 5000:5000`
- Build cache: Docker caches layers – change requirements only when needed

#### Homework for Day 18
1. Install Docker and run hello-world + official Python container.
2. Dockerize your best project so far:
   - Either OOP Contact Book (with persistence) OR Cricket Match Simulator.
   - Write proper Dockerfile.
   - Use volume for data persistence.
   - Bonus: Add a README.md with docker commands.
3. Bonus Project: Dockerize a simple agent script:
   - Create a script that prints "Agent running in container!" every 10 seconds.
   - Run it detached: `docker run -d ...`
   - Check logs: `docker logs <container_id>`
4. Comment “Day 18 Done ✅” with screenshot of:
   - `docker images` showing your image
   - Running container with your app output
   - Persistent data proof (contacts survive restart)
5. (Advanced Bonus): Write docker-compose.yml for two containers (e.g., app + fake database later).
