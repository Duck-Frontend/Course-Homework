class Product:
    def __init__(self, name="", store="", price=0.0):
        self.__name = name
        self.__store = store
        self.__price = price
    
    def get_name(self):
        return self.__name
    
    def get_store(self):
        return self.__store
    
    def get_price(self):
        return self.__price
    
    def display(self):
        print(f"Товар: {self.__name}, Магазин: {self.__store}, Цена: {self.__price} руб.")
    
    def __add__(self, other):
        return self.__price + other.__price

class Warehouse:
    def __init__(self):
        self.__products = []
    
    def add_product(self, product):
        self.__products.append(product)
    
    def show_by_index(self, index):
        if 0 <= index < len(self.__products):
            self.__products[index].display()
        else:
            print("Неверный индекс")
    
    def show_by_name(self, name):
        found = False
        for product in self.__products:
            if product.get_name() == name:
                product.display()
                found = True
        if not found:
            print("Товар не найден")
    
    def sort_by_name(self):
        self.__products.sort(key=lambda x: x.get_name())
    
    def sort_by_store(self):
        self.__products.sort(key=lambda x: x.get_store())
    
    def sort_by_price(self):
        self.__products.sort(key=lambda x: x.get_price())
