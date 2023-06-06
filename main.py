class Paint_shop:
    def __init__(self):
        super().__init__()
        self.goods = "In paint shop sells different colors"

class Clothing_store:
    def __init__(self):
        super().__init__()
        self.choice_of_clothes = "In clothing store sells different cloth  "

class Grocery_store:
    def __init__(self):
        super().__init__()
        self.food = "In grocery store sells different food  "

class Construction_shop:
    def __init__(self):
        super().__init__()
        self.construction = "In construction store sells different items for construction"

class Supermarket(Paint_shop,Clothing_store,Grocery_store,Construction_shop):
    def print_info(self):
        print(self.goods)
        print(self.choice_of_clothes)
        print(self.food)
        print(self.construction)
        print("All goods which was in privious markets, you can found in supermarket, another words supermarket unites all privious markets")


Novus = Supermarket()
Novus.print_info()