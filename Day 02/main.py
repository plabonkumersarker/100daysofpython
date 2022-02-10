print("Welcome to the tip Calculator!")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
num_of_people = int(input("How many people to split the bill?"))

#Each should pay
each_bill = total_bill/num_of_people
#Each should pay tips
each_tip = ((total_bill/num_of_people)*percentage)/100

#sum of net pay and tips with two decimal number
result = round(each_bill + each_tip,2)

#To make the result with exact 2 decimal point, even it's zero
result = "{:.2f}".format(result)

print(f"Each person should pay: ${result}")