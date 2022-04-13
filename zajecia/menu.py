class Menu():
    def __init__(self):
        self.dishes = []
        self.dish_reader()
        self.menu_printer()

    
    def dish_reader(self):
        index = 1
        with open(r"C:\Users\SEBA XD\Desktop\python vsc\zajecia\menu.txt", encoding="utf-8") as menu:
            for line in menu.readlines():
                line.strip()
                if ";" in line:
                    dish_and_price = line.split(";")
                    dish_name = dish_and_price[0]
                    price = int(dish_and_price[1])
                    self.dishes.append(Dish_Price_Structure(index, dish_name, price))
                    index += 1
    
    def menu_printer(self):
        for option in self.dishes:
            print(option.index, option.dish, option.price)

    def orders(self):
        order_amount = input("""Please enter how many products you wont order: """)
        if not order_amount.isdigit():
            print("Please enter a number not a string")
            self.orders()
            return
        else:
            order_amount = int(order_amount)
            order_sum = 0
            for _ in range(order_amount):
                dish_id = input("Please enter an id of a dish you wont to order: ")
                if not dish_id.isdigit():
                    print("Please enter a number not a string")
                    self.orders()
                    return
                else:
                    dish_id = int(dish_id)
                if 0 > dish_id or dish_id > len(self.dishes):
                    print("There is't such dish in menu")
                    break
                else:
                    dish = self.dishes[dish_id - 1]
                    order_sum += dish.price
            print(f"You need to pay {order_sum} for your order")

class Dish_Price_Structure():
    def __init__(self, index, dish_name, price):
        self.index = index
        self.dish = dish_name
        self.price = price



if __name__ == "__main__":
    menu1 = Menu()
    menu1.orders()