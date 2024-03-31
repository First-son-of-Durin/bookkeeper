"""
Модуль содержит описание абстрактного представления

ПОКА ЧТО ПРОСТО КОПИЯ abstract_repository.py

Репозиторий реализует хранение объектов, присваивая каждому объекту уникальный
идентификатор в атрибуте pk (primary key). Объекты, которые могут быть сохранены
в репозитории, должны поддерживать добавление атрибута pk и не должны
использовать его для иных целей.
"""

from abc import ABC, abstractmethod
from typing import Protocol
from collections.abc import Callable
from bookkeeper.bookkeeper.models.category import Category

class AbstractView(Protocol):
    def set_category_list(cat: list[Category]) -> None:
        pass

    def register_cat_modifier(
            handler: Callable[[Category],None]):
        pass


class AbstractView(ABC):
    """
    Абстрактное представления.
    Абстрактные методы:
    пока не известно
    """

    @abstractmethod
    def add(self) -> int:
        """
        Добавить объект в репозиторий, вернуть id объекта,
        также записать id в атрибут pk.
        """

    @abstractmethod
    def get(self) -> None:
        """ Получить объект по id """

    @abstractmethod
    def get_all(self) -> None:
        """
        Получить все записи по некоторому условию
        where - условие в виде словаря {'название_поля': значение}
        если условие не задано (по умолчанию), вернуть все записи
        """

    @abstractmethod
    def update(self) -> None:
        """ Обновить данные об объекте. Объект должен содержать поле pk. """

    @abstractmethod
    def delete(self) -> None:
        """ Удалить запись """
