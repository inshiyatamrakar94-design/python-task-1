
    # Get inputs
val1 = input("Enter first number: ")
val2 = input("Enter second number: ")

    # Convert to integers
num1 = int(val1)
num2 = int(val2)

    # Perform calculations
total = num1 + num2
diff = num1 - num2
    prod = num1 * num2

    # Print clean summary using f-strings
    print(f"\n--- Results for {num1} and {num2} ---")
    print(f"The sum is: {total}")
    print(f"The difference is: {diff}")
    print(f"The product is: {prod}")

except ValueError:
    # This runs if the user types letters instead of numbers
    print("Error: Please enter valid whole numbers only!")

except Exception as e:
    # This catches any other unexpected issues
    print(f"An unexpected error occurred: {e}")
