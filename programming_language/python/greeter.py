def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

def describe_pet(animal_type, pet_name="Willie"): # Default arguments always at the end
    """Display information about a pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('hamster', 'harry') # Positional arguments. The order matters
describe_pet(pet_name='harry', animal_type='hamster') # Keyword arguments.
describe_pet('dog')

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infitie loop
exit_command = 'Y'
while exit_command == 'Y':
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")
    exit_command = input("\nDo you want to continue? y/N") or 'N'
    exit_command = exit_command.upper()