#Brittini Bryant
#5/29/19
#Lab 2: Input, Processing & Output


#Prompt user for the charge of the food
food_charge = float(input("Enter amount of money for the food: ")) #This will convert the number entered into a float (so the user can type in 34.88, etc)

#configure tip amount
tip = 20 / 100 #Assumming Tip is 20%
print("Your tip is: ", format(tip, '.0%'))

#configure the sales tax
sales_tax = 8 / 100 #Assuming Tip is 8% aka 80 cents
print("Your sales tax is: " , format(sales_tax, '.0%'))

#total amount
total_amount = food_charge + tip + sales_tax

print("Your total amount is: " , format(total_amount, '.2f'))  
    