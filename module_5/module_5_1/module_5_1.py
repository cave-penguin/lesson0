class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor == 0:
            print("Вы на первом этаже")
        elif 0 < new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")


h1 = House("ЖК Горский", 18)
h2 = House("Домик в деревне", 2)
h3 = House("ЖК Какое-то название", 9)
h1.go_to(5)
h2.go_to(10)

h3.go_to(0)
h3.go_to(20)
h3.go_to(2)
h3.go_to(-2)
h3.go_to(1)
h3.go_to(9)
