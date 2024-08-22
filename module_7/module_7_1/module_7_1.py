from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = "products.txt"

    def get_products(self):
        file = open(self.__file_name, "r")
        file_read = file.read()
        file.close()
        return file_read

    def add(self, *products):
        file_r = open(self.__file_name, "r")
        file_read = file_r.read()
        file_r.close()
        file_write = open(self.__file_name, "a")
        if len(file_read) != 0:
            for product in products:
                if product.name not in file_read:
                    file_write.write(f"{product}\n")
                else:
                    print(f"Продукт {product} уже есть в магазине")
        else:
            for product in products:
                file_write.write(f"{product}\n")
        file_write.close()

    def clear_file(self):
        file = open(self.__file_name, "w")
        file.close()


s1 = Shop()
# s1.clear_file()
p1 = Product("Potato", 50.5, "Vegetables")
p2 = Product("Spaghetti", 3.4, "Groceries")
p3 = Product("Potato", 5.5, "Vegetables")

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
