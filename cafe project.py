Tea_unit=0
Coffee_unit=0
Juice_unit=0
Sandwich_unit=0
chocolatecoffee=0
Total_bill=0
Tea_unit1=0
Coffee_unit1=0
Juice_unit1=0
Sandwich_unit1=0
chocolatecoffee1=0
Tea_bill2=0
Coffeebill2=0
Sandwich_bill2=0
Juice_bill2=0
chocolatecoffee_bill2=0
Tea_total=0
Coffee_total=0
Juice_total=0
Sandwich_total=0
chocolatecoffee_total=0
#Welcome note
name=input("would you please tell your name sir:").strip()
print(f"Welcome to our cafe {name} sir")
print("please sit here")

#lucky discount
if name[0].lower()=="a":
    print("You are lucky customer")
    print("  ")
    print('since your name starts with  A you have discount of 5rs')
print("Here is the menu ")
print("Tea-15Rs\nCoffee-20Rs\nJuice-25Rs\nSandwich-30Rs")
#offers that cafe have
print("We have some offers for you :")
print(" ")
print("If more than 5 units of the same drink are ordered, a 10% bulk discount is applied ")
print("If bill is greater than 200 5% discount")
#order taking
def cafe():
    if order.lower()=="tea":
      Tea_unit=int(input("How many sir"))
    if order.lower()=="coffee":
      Coffee_unit=int(input("How many sir"))
      if Coffee_unit>=3:
        print("You should try some our special chocolate coffee")
        order2=input("Do you want it sir:")
        if order2.lower()=="yes":
            chocolatecoffee=int(input("how many sir"))
        else:
            print("ok sir")
    if order.lower()=="juice":
        Juice_unit=int(input("How many sir"))
        if Juice_unit==2:
          print("if you order another one you get a free cookie")
          order3=input("Do you want it sir:")
          if order3.lower()=="yes":
            Juice_unit2=int(input("how many sir"))
            Juice_unit+=Juice_unit2
          else:
            print("ok sir")
    if order.lower()=="sandwich":
        Sandwich_unit+=int(input("How many sir"))
order=input("Tell the order sir:")
cafe()
if (Tea_unit+Coffee_unit+Sandwich_unit+Juice_unit+chocolatecoffee)>=1:
 while True:
    other=input("Is there anything you want sir:")
    if other.lower()!="yes":
        print("okay no more orders sir.Thank you")
        break
    else:
        cafe()
if Tea_unit>=1 and Coffee_unit>=1 and Juice_unit>=1 and Sandwich_unit==0:
    print("Looks like someone is really thirsty today!")
if Tea_unit>=1 and Sandwich_unit>=1 and Juice_unit==0 and Coffee_unit==0:
    print("Perfect Combo! Here's a free smile :")
#billing for each item
Tea_bill=Tea_unit*15
Coffeebill=Coffee_unit*20
Juice_bill=Juice_unit*25
Sandwich_bill=Sandwich_unit*30
chocolatecoffee_bill=chocolatecoffee*35
print("Before Discount Bill is ")
if Tea_unit>=1:
    print(f"For {Tea_unit} Tea\'s : {Tea_bill}")
if Coffee_unit>=1:
    print(f"For {Coffee_unit} Coffee\'s : {Coffeebill}")
if Juice_unit>=1:
    print(f"For {Juice_unit} Juices : {Juice_bill}")
if Sandwich_unit>=1:
    print(f"For {Sandwich_unit} Sandwich\'s : {Sandwich_bill}")
if chocolatecoffee>=1:
    print(f"For {chocolatecoffee} chocolate coffee\'s : {chocolatecoffee_bill}")
