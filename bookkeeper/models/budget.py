"""
Описан класс, представляющий бюджет
"""

from dataclasses import dataclass
from datetime import timedelta


@dataclass(slots=True)
class Budget:
    """
    Бюджет
    budget - запланированный бюджет
    duration - запланированный промежуток времени
    """
    duration: timedelta
    budget: float = 0
    pk: int = None
