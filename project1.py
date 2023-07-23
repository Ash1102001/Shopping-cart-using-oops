class fruitCart :
    def __init__(self,name,price):
        self.name = name
        self.price = price

class Store :
    def __init__(self):
        self.__cart = []  #To make our variables protected we need to apply two underscore before the variable

    def addtoCart (self,item):
       self.__cart.append(item)
    
    def removefromCart (self,index):
       self.__cart.pop(index)  
       
    def clearList (self):
        self.__cart.clear()
    
    def totalBill (self):
        total = 0
        
        for item in self.__cart :
            total += int(item.price)
            
        return total
    
    def displayCart (self):
        
        for i in range(0,len(self.__cart)):
            print(i+1,self.__cart[i].name)
        

store = Store()
'''store.addtoCart(fruitCart("Banana", 90))
store.addtoCart(fruitCart("Apples",67))'''
#store.cart.append(fruitCart("Cherries", 99))  to omit any unwanted addition we have
# to protect our cart so that users wont be able to add data unethically

#store.displayCart()

'''print(fruitCart(["Apple", 10],["banana" , 20]))
print(totalBill([fruitCart("Apple",10),fruitCart("banana" , 20)]))'''

print("Welcome to our store")

while True:
    
    print("Press a to add item to the list")
    print("Press r to remove item to the list")
    print("Press x to exit the list")
    print("Press c to clear the list")
    
    userInput = input("Please enter the input ")
    
    if userInput == "a" :
        itemName = input("Please enter the item name ")
        itemPrice = input("Please enter the item price ")
        store.addtoCart(fruitCart(itemName, itemPrice))
        
    elif userInput == "x" :
        break
    elif userInput == "r":
        index = int(input("Enter the position of the item to be removed "))
        store.removefromCart(index)
        
    elif userInput == "c":
        store.clearList()
    else :
        print("Please enter the valid input")
        
store.displayCart()
print(store.totalBill())   


        