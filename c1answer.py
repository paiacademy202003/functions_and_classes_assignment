class Cafe:
    def __init__(self, menu, stock, money = 0):
        self.menu = menu
        self.stock = stock
        self.money = money

    def add_menu_item(self, item, price):
        self.menu[item] = price

    def add_stock(self, newstock):
        for x in newstock:
            if x in self.stock:
                self.stock[x] += newstock[x]
            else:
                self.stock[x] = newstock[x]

    def order_cost(self, order):
        total_cost = 0
        for item in order:
            if item not in self.menu:
                return "Not for sale"
            quantity = order[item]
            price = self.menu[item]
            total_cost += quantity * price
        return total_cost

    def place_order(self, order):
        valid_order = True
        for item in order:
            quantity = order[item]
            if item not in self.stock or item not in self.menu:
                valid_order = False
                return valid_order
            if self.stock[item] < quantity:
                valid_order = False
                return valid_order
        if valid_order:
            for item in order:
                quantity = order[item]
                self.stock[item] -= quantity
            self.money += self.order_cost(order)
        return valid_order

if __name__ == '__main__':
    sbux = Cafe({'coffee':2,'mocha':3,'bagel':2.5}, {'coffee':10, 'mocha':5, 'bagel':7, 'tea':20})
    print('menu before', sbux.menu)
    sbux.add_menu_item('sandwich',7)
    print('menu after', sbux.menu)
    print()
    print('stock before', sbux.stock)
    sbux.add_stock({'coffee':1})
    print('stock after', sbux.stock)
    price = sbux.order_cost({'mocha':3,'bagel':3})
    print('price of 3 mochas and 3 bagels', price)
    print()
    order = sbux.place_order({'mocha':3,'bagel':3})
    print(sbux.stock)
    print(sbux.money)
    print(order)
