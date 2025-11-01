
print(" Personal Info Formatter")
print("=" * 30)


name = input("Your name: ")
age = int(input("Your age: "))
height = float(input("Your height in meters: "))


formatted_name = name.strip().title()
next_year = age + 1
height_cm = height * 100


print(f"\n Your Formatted Info:")
print(f"Name: {formatted_name.upper()}")
print(f"Age: {age} (you'll be {next_year} next year!)")
print(f"Height: {height}m ({height_cm:.0f} cm)")


message = f"hello {formatted_name}"
print(f"\n String play: '{message}' -> '{message.upper()}'")
print(f"Name length: {len(formatted_name)} characters")

print("\n Info formatted successfully!")