Total_bill=Tea_bill+Coffeebill+Juice_bill+Sandwich_bill+chocolatecoffee_bill
#if the ordered item is less than 1 and 20rs
if (Tea_unit+Coffee_unit+Sandwich_unit+Juice_unit+chocolatecoffee)==1 and Total_bill<20:
    choice=input("Would you like to add something else to get free delivery")
    if choice.lower()=="yes":
        while True:
            other2=input("order what you want:")
            if other2.lower()=="nothing":
                print("Ok sir")
                break
            else:
                if other2.lower()=="tea": 
                    Tea_unit1=int(input("How many sir"))
                if other2.lower()=="coffee":
                    Coffee_unit1=int(input("How many sir"))
                    if (Coffee_unit+Coffee_unit1)>=3:
                        print("You should try some our special chocolate coffee")
                        order4=input("Do you want it sir:")
                        if order4.lower()=="yes":
                            chocolatecoffee1=int(input("how many sir"))
                        else:
                            print("ok sir")
                if other2.lower()=="juice":
                    Juice_unit1=int(input("How many sir"))
                    if (Juice_unit+Juice_unit1)==2:
                        print("if you order another one you get a free cookie")
                        order5=input("Do you want it sir:")
                        if order5.lower=="yes":
                            Juice_unit1=int(input("how many sir"))
                        else:
                            print("ok sir")
                if other2.lower()=="sandwich":
                    Sandwich_unit1=int(input("How many sir"))
            Tea_bill2=Tea_unit1*15
            Coffeebill2=Coffee_unit1*20 
            Juice_bill2=Juice_unit1*25
            Sandwich_bill2=Sandwich_unit1*30
            chocolatecoffee_bill2=chocolatecoffee1*35
            Total_bill=Total_bill+(Tea_bill2+Coffeebill2+Juice_bill2+Sandwich_bill2+chocolatecoffee_bill2)
            if (Tea_unit1+Tea_unit)>=1:
                print(f"For {Tea_unit1+Tea_unit} Tea\'s : {Tea_bill2+Tea_bill}")
            if (Coffee_unit1+Coffee_unit1)>=1:
                print(f"For {Coffee_unit1+Coffee_unit} Coffee\'s : {Coffeebill2+Coffeebill}")
            if (Juice_unit1+Juice_unit)>=1:
                print(f"For {Juice_unit1+Juice_unit} Juices : {Juice_bill2+Juice_bill}")
            if (Sandwich_unit1+Sandwich_unit)>=1:
                print(f"For {Sandwich_unit1+Sandwich_unit} Sandwich\'s : {Sandwich_bill2+Sandwich_bill}")
            if (chocolatecoffee1+chocolatecoffee)>=1:
                print(f"For {chocolatecoffee1+chocolatecoffee} chocolate coffee\'s : {chocolatecoffee_bill2+chocolatecoffee_bill}")
            break
    else:
        print("ok sir")
if (Tea_unit+Coffee_unit+Sandwich_unit+Juice_unit+chocolatecoffee)==1:
 print(Total_bill)
#Bulk Discount offer
 print("After Discount Total bill is:")
 Tea_total=Tea_bill+Tea_bill2
 if (Tea_unit+Tea_unit1)>5:
    print("for Bulk Discount offer:")
    Tea_total*=0.9
    print(Tea_total)
 Coffee_total=Coffeebill+Coffeebill2 
 if (Coffee_unit+Coffee_unit1)>5:
    print("for Bulk Discount offer:")
    Coffee_total*=0.9
    print(Coffee_total)
 Juice_total=Juice_bill+Juice_bill2
 if (Juice_unit+Juice_unit1)>5:
    print("for Bulk Discount offer:")
    Juice_total*=0.9
    print(Juice_total)
 Sandwich_total=Sandwich_bill+Sandwich_bill2
 if (Sandwich_unit+Sandwich_unit1)>5:
    print("for Bulk Discount offer:")
    Sandwich_total*=0.9
    print(Sandwich_total)
 chocolatecoffee_total=chocolatecoffee_bill+chocolatecoffee_bill2
 if (chocolatecoffee+chocolatecoffee1)>5:
    print("for Bulk Discount offer:")
    chocolatecoffee_total*=0.9
    print(chocolatecoffee_total)
 Total_bill=Tea_total+Coffee_total+Juice_total+Sandwich_total+chocolatecoffee_total
 #Big order discount

 if Total_bill>=200: 
    print("For Big order Discount")
    Total_bill=Total_bill-(Total_bill*0.05)
    print(Total_bill)
 if name[0].lower()=="a":
    print("For lucky letter discount")
    Total_bill-=5
    print(Total_bill)
 print("After All Discounts")
 print(f"the total bill is {Total_bill:.2f}")