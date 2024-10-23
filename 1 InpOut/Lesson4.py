num = input("Please input a whole number: ") 
num = int(num) 
num2 = num / 6
print("When", num, " is divided by 6", "the result is:", num2)

# PREDICT
# This code will print; Please input a whole number:  and then await an input from the user.
# Once an input is given the code will print: When [num] is divided by 6 the result is: [num2] 
# The variable num2 will be calculated based on the user's input of num

# RUN
# It ran as expected.

# INSPECT
# The code stopped executing once there was no more input to give and all calculations had been printed. The calculation was accurate to what I test on a calculator.

# MODIFY
num = input("Please input a whole number: ") 
num = int(num) 
num2 = input("Please input a whole number that is not zero: ") 
num2 = int(num2)
num3 = num/num2
print("When", num, "is divided by", num2, "the result is:", num3)

# It is necessary to specify that num2 should not be zero, because anything divided by zero is undefined and would crash the code.
