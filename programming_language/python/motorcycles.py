# Changing, Adding and Removing Elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Modifying
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding at the end of the list (Append)
motorcycles.append('honda')
print(motorcycles)

# Insert element in an specific index
motorcycles.insert(0, 'suhoya')
print(motorcycles)

# Removing elements
del motorcycles[0]
print(motorcycles)

# Manipulating the removed item
popped_item = motorcycles.pop() # Remove the last item of the list
# .pop(index) Poppes any element on that index
print(popped_item)
print(motorcycles)
# We may achieve the same
popped_item = motorcycles[-1]
del motorcycles[-1]
print(popped_item)
print(motorcycles)

# removing item by its value (like a dictory)
motorcycles.remove('ducati') # remove the first ocurrence
print(motorcycles)
