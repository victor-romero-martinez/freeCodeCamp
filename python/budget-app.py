from __future__ import annotations
from typing import Any


class Category:
    def __init__(self, category_name: str):
        self.category = category_name
        self.ledger: list[dict[str, Any]] = []

    def __str__(self):
        title = f'{self.category:^30}'.replace(' ', '*')
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
            amount, f'Transfer to {budget.category.capitalize()}')

        if withdraw:
            budget.deposit(
                amount, f'Transfer from {self.category.capitalize()}')
            return True

        return False


def create_spend_chart(categories: list[Category]):
    pass


if __name__ == '__main__':
    food = Category('Food')
    food.deposit(1000, 'initial deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    clothing = Category('clothing')
    food.transfer(50, clothing)
    print(food)
    # print(clothing)

# samle
# *************Food*************
# initial deposit        1000.00
# groceries               -10.15
# restaurant and more foo -15.89
# Transfer to Clothing    -50.00
# Total: 923.96
