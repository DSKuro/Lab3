from turtledemo.penrose import start

from transaction import Transactions

class Budget:
    total_income = 0.0
    total_expences = 0.0

    def __init__(self, start_budget : float, transactions : list) -> None:
        self.budget = 0.0
        self.debt = False
        self.start_budget = start_budget
        self.transactions = transactions

    def add_transactions(self, transaction : Transactions):
        self.transactions.append(transaction)

    def calculate_income(self) -> None:
        for i in self.transactions:
            if i.type:
                self.total_income += i.cost

    def calculate_expences(self) -> None:
        for i in self.transactions:
            if not i.type:
                self.total_expences += i.cost

    def calculate_budget(self):
        self.calculate_income()
        self.calculate_expences()
        self.budget = (self.total_income + self.start_budget) - self.total_expences
        if self.budget < 0:
            self.debt = True

    @property
    def get_total_income(self) -> float:
        return self.total_income

    @property
    def get_total_expences(self) -> float:
        return self.total_expences

    @property
    def get_budget(self) -> float:
        return self.budget

    def __str__(self):
        if not self.debt:
            return (f'Start budget: {self.start_budget},'
                f'Common income: {self.total_income},'
                f'Common expences: {self.total_expences},'
                f'Result budget: {self.budget}')
        else:
            return f'Debts!'
