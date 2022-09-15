squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

# Other operations with lists
print(min(squares))
print(max(squares))
print(sum(squares))

# List comprehension
squares = [value**2 for  value in range(1, 11)]
print(squares)