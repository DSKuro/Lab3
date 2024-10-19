from datetime import datetime

class Transactions:
    def __init__(self, type : bool, type_income : str, cost : float, date : datetime) -> None:
        self.type = type
        self.type_income = type_income
        self.cost = cost
        self.date = date

    def __str__(self) -> str:
        return (f'Тип транзакции  - {self.type},'
                f'Подтип транзакции - {self.type_income},'
                f'потраченные средства - {self.cost},'
                f'дата операции - {self.date}')