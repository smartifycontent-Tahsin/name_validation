try:
    age= 2025- int(input("What is your birth year? "))
    if age>=18:
        print(f"Your age is {age} and you are an adult.")
    else:
        print(f"Your age is {age} and you are a minor.")
except ValueError:
    print("Please enter a valid year!")
