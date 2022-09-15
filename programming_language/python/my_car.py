from electric_car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
print(f"The odometer reading is {my_new_car.odometer_reading}")
my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_new_car.fill_gas_tank()