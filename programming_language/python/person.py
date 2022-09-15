def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person"""
    person = {
        'first': first_name,
        'last': last_name
    }
    if age:
        person['age']  = age
    return person

print(build_person('jimi', 'hendrix'))
print(build_person('camaron', 'de la isla', 34))