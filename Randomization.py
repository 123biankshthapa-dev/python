import random

print("🎲 Random Name Picker")
print("=" * 25)


names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace"]

print("Our list of names:", names)
print(f"First name: {names[0]}")
print(f"Last name: {names[-1]}")


random_name = random.choice(names)
print(f"\n Randomly selected: {random_name}")


random.shuffle(names)
print(f"Shuffled list: {names}")