user = {
    'username': 'efermi',
    'another_username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user.items():
    print(f"{key} : {value}")

# Loop through the keys

for name in user.keys():
    print(f"Key: {name}")

print('money' in user.keys())
for value in user.values():
    print(f"Value: {value}")


print(set(user.values()))