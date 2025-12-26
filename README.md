### Day 17: More Design Patterns – Observer, Strategy & Introduction to Dependency Injection

**Live Session Plan (9:30 - 10:30 PST / ~9:30 - 10:30 PM PKT/IST)**  
- **0-5 mins**: Welcome + recap Day 16 + shoutouts to homework (abstract players, @property averages, singleton team managers, factories, logger singletons).  
- **5-25 mins**: Observer Pattern – automatic notifications (e.g., score updates to fans).  
- **25-45 mins**: Strategy Pattern – swappable algorithms (e.g., different batting styles).  
- **45-55 mins**: Dependency Injection (DI) intro – loose coupling for testable agents.  
- **55-60 mins**: Q&A, when to use patterns, homework, teaser for Day 18.

1. **Welcome & Recap**  
   - "Assalam-o-Alaikum everyone! Day 17 – your OOP and design skills are now at an advanced level, mashAllah!  
   - Yesterday abstract classes, @property, dataclasses, Singleton and Factory made everything cleaner and more professional. Incredible upgrades with calculated averages, singleton loggers, player factories – this is how real-world libraries are built!  
   - Today: More powerful Design Patterns – Observer (for notifications), Strategy (for flexible behavior), and Dependency Injection (the secret to testable, maintainable agentic systems). These patterns are used everywhere: Flask/Django extensions, LangChain tools, automation frameworks."

2. **Observer Pattern – “Subscribe and Get Notified”**  
   New folder: `day17_patterns_di`  
   File: `day17_observer_strategy.py`

   - Use case: Live cricket score – when score changes, all subscribers (fans, apps, TV) get updated automatically.

   ```python
   class ScoreBoard:
       def __init__(self):
           self._score = 0
           self._observers = []        # list of observers
       
       def attach(self, observer):
           self._observers.append(observer)
           print(f"{observer.name} subscribed!")
       
       def detach(self, observer):
           self._observers.remove(observer)
           print(f"{observer.name} unsubscribed!")
       
       def notify(self):
           for observer in self._observers:
               observer.update(self._score)
       
       @property
       def score(self):
           return self._score
       
       @score.setter
       def score(self, new_score):
           if new_score != self._score:
               self._score = new_score
               print(f"\n*** Score updated: {self._score} ***")
               self.notify()               # notify all observers
   
   
   class Observer:
       def __init__(self, name):
           self.name = name
       
       def update(self, score):
           pass                            # to be overridden
   
   
   class Fan(Observer):
       def update(self, score):
           print(f"🔔 {self.name}: Pakistan score is now {score}! Go team!")
   
   
   class TVChannel(Observer):
       def update(self, score):
           print(f"📺 {self.name}: Live - Pakistan {score}/? | Exciting match!")
   
   
   class MobileApp(Observer):
       def update(self, score):
           print(f"📱 {self.name} Notification: Current score {score}")
   
   
   # Usage
   scoreboard = ScoreBoard()
   
   fan1 = Fan("Ahmed from Lahore")
   fan2 = Fan("Sara from Karachi")
   geo_news = TVChannel("Geo Super")
   cricbuzz = MobileApp("CricBuzz")
   
   scoreboard.attach(fan1)
   scoreboard.attach(fan2)
   scoreboard.attach(geo_news)
   scoreboard.attach(cricbuzz)
   
   scoreboard.score = 50      # boundary!
   scoreboard.score = 56      # single
   scoreboard.score = 100     # century!
   
   scoreboard.detach(fan2)    # Sara turns off notifications
   scoreboard.score = 150
   ```

