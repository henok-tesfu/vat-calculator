# name = input("Enter your name")

# dailyBudget = 50

# print("Hello "+name+" Your daily budget is :",dailyBudget)

# bcost = input("Enter breakfast cost")
# bcost = float(bcost)
# dailyBudget = dailyBudget - bcost
# print("Your Current balance is :",dailyBudget)


# if dailyBudget > 0: 
#  lcost = input("Enter lunch cost")
#  lcost = float(lcost)
#  dailyBudget = dailyBudget - lcost
#  print("Your Current balance is :",dailyBudget)

  
# if dailyBudget > 0:
#  dcost = input("Enter dinner cost")
#  dcost = float(dcost)
#  dailyBudget = dailyBudget - dcost

# if dailyBudget <= 0:
#  print("You have finished your daily budget")


# Hello TheInputName, 
# your current Cost is: costOfTheDay
#  your breakFast cost: costValue
#  your lunch cost: costValue
#  your dinner cost: costValue
#  your total cost of the day : totalCost



# Question 1: Make a prompt for the user to enter their name then ask them the hr rate they are paid at work.
# the number of hrs they work in a day and the number of days they work in a week. 
# Calculate the total amount they make in a week and print it out to the console.



# Desired Output: Hello TheInputName, Your weekly pay is: totalPay

# name = input("Enter your name")
# hrrt = input("Enter your hourly rate")
# noHr = input("Enter the number of hours you work in a day")
# noDay = input("Enter number of days you work in a week")

# hrrt = float(hrrt)
# noHr = float(noHr)
# noDay = int(noDay)
# while noDay > 7:
#  print("Incorrect number of days please retry")
#  noDay = input("Enter number of days you work in a week")
#  noDay = int(noDay)

# print("Hello "+name +" Your weekly pay is:" ,hrrt * noHr * noDay)

name = input("Hello please enter your name: ")
print("Hello " + name, )
item = input("Please enter the item you used: ")
price = input("Please enter the price of the item: ")
amount = input("Please enter the amount you have used: ")

surcharge = 10
vat = 15
price = float(price)
amount = float(amount)

print("Subcharge amount is 10%")
print("Vat amount is 15%")
print("Your total amount is", price * amount + (price * amount *((surcharge + vat)/100)))
print("hello git")
print("all set and done")