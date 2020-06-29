# Tea-Coffee Vending Machine (TCVM) is a machine used for making tea and coffee.
# Nowadays tea-coffee machine is a common need of an organization/refreshment stall, where
# one can easily and quickly serve different flavours of tea and coffee drink.
# Here we want a simulator of tea-coffee vending machine. The TCVM should have different
# containers to contain material needed for making tea-coffee.


# ==================================CHLLNGS===================================================================================

# 13. No need to store data permanently, in every start of application system should be reset.
# • Modular Approach should be used in application development
# ◦ Class level
# ◦ Method level
# • Should make use of interface in appropriate situations.
# • Application code should be reusable
# • Application code should be well documented
# • Appropriate names should used for class, interfaces method and variables
# • Small method size
# • Optimized logic
# • User-friendly Interface
# • Accuracy of calculations and Report
# • Timeline delivery
# • Completion status

class coffee_machine:
    def set_machine(self):
        #This is the methode With initionlize the coffee machine basic Complonents
        self.tea_sold=0
        self.coffee_sold=0
        self.btea_sold=0
        self.bcoffee_sold=0
        self.tea_price=10
        self.btea_price=5
        self.coffee_price=15
        self.bcoffee_price=10

    def __str__(self):
        return "tea_sold"+str(self.tea_sold)+"coffee_sold"+str(self.coffee_sold)+"btea_sold"+str(self.btea_sold)+"bcoffee_sold"+str(self.bcoffee_sold)
    #================================================THESE METHODE MAKE CHANGES IN TOTAL NO OF ITEMS SOLD =====================================================================================================================

    def sell_tea(self,cups:int):
        # To add
        self.tea_sold+=cups
    def sell_coffee(self,cups:int):
        self.coffee_sold+=cups
    def sell_btea(self,cups:int):
        self.btea_sold+=cups
    def sell_bcoffee(self,cups:int):
        self.bcoffee_sold+=cups
    #================================================================================================

    def coffee_sale(self)->int:
        #retun to no of coffe have been sold till now
        return self.coffee_sold

    def bcoffee_sale(self)->int:
        # method return total no of Black coffy sold
        return self.bcoffee_sold

    def tea_sale(self)->int:
        #Method return total no of tea sold
        return self.tea_sold


    def btea_sale(self)->int:
        # This method retutn the no of Black tea sold
        return self.btea_sold


    def total_sale(self)->int:
        # This method return a int having tolat sale in term of Price
        return self.coffee_sale()*self.coffee_price + self.bcoffee_sale()*self.bcoffee_price + self.tea_sale()*self.tea_price + self.btea_sale()*self.btea_price

    
    def set_price(self,*args):
        #This methode would be implemented for Dynamic priceing instaed of hard coded
        pass

        

        
class container(coffee_machine):
    # 1. System should have containers with their maximum capacity.

    # 9. System required below containers:
    # SR Container Max Capacity
    # 1 Tea Container 2 KG
    # 2 Coffee Container 2 KG
    # 3 Sugar Container 8 KG
    # 4 Water Container 15 Litters
    # 5 Milk Container 10 Litters


    def fill(self):
        self.tea=2
        self.coffee=2
        self.sugar=8
        self.water=15
        self.milk=10
        

    def container_status(self):
        return "tea"+str(self.tea)+"coffee"+str(self.coffee)+"sugar"+str(self.sugar)+"water"+str(self.water)+"milk"+str(self.milk)

    # Use of Material in drink making
    def use_tea(self,quantity:float)->bool:
        print(quantity)
        if(quantity<=self.tea):
            print(self.tea)
            self.tea-=quantity
            return True
    def use_coffee(self,quantity:float)->bool:
        if(quantity<=self.coffee):
            self.coffee-=quantity
            return True
    def use_sugar(self,quantity:float)->bool:
        if(quantity<=self.sugar):
            self.sugar-=quantity
            return True
    def use_water(self,quantity:float)->bool:
        if(quantity<=self.water):
            self.water-=quantity
            return True
    def use_milk(self,quantity:float)->bool:
        if(quantity<=self.milk):
            self.milk-=quantity
            return True


