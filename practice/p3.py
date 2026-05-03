# create a class called order which stores item and its price .
# use dunder function __gt__() to convoy that:
# order1>order2: if price of order1 > price of order 2

class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self, order):
        return self.price>order.price

ord1=order("chips",20)
ord2=order("tea",15)

print(ord1>ord2)



