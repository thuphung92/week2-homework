class Cart():
    def __init__(self):
        self.cart = []
        self.request = Request()
    
    def add_item(self):
        self.item = input("What would you like to add to your cart? ")
        self.cart.append(self.item)
        print(f"{self.item} was added to your cart.")
        
    def remove_item(self):
        self.item = input("What item would you like to remove? ")
        if self.item not in self.cart:
            print(f"{self.item} is not in your cart.")
        else:
            self.cart.remove(self.item)
            print(f"{self.item} was removed from your cart.")
    
    def show_cart(self):
        if len(self.cart)==0:
            print("Your cart is empty.")
        else:
            print("Your cart has:")
            for item in self.cart:
                print (item)
            
class Request():
    def __init__(self):
        self.request = ''
    def get_response(self):
        while True:
            self.request = input("What would you like to do: quit/add/remove or show? ")
            if self.request.lower() not in ['quit','add','remove','show']:
                print("Invalid value! Please try again!")
                continue
            else:
                break
        return self.request.lower()