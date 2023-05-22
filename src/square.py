from src.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError(f'Pending side_a >0, got {side_a}')
        super().__init__(side_a, side_a)
        self.name = 'Square'
