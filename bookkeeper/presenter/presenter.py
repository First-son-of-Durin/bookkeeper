from setuptools.config._validate_pyproject import ValidationError

from bookkeeper.bookkeeper.view.abstract_view import AbstractView
from bookkeeper.bookkeeper.repository.abstract_repository import AbstractRepository, T
from bookkeeper.bookkeeper.repository.memory_repository import MemoryRepository
from bookkeeper.bookkeeper.models.expense import Expense
from bookkeeper.bookkeeper.models.category import Category
from bookkeeper.bookkeeper.models.budget import Budget

class Presenter:
    def __init__(self,
                 view: AbstractView, repo: AbstractRepository[T]  # DIP
                 ):

        self.view = view

        self.category_repository = MemoryRepository[Category]()
        self.cats = self.category_repository.get_all()
        self.view.set_category_list(self.cats)

        self.budget_repository = MemoryRepository[Budget]()
        self.buds = self.budget_repository.get_all()
        self.view.set_budget_list(self.buds)

        self.expense_repository = MemoryRepository[Expense]()
        self.exps = self.expense_repository.get_all()
        self.view.set_expense_list(self.exps)

        self.view.register_cat_modifier(self.modify_cat)

    def modify_cat(self, cat: Category) -> None:
        if Category.name in [c.name for c in self.cats]:
            raise ValidationError(
                f'Категория {Category.name} уже существует')
        self.category_repository.update(cat)
        self.view.set_category_list(self.cats)

    def add_category(self, name, parent) -> None:
        if name in [c.name for c in self.cats]:
            raise ValidationError(
                f'Категория {name} уже существует')
        cat = Category(name, parent)
        self.category_repository.add(cat)
        self.cats.append(cat)
        self.view.set_category_list(self.cats)
