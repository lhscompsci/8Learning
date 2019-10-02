#  What is an octothorpe?
# <- This is an octothorpe.
#  What is the octothorpe used for in python?
# Notes, also known in the programming community as Comments

print("hello world.")
print("howdy, y'all!")
print("I like typing this.")
print("Printing....Yay!!!")

# Practice with Maths and things
print("I will now count my chickens.")
print("Hens", 25 + 30 / 6)
print("Roosters: ", 100 - 25 * 3 % 4)
print("Now, I will count the eggs:")
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
print("Is it true that 3 + 2 < 5 - 7?")
print(3 + 2 < 5 - 7)


# variables
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers/cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")