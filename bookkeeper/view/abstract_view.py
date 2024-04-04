"""
Модуль содержит описание абстрактного представления
"""

from typing import Protocol, Callable
from bookkeeper.bookkeeper.models.expense import Expense
from bookkeeper.bookkeeper.models.category import Category
from bookkeeper.bookkeeper.models.budget import Budget


class AbstractView(Protocol):
    def set_category_list(self, handler: [Category]) -> None:
        """
        Метод воссоздает список категорий из базы данных и
        и добавляет его в графический интерфейс (GUI)
        # FIXME:
        Возможно вместо handler: [Category]
        должно быть cat: list[Category]
        """
        pass

    def register_category_deleter(self, handler: Callable) -> None:
        """
        Метод регистрирует обработчик команды кнопки, удаляющей категорию
        """
        pass

    def register_category_adder(self, handler: Callable) -> None:
        """
        Метод регистрирует обработчик команды кнопки, добавляющий категорию
        """
        pass

    def register_category_modifier(self, handler: Callable):
        """
        Метод регистрирует обработчик команды кнопки, изменяющий категорию.
        Менять можно родителя и название категории.
        # FIXME:
        Возможно вместо handler: Callable
        должно быть handler: Callable[[Category], None]
        """
        pass

    def set_expense_list(self, handler: [Expense]) -> None:
        """
        Метод воссоздает список расходов из базы данных и
        и добавляет его в графический интерфейс (GUI).
        # FIXME:
        Возможно вместо handler: [Expense]
        должно быть cat: list[Expense]
        """
        pass

    def register_expense_deleter(self, handler: Callable) -> None:
        """
        Метод регистрирует обработчик команды кнопки, удаляющей расходную операцию.
        """
        pass

    def register_expense_adder(self, handler: Callable) -> None:
        """
        Метод регистрирует обработчик команды кнопки, удаляющей расходную операцию.
        """
        pass

    def register_expense_modifier(self, handler: Callable):
        """
        Метод регистрирует обработчик команды кнопки, изменяющий расходную операцию.
        Менять можно родителя и название категории.
        # FIXME:
        Возможно вместо handler: Callable
        должно быть handler: Callable[[Category], None]
        """
        pass

    def set_budget_list(self, cat: list[Budget]) -> None:
        """
        Метод воссоздает список бюджетов из базы данных и
        и добавляет его в графический интерфейс (GUI)
        # FIXME:
        Возможно вместо handler: [Budget]
        должно быть cat: list[Budget]
        """
        pass
