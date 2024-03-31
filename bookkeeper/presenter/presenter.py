
from bookkeeper.bookkeeper.view.abstract_view import AbstractView
from bookkeeper.bookkeeper.repository.memory_repository import MemoryRepository
from bookkeeper.bookkeeper.models.expense import Expense
from bookkeeper.bookkeeper.models.category import Category

class Presenter:
    def __init__(self,
                 view: AbstractView,  # DIP
                 ):
        self.view = view

        self.category_repository = MemoryRepository[Category]()
        self.cats = self.category_repository.get_all()
        self.view.set_category_list(self.cats)
        self.view.register_cat_modifier(self.modify_cat)

    def modify_cat(self, cat: Category) -> None:
        self.category_repository.update(cat)
        self.view.set_category_list(self.cats)