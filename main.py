from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
selling_coffee = True 
while selling_coffee:

    choice = input(f"What would you like to drink? {menu.get_items()}: ")
    
    if choice == 'report':
        #Print report of machine's current resources
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        #Secret codeword to turn coffee machine off 
        selling_coffee = False 
    else:
        #See if the drink they chose is available and retrieve the drink
        drink = menu.find_drink(choice)
        if drink == None: 
            # Menu does not have the chosen drink
            pass
        else: 
            #Check if there are enough resources to make the drink 
            can_make = coffee_maker.is_resource_sufficient(drink)
            if not can_make: 
                pass
            else:
                # Processing the payment 
                payment_enough = money_machine.make_payment(drink.cost)
                if not payment_enough:
                    pass
                else:
                    coffee_maker.make_coffee(drink)
                    
                    
                
                
                
