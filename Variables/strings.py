# Title, this prints out "Flamy At Python"
name = "flamy at python"
print(name.title()) 


# Lowercase and Uppercase
print(name.lower())
print(name.upper())

print("1 ===")

# Using the f-strings as a variable
first_name = "flamy"
last_name = "python"
full_name = f"{first_name} {last_name}"
print(full_name)

# using f-string to compose complete messages
first_name = "flamy"
last_name = "python"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

print('2 ===')

first_name = "flamy"
last_name = "python"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}"
print(message)

print('3 ===')

# Pythons whitespace tabs
print("\tPython")

# New Line
print("Languages:\nPython\nJavaScript")

# Combine new Lines and Tabs:
print("Langauges:\n\tPython\n\tbash\n\tJavaScript")

# Removing whitespaces (rstrip() removes spaces in strings).
# rstrip() right spaces.
# lstrip() left spaces.
# strip() removes both left and right spaces.
favorite_language = "python "
print(favorite_language.rstrip())

print('4 ===')

# Removing Prefixes
url = 'https://google.com'
print(url.removeprefix('https://'))








