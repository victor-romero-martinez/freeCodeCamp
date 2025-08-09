from __future__ import annotations
from typing import Any


class Category:
    def __init__(self, category_name: str):
        self.category = category_name.capitalize()
        self.ledger: list[dict[str, Any]] = []

    def __str__(self):
        title = f'{self.category:*^30}'
        total_cash = f'Total: {self.get_balance()}'
        details = ''

        for item in self.ledger:
            value, desc = item.values()
            details += (self.append_detail_line(desc, value) + '\n')

        return title + '\n' +\
            details +\
            total_cash

    def append_detail_line(self, name: str, amount: float) -> str:
        return f'{name[:23]:<23}{amount:>7.2f}'

    def deposit(self, amount: float, description: str = '') -> None:
        self.ledger.append({'amount': abs(amount), 'description': description})

    def withdraw(self, amount: float, description: str = '') -> bool:
        to_descount = abs(amount)
        is_less = self.check_funds(to_descount)

        if is_less:
            self.ledger.append({
                'amount': -to_descount,
                'description': description})
            return True

        return False

    def get_balance(self) -> float:
        balance: float = 0

        for l in self.ledger:
            balance += l['amount']

        return balance

    def check_funds(self, amount: float) -> bool:
        return self.get_balance() >= amount

    def transfer(self, amount: float, budget: Category) -> bool:
        withdraw = self.withdraw(
            amount, f'Transfer to {budget.category}')

        if withdraw:
            budget.deposit(
                amount, f'Transfer from {self.category}')
            return True

        return False


def create_spend_chart(categories: list[Category]):
    spend_category: list[dict[str, Any]] = []
    chart = 'Percentage spent by category\n'
    total_spend = 0
    max_len = 0

    # append property of category and calc auxiliar vars
    for category in categories:
        spend: float = 0

        for ops in (category.ledger):
            if ops['amount'] < 0:
                spend += ops['amount']

        arr_name = list(category.category)
        len_aux = len(arr_name)
        fix_spend = abs(round(spend, 2))

        total_spend += fix_spend
        max_len = len_aux if len_aux > max_len else max_len
        spend_category.append({
            'name': arr_name,
            'total': fix_spend
        })

    # calc percentage value
    for c in spend_category:
        percentage = c['total'] / total_spend * 100
        floor_per = (percentage // 10) * 10
        c['percentage'] = floor_per

    # draw chart
    for s in range(100, -1, -10):
        bar = str(s) + '|'
        value = ''

        for v in spend_category:
            if s <= v['percentage']:
                value += ' o '
            else:
                value += (' '*3)

        chart += f'{bar:>4}{value} \n'

    # draw label
    chart += f'{"-":>5}{"---"*len(spend_category)}\n'
    for i in range(max_len):
        line = ''
        for c in spend_category:
            if i < len(c['name']):
                line += c['name'][i] + (' '*2)
            else:
                line += ' '*3

        chart += (' '*5) + line

        if i != max_len - 1:
            chart += '\n'

    return chart


if __name__ == '__main__':
    food = Category('Food')
    food.deposit(1000, 'initial deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    clothing = Category('clothing')
    food.transfer(50, clothing)
    clothing.withdraw(18.99, 't-shirt')
    auto = Category('auto')
    auto.deposit(50)
    auto.withdraw(23.99, 'test')
    print(food)
    # print(clothing)
    print(create_spend_chart([food, clothing, auto]))


# sample
# *************Food*************
# initial deposit        1000.00
# groceries               -10.15
# restaurant and more foo -15.89
# Transfer to Clothing    -50.00
# Total: 923.96

# Percentage spent by category
# 100|
#  90|
#  80|
#  70|
#  60| o
#  50| o
#  40| o
#  30| o
#  20| o  o
#  10| o  o  o
#   0| o  o  o
#     ----------
#      F  C  A
#      o  l  u
#      o  o  t
#      d  t  o
#         h
#         i
#         n
#         g
