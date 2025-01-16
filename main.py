import random

menu={
    "chai":15,
    "hot coffe":20,
    "chocolate coffe": 40,
    "sandwich":50,
    "plain dosa": 70,
    "masala dosa":100,
    "salad":70,
    "allo paratha":50
}
    
print('''Welcome To Café Reverie 
    !!MENU!!
    Chai:15 Rs
    Hot Coffe:20 Rs
    Chocolate Coffe: 40 Rs
    Sandwich:50 Rs
    Plain Dosa: 70 Rs
    Masala Dosa:100 Rs
    Salad:70 Rs
    Allo Paratha(2 piece):50 Rs
''' )
login_name=input("Enter your Name:")
login_no=random.randint(100000,9999999)
login_id=login_name[:3]+str(login_no)



order_prize=0
while True:
    item_1=input("Place your order:").strip().lower()
    if item_1 in menu:
     print(f"{item_1} is added to your order.")
     order_prize+=menu[item_1]
    else:
       print(f"{item_1} is not present in menu.Please order something from the menu.")
       continue

    another_item=input("Do you want to order something else(yes/no):").strip().lower()
    if another_item!="yes":
       break

print(f"your order is going to ready in 10 minutes.")
print(f"your Bill is {order_prize} Rs.")
print("Thankyou ! Please visit again.")


f=open("order.txt","w")
f.write(f"Customer ID {login_id}, Total Bill {order_prize}")
f.close()
