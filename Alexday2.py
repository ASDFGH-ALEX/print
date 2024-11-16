'''
Author:Alex
Date:13-11-2024
Description:The input() function allows you to take input from the user.
 It always returns the input as a string, so you’ll need to convert it to the appropriate data type
 (like int or float)if you want to perform arithmetic with it.
'''
number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))
Sum = number1+number2
Difference = number1-number2
Product = number1*number2
Quotient = number1/number2
print("sum:",Sum)
print("Difference:",Difference)
print("Product:",Product)
print("Quotient:",Quotient)