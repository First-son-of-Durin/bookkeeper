"""
Описан класс, представляющий расходную операцию
"""

from dataclasses import dataclass, field
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
    amount: int = 0
    category: int = 0
    expense_date: datetime = field(default_factory=datetime.now)
    added_date: datetime = field(default_factory=datetime.now)
    comment: str = ''
    pk: int = None

    def __init__(self, amount: int = 0, category: int = 0, expense_date: str = '',
                 added_date: str = '', comment: str = '', pk: int = 0):
        self.amount = amount
        self.category = category
        self.added_date = str(added_date)[:-7]
        self.expense_date = str(expense_date)[:-7]
        self.comment = comment
        self.pk = pk

    def __repr__(self):
        """
        Объект класса Expense отображается как
        Expense(amount=int, category=int, expense_date=str,
                added_date=str, comment=str, pk=int)
        """
        return (f'Expense(amount={self.amount}, category={self.category},'
                f'expense_date={self.expense_date}, added_date = {self.added_date}, '
                f'comment={self.comment}, pk={self.pk})')

    def __str__(self):
        """
        Объект класса Expense отображается как
        Expense(amount=int, category=int, expense_date=str,
                added_date=str, comment=str, pk=int)
        """
        return (f'Expense(amount={self.amount}, category={self.category},'
                f'expense_date={self.expense_date}, added_date = {self.added_date}, '
                f'comment={self.comment}, pk={self.pk})')
