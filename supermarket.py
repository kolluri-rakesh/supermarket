from datetime import datetime
name=input("enter your name:")

lists=''' 
         rice   rs 20/kg
         sugar  rs 10/kg
         salt   rs 15/kg
         oil    rs 500/kg
         soap   rs 20
         ghee   rs 24/kg
         bottle rs 20
         salt   rs 19/kg
         book   rs 10
         pen    rs 5
         milk   rs 10
         butter rs 12

        

          '''

price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]
items={  'rice'   :20,
         'sugar'  :10,
         'salt'   :15,
         'oil'    :500,
         'bottle' : 20,
         'salt'   : 19,
         'book'   : 10,
         'pen'    : 5,
         'milk'   : 10,
         'butter' : 12
          }

option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items:")
        quantity=int(input("enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice=totalprice+price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is not found")
    else:
        print("you entered item is wrong")
    inp=input("can i bill the items yes or no:")
    if inp=="yes":
        pass
        if finalamount!=0:
            print(25*"=","ram supermarket",25*"=")
            print(28*" ","RGM")
            print("name:",name,30*" ","date:",datetime.now())
            print(60*"-")
            print("sno",8*" ","items",8*" ","quality",3*" ","price")
            for i in range(len(pricelist)):
                print(i,8*" ",ilist[i],3*" ",qlist[i],8*" ",plist[i])
            print(75*"-")
            print(50*" ","totalprice:","rs",totalprice)
            print('gst amount',50*" ","rs",gst)
            print(75*"-")
            print(50*" ","finalAmount","rs",finalamount)
            print(75*"-")
            print(20*" ","Thanks for visiting")
            print(75*"-")



        

