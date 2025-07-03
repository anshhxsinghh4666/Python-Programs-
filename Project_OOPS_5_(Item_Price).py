# Create a class called order which stored ite & its price.
# Use Dunder function __gt__() to convey that:
#                 order 1 > order 2 if price of order 1 > price of order 2.

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self,odr2):
        return self.price > odr2.price

odr1 = Order("Chips" , 20)
odr2 = Order("Tea" , 15)

print(odr1 > odr2) # Output: True
