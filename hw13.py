def shutdown(user_input):
    # Check if the user wants to shut down
    if user_input == "Yes":
        print("shutting down")
    # Check if the user wants to cancel
    elif user_input == "no":
        print("abort shut down")
    # Handle any other unexpected input
    else:
        print("sorry")

# --- Testing the function ---
# You can call the function with different arguments to see how it works:
shutdown("Yes")   # Output: shutting down
shutdown("no")    # Output: abort shut down
shutdown("Maybe") # Output: sorry