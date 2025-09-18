
def exceptions():
    try:
        num1=int(input("Enter first number: "))
        num2=int(input("Enter second number: "))
        result=num1/num2
        print(f"{num1} divided by {num2} is {result}")
    except ValueError:
        print("Error! Invalid input. Please enter numeric values.")
    except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Execution completed.")
exceptions()

def multiple_exceptions(): 
    try:
        n = 1
        res = 100 / n
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except exceptions as e:
        print("Enter a valid number!")
    else:
        print("Result is", res)
    finally:
        print("Execution complete.")