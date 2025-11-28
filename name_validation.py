user_name = input("Enter your username: ")
if len(user_name) < 5:
    print("Username must be at least 5 characters long.")
elif len(user_name) > 15:
    print("Username can be a maximum of 15 characters long.")
else:
    print("Your username is valid.")

