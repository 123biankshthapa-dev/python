

print(" Shopping List Manager")
print("=" * 25)

shopping_list = ["milk", "bread", "eggs", "apples", "cheese"]

print("My shopping list:")
for item in shopping_list:
    print(f"☐ {item}")



print("\nChecking off items:")
purchased = ["milk", "bread"]

for item in shopping_list:
    if item in purchased:
        print(f"✅ {item} - Purchased!")
    else:
        print(f"☐ {item} - Still needed")



print("\nNumbered shopping list:")
for i in range(len(shopping_list)):
    print(f"{i + 1}. {shopping_list[i]}")