3. **Strategy Pattern – Swappable Behavior**  

   - Use case: Different batting strategies (defensive, aggressive, T20 power-hitting).

   ```python
   from abc import ABC, abstractmethod
   
   class BattingStrategy(ABC):
       @abstractmethod
       def play_shot(self, balls_faced):
           pass
   
   
   class Defensive(BattingStrategy):
       def play_shot(self, balls_faced):
           return "Plays defensively – focuses on survival"
   
   
   class Aggressive(BattingStrategy):
       def play_shot(self, balls_faced):
           if balls_faced > 30:
               return "Goes aggressive – looking for boundaries!"
           else:
               return "Builds inning carefully"
   
   
   class T20Power(BattingStrategy):
       def play_shot(self, balls_faced):
           return f"Power hitting! Attempts six – ball #{balls_faced}"
   
   
   class Batsman:
       def __init__(self, name, strategy: BattingStrategy):
           self.name = name
           self.strategy = strategy          # injected strategy
           self.runs = 0
           self.balls = 0
       
       def set_strategy(self, new_strategy: BattingStrategy):
           self.strategy = new_strategy
           print(f"{self.name} changes to {new_strategy.__class__.__name__} mode!")
       
       def face_ball(self):
           self.balls += 1
           action = self.strategy.play_shot(self.balls)
           runs_today = self.balls % 4             # simple simulation
           self.runs += runs_today
           print(f"{self.name}: Ball {self.balls} - {action} (+{runs_today} runs)")
   
   
   # Usage
   rizwan = Batsman("Rizwan", Defensive())
   rizwan.face_ball()
   rizwan.face_ball()
   
   rizwan.set_strategy(Aggressive())
   rizwan.face_ball()
   rizwan.face_ball()
   
   rizwan.set_strategy(T20Power())
   rizwan.face_ball()
   ```

   - Strategy is injected and can be changed at runtime → very flexible.

4. **Dependency Injection (DI) – Loose Coupling for Testable Code**  

   - Problem: Hard-coded dependencies make testing hard.
   - Solution: Pass dependencies from outside.

   ```python
   # Bad – tight coupling
   class AgentBad:
       def __init__(self):
           self.storage = JSONStorage()           # hard-coded
   
   # Good – DI
   class Storage(ABC):
       @abstractmethod
       def save(self, data):
           pass
       
       @abstractmethod
       def load(self):
           pass
   
   
   class JSONStorage(Storage):
       def save(self, data):
           print(f"Saving to JSON: {data}")
       
       def load(self):
           return {"loaded": "data"}
   
   
   class DatabaseStorage(Storage):
       def save(self, data):
           print(f"Saving to DB: {data}")
       
       def load(self):
           return {"from": "database"}
   
   
   class Agent:
       def __init__(self, storage: Storage):      # injected
           self.storage = storage
       
       def remember(self, info):
           self.storage.save(info)
       
       def recall(self):
           return self.storage.load()
   
   
   # Usage – easy to switch or mock for testing
   agent1 = Agent(JSONStorage())
   agent1.remember("My goal for Day 100")
   
   agent2 = Agent(DatabaseStorage())
   agent2.remember("Production deployment")
   ```

   - In testing: Pass a fake MockStorage.
   - This is how LangChain, FastAPI, Django inject services.

#### When to Use These Patterns
- Observer → real-time updates (scores, stock prices, chat apps).  
- Strategy → changeable algorithms (payment methods, AI models).  
- DI → anywhere you want testability and flexibility (almost always in big projects).

#### Homework for Day 17
1. Run all examples – play with observers, strategies, DI.
2. Build a Live Cricket Match Simulator:
   - ScoreBoard with Observer pattern (add Fan, TV, App, and maybe WhatsAppGroup observer).
   - Batsman with Strategy pattern (switch between Defensive/Aggressive based on wickets fallen).
   - Use DI to inject different notifiers or storage.
3. Bonus Project: Simple Chat Agent:
   - Observer for new messages.
   - Strategy for different response styles (formal, casual, Urdu).
   - DI for storage (memory vs file).
4. Comment “Day 17 Done ✅” with screenshot of score updates notifying multiple observers.
5. (Advanced Bonus): Implement a Strategy for different bowling types (fast, spin).
