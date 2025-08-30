import copy
import random


class Hat:
    def __init__(self, **bolls: int) -> None:
        self.contents: list[str] = []

        for color, count in bolls.items():
            self.contents.extend([color] * count)

    def __repr__(self) -> str:
        return f'Hat({self.contents})'

    def draw(self, num: int = 1) -> list[str]:
        if num >= len(self.contents):
            drawn = self.contents[:]
            self.contents.clear()
            return drawn

        drawn = random.sample(self.contents, num)

        for ball in drawn:
            self.contents.remove(ball)

        return drawn


def experiment(hat: Hat, expected_balls: dict[str, int], num_balls_drawn: int, num_experiments: int) -> float:
    succes = 0

    for _ in range(num_experiments):
        copy_hats = copy.deepcopy(hat)
        drawn = copy_hats.draw(num_balls_drawn)

        counts: dict[str, int] = {}
        for ball in drawn:
            counts[ball] = counts.get(ball, 0) + 1

        ok: bool = True
        for color, count in expected_balls.items():
            if counts.get(color, 0) < count:
                ok = False
                break

        if ok:
            succes += 1

    return succes / num_experiments


if __name__ == '__main__':
    hat = Hat(black=6, red=4, green=3)
    print(repr(hat))
    probability = experiment(hat=hat,
                             expected_balls={'red': 2, 'green': 1},
                             num_balls_drawn=5,
                             num_experiments=2000)
    print(probability)
