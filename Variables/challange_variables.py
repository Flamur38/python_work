# 2-3 Personal Message 
first_name = "flamy"
print(f"Hello, {first_name} would you like to learn some python?")

print("1 ---")

# 2-4 Name Cases
name = "flamy"
print(f"{name.lower()} \n{name.upper()}\n{name.title()}")

print("2 ---")

# 2-5 Famous Quote
quote = "Albert Einstein once said, \"A person who never made a mistake never tried anything new\""
print(quote)


print("3 ---")

# Famous Quote 2
famous_person = "Albert Einstein"
message = "\"A person who never made a mistake never tried anything new\""
print(f"{famous_person} once said, {message}")


print("4 ---")


# 2-7 Stripping Names:
hes_name = ' flamy '
print(hes_name) # whitespaces are displayed.
print(hes_name.lstrip())
print(hes_name.rstrip())
print(hes_name.strip())
print(f"\t{hes_name.rstrip()} \n{hes_name.lstrip()}")


print("5 ---")


# 2-8 File Extensions:
filename = "python_notes.txt"
print(f"{filename.removesuffix('.txt')}")