class maker(container):

    def __init__(self):
        # System should be started with assumption that all containers are filled with material needed for making drink.
        self.fill()
        self.set_machine()
        # pass
    def make_tea(self,cups:int):

        tea=(5/1000)*cups
        water=(60/1000)*cups
        milk=(40/1000)*cups
        sugar=(15/1000)*cups

        # 4. System should care of overflow and underflow condition of containers
        # 5. System should not allow drink making in underflow condition(no enough material available)

        if(self.use_tea(tea) and self.use_water(water) and self.use_milk(milk) and self.use_sugar(sugar)):
            self.sell_tea(cups)
            print("------------------------------------------------------------------")
            print("Thanku you for using the machine")
            print("------------------------------------------------------------------")
        else:
            print("------------------------------------------------------------------")
            print("Need to refilled")
            print("------------------------------------------------------------------")

    def make_btea(self,cups:int):
        tea=(5/1000)*cups
        water=(100/1000)*cups
        # milk=1000/40
        sugar=(15/1000)*cups
        if(self.use_tea(tea) and self.use_water(water) and self.use_sugar(sugar)):
            self.sell_btea(cups)
            print("------------------------------------------------------------------")
            print("Thanku you for using the machine")  
            print("------------------------------------------------------------------")
        else:
            print("------------------------------------------------------------------")
            print("Need to refilled")
            print("------------------------------------------------------------------")

    
    def make_coffee(self,cups:int):
        coffee=(4/1000)*cups
        water=(20/1000)*cups
        milk=(80/1000)*cups
        sugar=(15/1000)*cups
        if(self.use_coffee(coffee) and self.use_water(water) and self.use_milk(milk) and self.use_sugar(sugar)):
            self.sell_coffee(cups)
            print("------------------------------------------------------------------")
            print("Thanku you for using the machine")
            print("------------------------------------------------------------------")
        else:
            print("------------------------------------------------------------------")
            print("Need to refilled")
            print("------------------------------------------------------------------")


    def make_bcoffee(self,cups:int):
        coffee=(3/1000)*cups
        water=(100/1000)*cups
        # milk=1000/40
        sugar=(15/1000)*cups
        if(self.use_coffee(coffee) and self.use_water(water)and self.use_sugar(sugar)):
            self.sell_bcoffee(cups)
            print("------------------------------------------------------------------")
            print("Thanku you for using the machine")  
            print("------------------------------------------------------------------")   
        else:
            print("------------------------------------------------------------------")
            print("Need to refilled")
            print("------------------------------------------------------------------")

if __name__ == "__main__":
    
    tcvm='''
    $$$$$$$$\                                 
    \__$$  __|                                
    $$ | $$$$$$$\ $$\    $$\ $$$$$$\$$$$\  
    $$ |$$  _____|\$$\  $$  |$$  _$$  _$$\ 
    $$ |$$ /       \$$\$$  / $$ / $$ / $$ |
    $$ |$$ |        \$$$  /  $$ | $$ | $$ |
    $$ |\$$$$$$$\    \$  /   $$ | $$ | $$ |
    \__| \_______|    \_/    \__| \__| \__|
                                            '''
    print(tcvm)
                                          
                                          
    machine=maker()
    while(True):
        try:
            # 3. System should have support for options like
            # ◦ Make Coffee
            # ◦ Make Tea
            # ◦ Make Black Coffee
            # ◦ Make Black Tea
            # ◦ Refill Container
            # ◦ Check Total Sale
            # ◦ Container Status
            # ◦ Reset Container
            # ◦ Exit TCVM

            # 8. System should be user-friendly & display message properly.


            option = int(input("\033[93m what you want to have \n 1.coffee\n 2.black coffee \n 3.tea \n 4.black tea \n 5.other\n 99.break\n"))
            # 7. System should have feature to take multiple orders(ex. 2 coffee or 10 tea)
            if(option == 1 or option ==2 or option ==3  or option==4):
                quantity=int(input("enter Quantity"))
            if(option==1):
                machine.make_coffee(quantity)
            elif (option==2):
                machine.make_bcoffee(quantity)
            elif(option==3):
                machine.make_tea(quantity)
            elif(option ==4):
                machine.make_btea(quantity)
            elif(option==5):
                # 11. Reports/Statistics:

                # • Total Tea-Coffee Sale Report Drink wise.
                # • Total Tea-Coffee Sale.
                # • Container Status Report(quantity of material present)
                # • Refilling counter (how many times refilling is done)

                print("\033[31m what do you want to do:")
                print("\033[93m 1.Refill")
                print("2.Total sale")
                print("3.Container_status")
                print("4.Reset Machine")
                print("5.Exit")
                option=int(input("\033[31m Please select an option"))
                if(option==1):
                    machine.fill()
    
                elif (option==2):
                    print("\033[93m total sale :",machine.total_sale())
                    print("tea: ",machine.tea_sale())
                    print("Black tea :",machine.btea_sale)
                    print("coffee :",machine.coffee_sale())
                    print("Black coffee :0",machine.bcoffee_sale())
                elif(option==3):
                    print(machine.container_status())
                elif(option ==4):
                    machine=maker()
                elif(option==5):
                    print("------------------------------------------------------------------")
                    print("\033[32m Thanku for Using TCVM")
                    print("------------------------------------------------------------------")
                    break

            elif (option==99):
                print("------------------------------------------------------------------")
                print("\033[32m Thanku for Using TCVM")
                print("------------------------------------------------------------------")
                break

            else:
                print("------------------------------------------------------------------")
                print("\033[32m please print a vaailid option")
                print("------------------------------------------------------------------")
        except:
            print("------------------------------------------------------------------")
            print("Some Error occured pleases try again")
            print("------------------------------------------------------------------")


    

    




