#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Exercise 4: Variables And Names

cars = 100                  # assign teh value 100 for the varibal, cars
space_in_a_car = 4.0        # assign the value 4.0 for the variable, space_in_a_car
drivers = 30                # assign the value 30 for the variable, drivers
passengers = 90             # assign the value 90 for the varibale, passngers
cars_not_driven = cars - drivers    
                            # calculate the number of cars without drivers
cars_driven = drivers       # calculate the number of cars with driver
carpool_capacity = cars_driven * space_in_a_car 
                            # the available space for all driven cars
average_passengers_per_car = passengers / cars_driven
                            # calculate the average passangers in driven cars


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

"""
Study Drills
1. I used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4?
2. Remember that 4.0 is a floating point number. It's just a number with a decimal 
    point, and you need 4.0 instead of just 4 so that it is floating point.
3. Write comments above each of the variable assignments.
4. Make sure you know what = is called (equals) and that it's making names for things.
5. Remember that _ is an underscore character.
6. Try running python from the Terminal as a calculator like you did before and use 
    variable names to do your calculations. Popular variable names are also i, x, and j.
"""