cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# innequality
requested_topping = 'mushrooms'
if requested_topping != 'anchoives':
    print("Hold the anchovies!")

# innequality with numbers
answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

# and or
age_1 = 22
age_2 = 45
if age_1 >= 21 and age_2 < 32:
    print("Your age is in the expected range!")

if age_1 >= 21 or age_2 < 32:
    print("Your age might be on expected range!")

# Use conditional to validate in lists
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print('The pizza will include mushrooms')
if 'pepperony' in requested_toppings:
    print('The pizza will include pepperony')

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish")

# check that list is not empty
requested_topping = []

if requested_topping:
    print("List is full of requirements")
else:
    print("Pizza does not have requested toppings")
# pretty sick! You can in one line cross-validate elements
# from different lists
available_toppings = ['mushrooms', 'olives', 'green peppers',
    'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

# Conditional statements: else and elif
age = 42

if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $25")
else:
    print("Your admission cost is $40")