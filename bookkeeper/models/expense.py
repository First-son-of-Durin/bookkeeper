"""
Описан класс, представляющий расходную операцию
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Expense:
    """
    Расходная операция.
    amount - сумма
    category - id категории расходов
    expense_date - дата расхода
    added_date - дата добавления в бд
    comment - комментарий
    pk - id записи в базе данных
    """
    amount: float
    category: str
    expense_date: str
    added_date: str
    comment: str = ''
    pk: int = 0

    def __init__(self, amount: float, category: str, expense_date: str = "", added_date: str = "", comment: str = ""):
        self.amount = amount
        self.category = category
        self.added_date = str(datetime.now())[:-7]
        self.expense_date = expense_date
        self.comment = comment
        self.pk: int = 0