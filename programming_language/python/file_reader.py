with open('pi_digits.txt') as file_object:
    contents = file_object.read() # you can use relative paths
print(contents)

with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line)

with open('pi_digits.txt') as file_object:
    lines = file_object.readlines() # get the lines on a list

for line in lines:
    print(line)