#example 1
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.5
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15
sales_tax = 0.088

customer_one_total = 0
customer_one_itemization = ""
customer_one_tax = 0

customer_one_total += lovely_loveseat_price
customer_one_itemization += "[" + str(lovely_loveseat_price) + "]" + lovely_loveseat_description 

customer_one_total += luxurious_lamp_price
customer_one_itemization += "\n" + "[" + str(luxurious_lamp_price) + "]" + luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax

customer_one_total += customer_one_tax

print("Customer One Items:"
+ "\n"
+ customer_one_itemization
+ "\n\nCustomer One Total:"
+ "\n"
+ str(customer_one_total))

#example 2
import random

name = "Abraham"
question = "Will it rain on Friday?"
answer = ""
random_number = random.randint(1,11)

if question == "":
  print("No question was asked.")
else:

  if random_number == 1:
    answer = "Yes - definitely."
  elif random_number == 2:
    answer = "It is decidedly so."
  elif random_number == 3:
    answer = "Without a doubt."
  elif random_number == 4:
    answer = "Reply hazy, try again."
  elif random_number == 5:
    answer = "Ask again later."
  elif random_number == 6:
    answer = "Better not tell you now."
  elif random_number == 7:
    answer = "My sources say no."
  elif random_number == 8:
    answer = "Outlook not so good."
  elif random_number == 9:
    answer = "Very doubtful."
  elif random_number == 10:
    answer = "Very probable."
  elif random_number == 11:
    answer = "Unlikely."
  else:
    answer = "Error."

  if name == "":
    print("Question: " + question)
    print("Magic 8-Ball's answer: " + answer)
  else:
    print(name + " asks: " + question)
    print("Magic 8-Ball's answer: " + answer)

#example 3
# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)

num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) + " different kinds of pizza!")

pizza_and_prices = [list(a) for a in zip(prices, toppings)]

print(pizza_and_prices)

pizza_and_prices.sort()

cheapest_pizza = pizza_and_prices[0]

priciest_pizza = pizza_and_prices[-1]

pizza_and_prices.pop()

pizza_and_prices.insert(0 ,[2.5 , "peppers"])

three_cheapest = pizza_and_prices[:3]

print(three_cheapest)

#example 4
# Your code below:
import math
single_digits = range(10)

squares = []

for digits in single_digits:
  print(digits)
  squares.append(digits ** 2)

print(squares)

cubes = [digits ** 3 for digits in single_digits]

print(cubes)

#example 5
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#1
total_price = 0

#2
for price in prices:
  total_price += price

#3
average_price = total_price / len(prices)

#4
print("Average Haircut Price: " + str(average_price))

#5
new_prices = [price - 5 for price in prices]

#6
print(new_prices)

#7
total_revenue = 0

#8 & #9
for i in range(len(hairstyles)):
  total_revenue += (prices[i] * last_week[i])

#10
print("Total Revenue: " + str(total_revenue))

#11
average_daily_revenue = total_revenue / 7
print("Average daily Revenue: " + str(average_daily_revenue))

#12
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if prices[i] < 30]

#13
print(cuts_under_30)

#example 6
# Write your code below:

def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + name)

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + "hours")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

# Uncomment these in the last step 
trip_planner_welcome("Abraham")
estimate = estimated_time_rounded(45.88)
destination_setup("Skyrim", "the Hallway of doom", estimate, "Dragon")

#example 7
# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)

def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)

print("The GE train suppliers " + str(train_force) + " Newtons of force.")

def get_energy(mass, c=3*10**8):
  return mass * c ** 2

bomb_energy = get_energy(bomb_mass)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")

#example 8
