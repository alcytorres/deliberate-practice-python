# Write a loop which modifies a variable each time the loop runs

# 1. Write a while loop to print the numbers 1 through 10.

# num = 1
# while num <= 10:
#     print(num)
#     num += 1


# 2. Write a while loop that prints the word "hello" 5 times.

# count = 1
# while count <= 5:
#     print("hello")
#     count += 1
    

# 3. Write a while loop that asks the user to enter a word and will run forever until the user enters the word "stop".
# #    REVIEW


# while True:
#     word = input("Enter a word: ")
#     if word == "stop":
#         break


# Solution
# while True:             # Starts an infinite loop that keeps running until broken
#     word = input("Enter a word: ")  # Prompts user for input and stores it in 'word' variable
#     if word == "stop":  # Checks if the entered word is exactly "stop"
#         break           # Exits the loop immediately if condition is true


# 4. Write a while loop that prints the numbers 0 through 100, increasing by 5 each time.

# Solution

# num = 0
# while num <= 100:
#     print(num)
#     num += 5


# 5. Write a while loop that prints the number 9000 ten times.

# count = 1
# while count <= 10:
#     print(9000)
#     count += 1


# 6. Write a while loop that asks the user to enter a number and will run forever until the user enters a number greater than 10.

# while True:
#     num = input("Enter a number: ")
#     if int(num) > 10:
#         break


# Solution
# while True:                # Infinite loop runs until stopped
#     num = input("Enter a number: ")  # Asks user for input, stores it as a string in 'num'
#     if int(num) > 10:      # Converts 'num' to integer, checks if it’s greater than 10
#         break              # Stops the loop if the number is > 10


# 7. Write a while loop that prints the numbers 50 to 70.

# num = 50
# while num <= 70:
#     print(num)
#     num += 1


# 8. Write a while loop that prints the phrase "Around the world" 144 times.

# count = 1
# while count <= 144:
#     print("Around the world")
#     count += 1


# 9. Write a while loop that asks the user to enter a word and will run forever until the user enters a word with more than 5 letters.

# while True:
#     word = input("Enter a word: ")
#     if len(word) > 5:
#         break


# 10. Write a while loop that prints the even numbers from 2 to 40.

# num = 2 
# while num <= 40:
#     print(num)
#     num += 2


