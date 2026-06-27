def check_age():
    user_input = input("Please enter your age: ")
    try:
        age = int(user_input)
        
        if age < 0 or age > 125:
            print(f"Error: age {age} is not valid. Please enter a valid age between 0 and 125.")
        else:
            print(f"Age successfully recorded: {age}")   
            if age % 2 == 0:
                print(f"Your age {age} is an even number.")
            else:
                print(f"Your age {age} is an odd number.")

    except ValueError:
        print(f"Error: '{user_input}' is not a valid integer. Please enter a valid age.")

check_age()