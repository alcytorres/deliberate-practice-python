# Write a custom method with valid syntax

# 1. Write a method that takes in a number and returns the number times two. Then run the method and print the result.

def get_double(num):
    return num * 2

# print(get_double(10))


# Solutions
# number = 10
# print(get_double(number))

# number = get_double(10)
# print(number)


# 2. Write a method that takes in a string and returns the string with all capital letters. Then run the method and print the result.

def make_upcase(string):
    return string.upper()

# print(make_upcase("sky"))


# 3. Write a method that takes in two numbers and returns the first number subtracted by the second. Then run the method and print the result.

def get_difference(num1, num2):
    return num1 - num2

# print(get_difference(10, 4))


# 4. Write a method that takes in a number and returns the number times itself. Then run the method and print the result.

def square(num):
    return num * num

# print(square(5))


# 5. Write a method that takes in a string and returns the first letter of the string. Then run the method and print the result.

def get_first_letter(string):
    return string[0]    

# print(get_first_letter("fly"))


# 6. Write a method that takes in three strings and returns a string that combines all three strings with spaces in between. Then run the method and print the result.

def string_combiner(s1, s2 , s3):
    return f"{s1} {s2} {s3}"        # Returns a single string with the 3 inputs separated by spaces
# print(string_combiner("the", "cat", "jumped"))


# What Does the f Do?
# The f before the string (e.g., f"{s1} {s2} {s3}") makes it an f-string (short for "formatted string").
# Simply: It lets you put variables (like s1, s2, s3) directly inside the string using {} curly braces.
# The f tells Python to replace {s1}, {s2}, and {s3} with their actual values, and the spaces between them stay as spaces.


# 7. Write a method that takes in a number and returns the number as a string. Then run the method and print the result.

def convert_to_string(num):
    return str(num)

# print(convert_to_string(10))


# 8. Write a method that takes in a string and returns the string repeated 5 times. Then run the method and print the result.

def repeat_strings(string):
    return string * 5

# print(repeat_strings("run"))


# 9. Write a method that takes in 3 numbers and returns the average (the sum divided by 3.0). Then run the method and print the result.

def average(num1, num2, num3):
    return (num1 + num2 + num3) / 3.0

# print(average(5, 10, 15))


# 10. Write a method that takes in a number and returns the number times 10 plus 30. Then run the method and print the result.

def convert_number(num):
    return num * 10 + 30

# print(convert_number(10))
