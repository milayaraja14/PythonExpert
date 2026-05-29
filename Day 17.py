# Day 17: Exception Handling Example
    
    def divide_numbers():
        try:
            # Prompt user for input
            numerator = int(input("Enter a number to divide: "))
            denominator = int(input("Enter a number to divide by: "))
            
            # This will raise ZeroDivisionError if denominator is 0
            # or ValueError if input is not an integer
            result = numerator / denominator
            
        except ValueError:
            # Runs if the user types something that isn't an integer
            print("Error: Please enter valid whole numbers.")
            
        except ZeroDivisionError:
            # Runs if the user tries to divide by zero
            print("Error: You cannot divide by zero!")
            
        except Exception as e:
            # Catch-all for any other unexpected errors
            print(f"An unexpected error occurred: {e}")
            
        else:
            # Runs only if the try block was successful
            print(f"Success! The result is: {result}")
            
        finally:
            # Runs every single time, regardless of errors
            print("Thank you for using the divider program.")
    
    # Execute the function
    divide_numbers()

# Handling File Errors

    try:
        # Attempt to open a file that might not exist
        with open("secret_data.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Oops! The file 'secret_data.txt' was not found.")
