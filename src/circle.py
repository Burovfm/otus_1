from src.figure import Figure

pi = 3.14


class Circle(Figure):
    def __init__(self, radius: int):
        self.radius = radius
        self.name = 'Circle'
        if radius <= 0:
            raise ValueError(f'Pending radius >0, got {radius}')

    def get_area(self):
        return round(pi * (self.radius ** 2), 2)

    def get_perimeter(self):
        return round(2 * pi * self.radius)
