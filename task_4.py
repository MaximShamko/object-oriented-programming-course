class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Z:
    def __init__(self, z):
        self.z = z


class H:
    def __init__(self, h):
        self.h = h


class Point3Dh(Point2D, Z, H):
    def __init__(self, x, y, z, h):
        Point2D.__init__(self, x, y)
        Z.__init__(self, z)
        H.__init__(self, h)

    def print_info(self):         # метод для вывода информации о координатах
        if self.h != 0:
            print("Обычные координаты точки: (" + str(self.x / self.h) + ", " + str((self.y / self.h)) + ", " +
                  str(self.x / self.h) + ")")
        else:
            print("Ошибка, параметр h не может быть равен 0")


A = Point3Dh(50, 25, 15, 5)    # создаем 3 объекта класса Point3Dh
B = Point3Dh(24, 18, 16, 2)
C = Point3Dh(27, 6, 18, 3)

A.print_info()       # программа выводит обычные координаты точки, используя данные об однородных координатах
B.print_info()
C.print_info()