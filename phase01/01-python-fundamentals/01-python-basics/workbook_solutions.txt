# ==============================================================================
# AUTOMATE THE BORING STUFF WITH PYTHON - CHAPTER 1 WORKBOOK SOLUTIONS
# ==============================================================================

# ------------------------------------------------------------------------------
# Entering Expressions into the Interactive Shell
# ------------------------------------------------------------------------------
#Match the names for questions 1 through 7 to these math operators:
#+  -  *  /  **  //  %
#1. Division            /
#2. Multiplication      *
#3. Subtraction         -
#4. Modulo              %
#5. Addition            +
#6. Exponentiation      **
#7. Floor division      //

#8. Is there a difference in how Python interprets these two expressions?
#   2 + 2 and 2        + 2
print(2 + 2)
print(2       + 2)
#-> No, there is no difference in how Python interprets these two expressions. Both will yield the same result of 4.

#9. If the expression 26 / 8 evaluates to 3.25, what does the expression 26 // 8 evaluate to?
print(26 // 8) 
#-> 3

#10. 26 divided by 8 is 3 with a remainder of 2. What does the expression 26 % 8 evaluate to
print(26 % 8)
#-> 2

#11. Write the expression that adds the numbers 1 to 10.
print(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)
#Which of the two operators in the following expressions is evaluated first according to Python’s order of operation rules?
#12. (4 + 5) * 6
#-> The parentheses operator is evaluated first 

#13. 2 ** 3 + 1
#-> The exponentiation operator is evaluated first

#14. 1 + 2 ** 3#
#-> The exponentiation operator is evaluated first

#15. (1 + 2) ** 3
#-> The parentheses operator is evaluated first
#16. 2 + 4 + 6
#-> The addition operators on the left (2 + 4) are evaluated first, then the result is added to 6.      

#Which of the following expressions produce errors? (You can enter them into the interactive shell to check.)
#17. 2 + 
#18. 42
#19. ((3 + 1) * 2) 
#20. ((3 + 1 * 2)
#21. (0)
#22. 1 + 2 3
#-> The result is 17, 20, 21, 22

#Label the data types of the values in questions 23 through 29 as either int, float, or string.
#23. 2              -> int
#24. -2             -> int
#25. 2.0            -> float
#26. 'hello'        -> string
#27. 2.2            -> float
#28. '2'            -> string
#29. '2.2'          -> string
#30. What is the difference between the values 10, 10.0, and '10'?
#-> 10 is an integer (int), 10.0 is a floating-point number (float), and '10' is a string (str). The integer represents whole numbers, the float represents decimal numbers, and the string represents text.

#When the + operator combines two string values, it joins the strings as the string concatenation operator. When the * operator is used on one string value and one integer value, it becomes the string replication operator. What do the following expressions evaluate to?
#31. 'Hello' + 'Hello' + 'Hello'    -> 'HelloHelloHello'
#32. 'Hello' * 3                    -> 'HelloHelloHello'
#33. 3 * 'Hello'                    -> 'HelloHelloHello'
#34. (2 * 2) * 'Hello'              -> 'HelloHelloHelloHello'
#35. '13' + '12'                    -> '1312'

#Which of the following expressions produce errors?
#36. 'Forgot the closing quote     
#37. 'Hello' * 3.0
#38. 'Hello' + 3
#39. Hello + Hello + Hello
#40. 'Alice' * 'Bob'
#41. 'Hello' / 5
#42. 'Hello' / 'Hello'
#-> The result is 36, 37, 38, 39, 40, 41, 42

#The following programs store values in variables. Determine what each program outputs.
#43.
#nephew = 'Jack'
#print(nephew)
#44.
#nephew = 'Jack'
#print('nephew')
#45.
#nephew = 'Jack'
#nephew = 'Albert'
#print(nephew)
#46.
#nephew = 'Jack'
#Nephew = 'Albert'
#print(nephew)
#-> The result is 'Jack', 'nephew', 'Albert', 'Jack'

#Why do the following programs cause an error?
#47.
#nephew = Jack
#print(nephew)
#-> Because Jack is not placed in quotes, Python treats it as a variable name rather than a string
#48.
#nephew = 'Jack'
#print(Jack)
#-> Because Jack is not defined as a variable
#49.
#nephew = 'Jack'
#print(NEPHEW)
#-> Because NEPHEW is not defined as a variable
#50. print(nephew)
#-> Because nephew is not defined as a variable before this line of code is executed

#Which of the following are valid variable names?
#51. number_of_cats
#52. number-of-cats
#53. numberofcats
#54. numberOfCats
#55. _42
#56. _
#57. 42
#-> The result is 51, 53, 54, 55, 56

#While the interactive shell is good for running Python instructions one at a time, to write entire Python programs you’ll need to enter the instructions into the file editor. Chapter 1 of Automate the Boring Stuff with Python includes a “Hello, world” program that uses comments, the print() and input() functions, and the value and operator concepts from the previous section. To further explore these building blocks of programs, label the following as a variable, function call, or string.
#58. 'hello'
#59. hello
#60. print()
#61. 'print()'
#Do the following expressions cause an error or no error? If they cause no error, what do they evaluate to?
#-> The result is 58, 60, 61 cause no error and evaluate to 'hello', None, 'print()' respectively. 59 causes an error because it is not defined as a variable or function.

#62 int('42')
#63. int('forty two')
#64. int('Hello')
#65. int(-42)
#66. int(3.1415)
#67. float(-42)
#68. str(-42)
#69. str(3.1415)
#70. str('Hello')
#71. str(float(int(3.14)))
#72. str(3)
#73. str(3.0)
#-> The result is 62, 65, 66, 67, 68, 69, 70, 71, 72, 73 cause no error and evaluate to 42, -42, 3.1415, '-42', '3.1415', 'Hello', '3.14', '3', '3.0' respectively. 63 and 64 cause an error because the strings cannot be converted to integers.

#74. Why does this two-line program cause an error?
number_of_cats = 4
print('I have ' + number_of_cats)
#-> Because number_of_cats is an integer and cannot be concatenated with a string

#75. Does round(4.9) evaluate to the integer 5 or the float 5.0?
round(4.9)
#-> round(4.9) evaluates to the integer 5.

#76. Describe what the abs() function returns.
#-> This function returns the absolute value of a number, which is the distance of that number to 0

#77. What does abs(5) return?
#-> returns 5

#78. What does abs(-5) return?
#-> returns 5

#79. Why do computers use the base-2 binary number system instead of the more familiar base-10 decimal system humans use?
#-> Because computers use 0 and 1 to represent data, which is more efficient for their hardware to process. The base-2 binary system allows for simpler and faster computations compared to the base-10 decimal system.

#80. How many bits are in 1 byte?
#-> 8 bits are in 1 byte.

#Determine how many bytes the units in 81 through 84 represent, both as an exponent like 210 and a whole number like 1,024. You can enter an expression like 2 ** 10 into the interactive shell to calculate 210.
#81. Kilobyte -> 1 KB = 1024 bytes
#82. Megabyte -> 1 MB = 1024 KB = 1024 * 1024 bytes = 1,048,576 bytes
#83. Gigabyte -> 1 GB = 1024 MB = 1024 * 1024 KB = 1024 * 1024 * 1024 bytes = 1,073,741,824 bytes
#84. Terabyte -> 1 TB = 1024 GB = 1024 * 1024 MB = 1024 * 1024 * 1024 KB = 1024 * 1024 * 1024 * 1024 bytes = 1,099,511,627,776 bytes
#85. Decimal 2 is 10 in binary. What is decimal 3 in binary? -> 11
#86. Decimal 7 is 111 in binary. What is decimal 8 in binary? -> 1001


