# Write nested conditionals


# 1. Write a program that stores a customer's age and a movie's time in two separate variables. Then calculate the price of a movie ticket based on the following conditions:

# If the age is 12 years old or younger, the ticket price is $5.
# If the age is between 13 and 59 years old and the movie is before 6 PM, the ticket price is $7. After 6 PM, the ticket price is $10.
# If the customer is 60 years old or older, the ticket price is $7.

age = 70
time = 10

if age <= 12:
    price = 5
elif age >= 13 and age <= 59:
    if time < 18:
        price = 7
    else:
        price = 10
elif age >= 60:
    price = 7

# print(f"Ticket price: ${price}")
    

# 2. Write a program to store the type of book (regular, reference, or special collection) and the number of days its overdue. Then calculate the fine amount based on the following conditions:

# If the book is a regular book and overdue by up to 7 days, the fine is $1 per day.
# If the book is a regular book and overdue by more than 7 days, the fine is $2 per day.
# If the book is a reference book, there is no fine, regardless of the number of days overdue.
# If the book is a special collection book, the fine is $5 per day, regardless of the number of days overdue.

book_type = "special collection"
days_overdue = 10

if book_type == "regular":
    if days_overdue <= 7:
        fine_amount = 1 * days_overdue
    elif days_overdue > 7:
        fine_amount = 2 * days_overdue
elif book_type == "reference":
    fine_amount = 0
elif book_type == "special collection":
    fine_amount = 5 * days_overdue

# print(f"Fine amount ${fine_amount}")


# 3. Write a program that stores a person's order value and membership level (regular or premium). Then calculate a discount amount based on the following conditions:

# If the total order value is less than $50, there is no discount.
# If the total order value is between $50 and $100, the discount is 5% for regular customers and 10% for premium customers.
# If the total order value is greater than $100, the discount is 10% for regular customers and 15% for premium customers.

order_value = 1000
membership = "premium"

if order_value < 50:
    discount = 0
elif order_value >= 50 and order_value <= 100:
    if membership == "regular":
        discount = 0.05
    elif membership == "premium":
        discount = 0.1
elif order_value > 100:
    if membership == "regular":
        discount = 0.1
    elif membership == "premium":
        discount = 0.15

# print(f"Discount: ${order_value * discount}")


# 4. Write a Ruby program that stores the weight of a package and the destination (domestic or international). Then calculate the shipping fee based on the following conditions:

# If the destination is domestic:
# If the weight is less than or equal to 1 kg, the shipping fee is $5.
# If the weight is greater than 1 kg, the shipping fee is $10.
# If the destination is an international shipment:
# If the weight is less than or equal to 1 kg, the shipping fee is $15.
# If the weight is greater than 1 kg, the shipping fee is $25.

destination = "international"
weight = 30

if destination == "domestic":
    if weight <= 1:
        shipping_fee = 5
    else:
        shipping_fee = 10
elif destination == "international":
    if weight <= 1:
        shipping_fee = 15
    else:
        shipping_fee = 25

# print(f"Shipping Fee: ${shipping_fee}")
