print ("\nWelcome to our grocery store ☺️")

inventory = {
    1:{"apple  🍎":{"price":20,           "qnt":100}},
    2:{"banana  🍌":{"price": 25,         "qnt":60}},
    3:{"milk  🥛":{"price": 25,           "qnt":50}},
    4:{"choclate  🍫":{"price":20,        "qnt":100}},          
    5:{"egg  🥚":{"price":20,             "qnt":40}}
}

cart =[]

def home ():
    print ("\npress 1 to see the available items")
    print ("press 2 to open cart")
    print ("press 3 to exit the stor")
    print ("press 4 to open order history")
    choice = (input("\nPlease enter your choice:"))
    if choice.isdigit() and choice in ["1","2","3","4"]:
        choice = int(choice)
        if choice == 1:
            print ("-"* 30)
            for pid,info in inventory.items():
                product_name = next(iter(info))
                price = info[product_name]['price']
                quantity = info[product_name]['qnt']
                print({pid})
                print(f"product:{product_name}")
                print(f"price:{price}")
                print(f"available quantity:{quantity}")
                print ("-"* 30)
            print("\nTo add an item to cart write the item no.")
            print("write order to place order of selected products")
            print("write back to get back to home page or exit to exit store")
            Store().selecting(home,choice)
        elif choice == 2:
            Store().selecting(home,choice)
        elif choice == 3:
            Store().selecting(home,choice)
        return choice
    else:
        print("\nwrong input")
        home()

def confirmation ():
    print ("\n!ORDER PLACED! 🥳")

class Payment():
    def bill (self,home,choice):
        while True :
            money = 0
            print("\nyour cart")
            for item in cart:
                money += item["quantity"]*item["price"]
                final_amount=item["price"]*item["quantity"]
                print("-"*30)
                print(f"product:{item['product']}")
                print(f"price:{item['price']}")
                print(f"quantity:{item['quantity']}")
                print(f"payable amount:{final_amount}")
                print("-"*30)
            tell = str (input("Confirm your booking (y/n):"))
            if tell == "y" or tell == "Y":
                Payment().ask(self.bill,home,choice)
                break
            elif tell == "n" or tell == "N":
                Store().selecting(home,choice)
                break
            else:
                print ("\nwrong input")
                continue

    def ask (self,bill,home,choice):
        while True :
            print ("1. Cash on deliver\n2. UPI \n3. Card \n4. back") 
            pay =(input("please enter your mode of payment or choice:"))
            if pay == ("Cash on delivery") or pay == ("cash on deliver") or pay == ("cod") :
                confirmation ()
                break
            elif pay == ("upi") or pay == ("Upi") or pay == ("UPI"):
                upi_id = input("please tell your upi id and complete the paymet request:")
                print("checking......")
                conf = input("press y on completing payment and n to change payment method:")
                if conf == "y":
                    confirmation ()
                    break
                elif conf == "no":
                    Payment().bill (home,choice)
                    continue
                else :
                    print ("\ninvalid input")
                    continue
            elif pay == ("card") or pay == ("Card"):
                card_num = int(input("please enter the card number"))
                card_cvv = int(input("pleasee enter the cvv number"))
                print ("checking......")
                ask = input("press y on completing payment and n to change payment method")
                if ask == "y" or ask == "Y":
                    confirmation ()
                    break
                if ask == "n" or ask == "N":
                    bill ()
                else :
                    print ("\ninvalid input")
                    bill()
            elif pay == ("back") or pay == ("Back"):
                Store().selecting(home,choice)
            elif pay.isdigit():
                transition= int(pay)
                if transition == 1:
                    confirmation ()
                    break
                elif transition == 2:
                    upi_id = input("please tell your upi id and complete the paymet request:")
                    print("checking......")
                    ask = input("press y on completing and n to change method:")
                    if ask == "y":
                        confirmation ()
                        break
                    elif ask == "n":
                        continue
                    else :
                        print ("\ninvalid input")
                        continue
                elif transition == 3:
                    card_num = int(input("please enter the card number"))
                    card_cvv = int(input("pleasee enter the cvv number"))
                    print ("checking......")
                    ask = input("press y on completing payment and n to change payment method")
                    if ask == "y":
                        confirmation ()
                        break
                    elif ask == "n":
                        continue
                    else :
                        print ("\ninvalid input")
                        continue
                elif transition == 4:
                    Store().selecting(home,choice)
                elif pay not in "1234":
                    print ("\nplease input the value from given options")
                    continue
            else: 
                print ("\nplease input the value from given options")
                continue

class Store ():
    def __init__ (self):
        self.inventory = inventory
        self.cart = cart
    def selecting(self,home,choice):
        while True :
            if choice == 1:
                itm_no = (input("\nPlease choose your product's or choice:"))
                if itm_no.isdigit() and int(itm_no) in self.inventory:
                    num= int(itm_no)
                    product_name=next(iter(self.inventory[num]))
                    price=(self.inventory[num][product_name]["price"])
                    quantity = (input ("please enter the quantity:"))
                    if quantity.isdigit():
                        quantity = int (quantity)
                        if num in self.inventory and quantity < self.inventory[num][product_name]["qnt"]:
                            self.inventory[num][product_name]["qnt"] -= quantity
                            if len(self.cart) != 0:
                                for item in self.cart:
                                    if item["product"] == product_name:
                                        item["quantity"] += quantity
                                    else:
                                        continue
                            else:
                                self.cart.append({"product" : product_name,
                                "quantity":quantity,
                                "price":price
                                })
                                print("item added to cart!")
                            self.product = product_name
                            self.price   = price
                            self.quantity=quantity
                            continue
                        else :
                            print("\nnot enough stock")
                            continue
                    else:
                        print("\nwrong input or not enough stock")
                        continue
                elif itm_no == "order":
                        Payment().bill(home,choice)
                        return "price" ,"quantity","product"
                elif itm_no == "back":
                    home()
                elif itm_no == "exit":
                    break
                else:
                    print("\nwrong input")
                    continue
            elif choice == 2:
                print (cart)
                home()
            elif choice == 3:
                return
            else:
                print("\nwrong input")
                home()
            
home()

def rev ():
    while True :
        review = str(input("\nWhould u like to review us🤗 (y/n):"))
        if review in "yY":
            print ("\n1. loved it 🤩 \n2. like it ☺️ \n3. nutral 😐 \n4. it was not good 🙁 \n5. it was worst 😣") 
            reply = (input("\nTell ur your openion:"))
            reply = str(reply)
            if reply not in "12345":
                print ("\nwrong input")
                continue
            else:
                print("thank you for your review it's valuble to us 🙂")
                break
        elif review in "Nn" :
            break
        elif review not in "YyNn":
            print ("\nwrong input")
            continue

rev()
print("\nTHANKS FOR VISITING ☺️")