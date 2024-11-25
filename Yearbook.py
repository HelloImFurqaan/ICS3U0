"""
Furqaan Mohammed 752879
Date: 8 November, 2024
Course: ICS3U0-Introduction to Computer Science
Title: School Yearbook
Description: A program that calculates the minimum perimeter and dimension for a given amount of yearbook photos to be displayed.

VARIABLE DICTIONARY:
  N           (int)   The number of photographs to be laid out in a rectangle.
  fac         (list)  A list of factors of the input number `N`.
  Max         (int)   The largest possible factor to check, calculated as the square root of `N`.
  x           (int)   One dimension of the rectangle, chosen as the largest factor of `N`.
  y           (float) The other dimension of the rectangle, calculated as `N / x`.
  P           (float) The calculated perimeter of the rectangle.
  photos      (str)   The user input, which is either a positive integer or the string "done".
  done        (bool)  A flag indicating whether the user has terminated the program.
"""

import math  # Importing math

def factors(N):
    """
    Finds all factors of the input number N up to its square root.
    
    Parameters:
    N (int): The number for which factors are calculated.

    Returns:
    list: A list of factors of N.
    """
    fac = []  # Epty list to store factors
    if N > 0:  # Ensure N is positive
        Max = math.floor(math.sqrt(N))  # Calculate the largest factor to check
        for x in range(1, Max + 1):  # Iterate through potential factors
            if N % x == 0:  # Check if x is a factor
                fac.append(x)  # Add x to the list of factors
    elif N >= 0:  # If N is 0 or negative, return itself
        fac.append(N)
    return fac  # Return the list of factors

def perimeter(N):
    """
    Calculates the minimum perimeter of a rectangle that fits N photographs.

    Parameters:
    N (int): The number of photographs.

    Returns:
    str: A formatted string describing the minimum perimeter and dimensions.
    """
    fac = factors(N)  # Get the list of factors of N
    x = fac[-1]  # The largest factor is x
    y = N / x  # Calculate y
    P = 2 * (x + y)  # Calculate the perimeter of the rectangle
    return ("Minimum perimeter is %d with dimensions: %d x %d."
            % (P, x, y))  # Return the result as a formatted string

# Welcome message for the user
print("Welcome to the school yearbook program!")

done = False  # Initialize done as False

# Main loop to repeatedly prompt the user for input
while done != True:
    print()  # Formatting
    photos = input("Please input your number of photographs:")  # Get user input
    
    # Check if the user is done
    if photos.lower() == "done":
        print("Goodbye!")  # Print a farewell message
        done = True  # Set done to True
        break  # Exit the loop
    
    try:
        photos = int(photos)  # Attempt to convert the input to an integer
        if photos <= 0:  # Check if the input is a valid positive integer
            print("%d is not a valid number of photos. Please enter a positive number." % photos)
        else:
            print(perimeter(photos))  # Calculate and display the perimeter
    except:
        # Handle invalid inputs that cannot be converted to an integer
        print("Please enter a positive number.")        
