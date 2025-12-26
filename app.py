# Day 2: Goal Tracker Agent (Rule-Based)
print("🤖 Welcome to your Personal Agentic Goal Tracker!")
print("This is a simple rule-based agent that will help you track daily goals.\n")

name = input("What's your name? ")
print(f"\nHello {name}! I'm your AI assistant for the next 100 days.\n")

goals = []
print("Tell me up to 3 goals you want to achieve (type 'done' when finished):")

while len(goals) < 3:
    goal = input(f"Goal {len(goals)+1}: ").strip()
    if goal.lower() == 'done':
        break
    if goal:
        goals.append(goal)

print("\n🎯 Your Goals for Today:")
for i, goal in enumerate(goals, 1):
    print(f"   {i}. {goal}")

if goals:
    print("\n💡 Agent Advice:")
    print("   - Break big goals into small steps")
    print("   - Do the hardest task first")
    print("   - Review progress at night")
    print(f"\n{name}, I'll help you automate reminders soon using real Agentic AI!")
else:
    print("\nNo goals entered? Start small tomorrow – consistency is key!")

print("\nSee you tomorrow for more Python basics!")