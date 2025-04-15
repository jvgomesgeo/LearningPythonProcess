# Exception = An event that iterrupts the flow of a program
#              (ZeroDivisionError, TypeError, ValueError)
#               1. try; 2. except Exception; 3. finally



# TypeError = int(i) + string => 1 + '1' => TypeError sum between a int and a string
# ZeroDivisionError = 1/0 division per 0
# ValueError = int("Victor") int operator with a string

# Structure => 1. try; 2. except Exception; 3. finally

try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError: 
    print(f"You can't divide by zero IDIOT !")
    
except ValueError:
    print("Enter only numbers please! ")

except TypeError:
    print("You can't use a string")

finally:
    print("Do some cleanup here")