import math


class Sphere:
    """Класс сферы"""

    def __init__(self, radius=1, x=1, y=1, z=1):
        self.__radius = radius
        self.__x = x
        self.__y = y
        self.__z = z

    def get_volume(self):
        return (4/3) * math.pi * self.__radius**3

    def get_square(self):
        return 4 * math.pi * self.__radius**2

    def set_radius(self, new_radius):
        self.__radius = new_radius

    def get_radius(self):
        return self.__radius

    def get_center(self):
        return self.__x, self.__y, self.__z

    def set_center(self, new_x, new_y, new_z):
        self.__x = new_x
        self.__y = new_y
        self.__z = new_z

    def is_point_inside(self, x, y, z):
        distance = math.sqrt(
            (x - self.__x)**2 +
            (y - self.__y)**2 +
            (z - self.__z)**2)

        return distance < self.__radius
