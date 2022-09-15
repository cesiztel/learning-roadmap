def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info['first_name'] = first
    user_info['second_name'] = last

    return user_info

# ** creates a dictionary with all the key-pair values associate to it
user_profile = build_profile('albert', 
                            'einstein',
                            location='princeton',
                            fields='physics')
print(user_profile)