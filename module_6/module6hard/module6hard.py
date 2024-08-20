import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(0 <= col <= 255 and isinstance(col, int) for col in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            return self.__color

    def __is_valid_sides(self, *args):
        if len(args) == 1 and isinstance(args[0], int) and args[0] > 0:
            return True
        elif len(args) > 1:
            return all(
                isinstance(side, int) and 0 < side for side in args
            ) and self.sides_count == len(args)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        if self.sides_count == 1:
            return self.get_sides()[0]
        else:
            return sum(list(self.get_sides()))

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.__sides = [*new_sides]
        elif self.__is_valid_sides(*new_sides):
            self.__sides = [1 for _ in range(self.sides_count)]


class Circle(Figure):
    def __init__(self, color, *sides):
        self.sides_count = 1
        if len(sides) == 1:
            self.__sides = [sides]
        else:
            self.__sides = [1]
        super().__init__(color, self.__sides)

    def __radius(self):
        P = self.get_sides()[0]
        return P / (2 * math.pi)

    def get_square(self):
        radius = self.__radius()
        return math.pi * radius**2


class Triangle(Figure):
    def __init__(self, color, *sides):
        self.sides_count = 3
        if len(sides) == 3:
            self.__sides = [side for side in sides]
        else:
            self.__sides = [1] * self.sides_count
        super().__init__(color, *self.__sides)

    def get_square(self):
        p = self.__len__() / 2
        return math.sqrt(
            p
            * (p - self.get_sides()[0])
            * (p - self.get_sides()[1])
            * (p - self.get_sides()[2])
        )


class Cube(Figure):

    def __init__(self, color, *sides):
        self.sides_count = 12
        if len(sides) == 1:
            self.__sides = [sides[0]] * self.sides_count
        else:
            self.__sides = [1] * self.sides_count
        super().__init__(color, *self.__sides)

    def get_volume(self):
        side_length = self.get_sides()[0]
        return side_length**3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((0, 0, 0), 3, 4, 5)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


print(triangle1.get_square())
triangle1.set_color(234, 123, 145)
print(triangle1.get_color())

triangle1.set_sides(5, 6, 7)
print(triangle1.get_sides())
print(triangle1.get_square())

print(circle1.get_square())
