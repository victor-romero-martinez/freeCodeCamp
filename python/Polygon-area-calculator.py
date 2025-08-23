from __future__ import annotations


class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.max_size = 50

    def __str__(self) -> str:
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width: int) -> None:
        self.width = width

    def set_height(self, height: int) -> None:
        self.height = height

    def get_area(self) -> float:
        return self.width * self.height

    def get_perimeter(self) -> float:
        return 2 * self.width + 2 * self.height

    def get_diagonal(self) -> float:
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self) -> str:
        if self.width >= self.max_size or self.height >= self.max_size:
            return 'Too big for picture.'

        return '\n'.join('*' * self.width for _ in range(self.height)) + '\n'

    def get_amount_inside(self, shape: Rectangle) -> int:
        if self.width < shape.width or self.height < shape.height:
            return 0

        return int((self.width // shape.width) * (self.height // shape.height))


class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(side, side)

    def __str__(self) -> str:
        return f'Square(side={self.width})'

    @property
    def side(self) -> int:
        return self.width

    @side.setter
    def side(self, value: int):
        self.set_side(value)

    def set_side(self, side: int) -> None:
        super().set_width(side)
        super().set_height(side)

    def set_width(self, width: int) -> None:
        self.set_side(int(width))

    def set_height(self, height: int) -> None:
        self.set_side(int(height))


if __name__ == '__main__':
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))
