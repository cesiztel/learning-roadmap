alien_0 = {
    'color': 'green',
    'points': 5 
}

print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0['position'] = {
    'x': 0,
    'y': 25
}

print(alien_0)

# Python 3.7 retain the order in which they were defined

# Starting with empty diccionary

alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 5

print(alien_1)

# Small program with indices
alien_0 = { 'x_position': 0, 'y_position': 25, 'speed': 'medium' }
print(f"Original x-position: {alien_0['x_position']}")

# Move the alien to the right
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alient
    x_increment = 3

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New x-position: {alien_0['x_position']}")

# Removing keys
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

print(alien_0.get('points'))
if alien_0.get('points') is None: # Use always is
    print("No point value assigned")
