# Developed by Arya C. Murray
# Date: January 25th, 2022
# Desc: A Program in order to recommend for for a party based on preferences. Also calculates cost for participants.
# DISCLAIMER: Program assumes that user knows the program syntax.



#Establishing number of dinner invitees and assigning to variable
#valid input is assumed for these integer values


print("Please enter the number of invitees:")
invitees = int(input())


#loop over the number of invitees to attain their preferences

food_choices = [] #initialize the chosen foods list.


for i in range(invitees):
    print("Please enter the order details for invitee Number",i+1,"/", invitees)

#store preferenes in boolean variables named after preference types within loop

    print("Do you want a keto friendly meal?")
    if input() == "y" or "yes":
        keto = True
    else:
        keto = False
    print("Do you want a vegan meal?")
    if input() == "y" or "yes":
        vegan = True
    else:
        vegan = False
    print("Do you want a Gluten-free meal?")
    if input() == "y" or "yes":
        gf = True
    else:
        gf = False

    #Make reccomendations for food based on preferences !!
    # food_choices = [] #initialize the chosen foods list.
    cost = 0 #initialize the cost variable 
    if (keto == False and vegan == False and gf == False):
        choice = input("Would you like 'Pizza', 'Pasta', 'Falafel', 'Steak' or just a 'Beverage'?:")
        if choice == "Pizza":
            cost = cost + 44.50
            food_choices.append("Pizza")
        elif choice == "Pasta":
            cost = cost + 48.99
            food_choices.append("Pasta")
        elif choice == "Falafel":
            cost = cost + 52.99
            food_choices.append("Falafel")
        elif choice == "Steak":
            cost = cost + 49.60
            food_choices.append("Steak")
        elif choice == "Beverage":
            cost = cost + 5.99
            food_choices.append("Beverage")
        else:
            print("Invalid Input, Restarting.")
            continue
    elif keto == False and vegan == False and gf == True:
        choice = input("Would you like 'Falafel', 'Steak' or just a 'Beverage'?:")
        if choice == "Falafel":
            cost = cost + 52.99
            food_choices.append("Falafel")
        elif choice == "Steak":
            cost = cost + 49.60
            food_choices.append("Steak")
        elif choice == "Beverage":
            ccost = cost + 5.99
            food_choices.append("Beverage")
    elif keto == False and vegan == True and gf == False:
        choice = input("Would you like 'Pizza', 'Pasta', 'Falafel', just a 'Beverage'?:")
        if choice == "Pizza":
            cost = cost + 44.50
            food_choices.append("Pizza")
        elif choice == "Pasta":
            cost = cost + 48.99
            food_choices.append("Pasta")
        elif choice == "Falafel":
            cost = cost + 52.99
            food_choices.append("Falafel")
        elif choice == "Beverage":
            cost = cost + 5.99
            food_choices.append("Beverage")
    elif keto == True and vegan == False and gf == False:
        choice = input("Would you like 'Pizza', 'Falafel', 'Steak' or just a 'Beverage'?:")
        if choice == "Pizza":
            cost = cost + 44.50
            food_choices.append("Pizza")
        elif choice == "Falafel":
            cost = cost + 52.99
            food_choices.append("Falafel")
        elif choice == "Steak":
            cost = cost + 49.60
            food_choices.append("Steak")
        elif choice == "Beverage":
            cost = cost + 5.99
            food_choices.append("Beverage")
    elif keto == True and vegan == True and gf == False:
        choice = input("Would you like 'Pizza', 'Falafel', or just a 'Beverage'?:")
        if choice == "Pizza":
            cost = cost + 44.50
            food_choices.append("Pizza")
        elif choice == "Falafel":
            cost = cost + 52.99
            food_choices.append("Falafel")
        elif choice == "Beverage":
            cost = cost + 5.99
            food_choices.append("Beverage")
    elif keto == False and vegan == True and gf == True:
        choice = input("Would you like 'Falafel', or just a 'Beverage'?:")
        if choice == "Falafel":
            cost = cost + 52.99
            food_choices.append("Falafel")
        elif choice == "Beverage":
            cost = cost + 5.99
            food_choices.append("Beverage")
    elif keto == True and vegan == False and gf == True:
        choice = input("Would you like 'Falafel', 'Steak' or just a 'Beverage'?:")
        if choice == "Falafel":
            cost = cost + 52.99
            food_choices.append("Falafel")
        elif choice == "Steak":
            cost = cost + 49.60
            food_choices.append("Steak")
        elif choice == "Beverage":
            cost = cost + 5.99
            food_choices.append("Beverage")
    elif keto == True and vegan == True and gf == True:
        choice = input("Would you like 'Falafel', or just a 'Beverage'?:")
        if choice == "Falafel":
            cost = cost + 52.99
            food_choices.append("Falafel")
        elif choice == "Beverage":
            cost = cost + 5.99
            food_choices.append("Beverage")
    else:
        print("you've entered an invalid value, please restart the program")
        continue

# Report to the user the orders that they have chosen
print("You have X invitees with the following orders:")
print(food_choices.count("Pizza"), 'invitees ordered Pizza. The cost is:$%d ' % (food_choices.count("Pizza")* 44.50 ))
print(food_choices.count("Pasta"), 'invitees ordered Pasta. The cost is:$%d ' % (food_choices.count("Pasta")* 48.99 ))
print(food_choices.count("Falafel"), 'invitees ordered Falafel. The cost is:$%d' % (food_choices.count("Falafel")* 52.99) )
print(food_choices.count("Steak"), 'invitees ordered Steak. The cost is:$%d ' % (food_choices.count("Steak")* 49.60 ))
print(food_choices.count("Beverage"), 'invitees ordered only Beverage. The cost is:$%d' % (food_choices.count("Beverage")* 49.60) )



print(cost)


