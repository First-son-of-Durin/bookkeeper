"""
Описан класс, представляющий бюджет
"""
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass(slots=True)
class Budget():
    """
    Бюджет
    budget - запланированный бюджет
    sum - сумма потраченных средств
    duration - запланированный промежуток времени
    """
    duration: timedelta
    sum: float = 0
    budget: float = 0

    def __init__(self, budget: float, duration: timedelta, db_file: str):
        self.db_file = db_file
        self.duration = duration
        self.budget = budget
        self.sum = self.expenses_counting()

    def expenses_counting(self) -> float:
        con = sqlite3.connect(self.db_file)
        cursor = con.cursor()
        cursor.execute(f'SELECT SUM(amount) FROM expense WHERE expense_date>{str(datetime.now()-self.duration)[-8]}',)
        sum = cursor.fetchone()[0]
        con.commit()
        con.close()
        return sum