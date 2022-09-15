users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    fullname = f"{username['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {fullname.title()}")
    print(f"\tLocation: {location.title()}")