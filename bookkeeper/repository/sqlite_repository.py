"""
Модуль описывает репозиторий, работающий в sqlite
"""
# from itertools import count
# from typing import Any
from inspect import get_annotations
import sqlite3

from bookkeeper.bookkeeper.repository.abstract_repository import AbstractRepository, T


class SQLiteRepository(AbstractRepository[T]):
    """
    Репозиторий, работающий в работающий в sqlite. Хранит данные в файле .db
    """

    def __init__(self, db_file: str, cls: type) -> None:
        self.db_file = db_file
        self.table_name = cls.__name__.lower()
        self.fields = get_annotations(cls, eval_str=True)
        self.fields.pop('pk')

    def add(self, obj: T) -> int:
        names = ', '.join(self.fields.keys())
        p = ', '.join("?" * len(self.fields))
        values = [getattr(obj, x) for x in self.fields]
        with sqlite3.connect(self.db_file) as con:
            cur = con.cursor()
            cur.execute('PRAGMA foreign_keys = ON')
            cur.execute(
                f'INSERT INTO {self.table_name} ({names}) VALUES ({p})',
                values
            )
            obj.pk = cur.lastrowid
        con.commit()
        con.close()
        return obj.pk

    def get(self, pk: int) -> T | None:
        with sqlite3.connect(self.db_file) as con:
            cur = con.cursor()
            cur.execute('PRAGMA foreign_keys = ON')
            cur.execute(f'SELECT * FROM {self.table_name} WHERE pk = ?', (pk,))
            result = cur.fetchone()
        con.commit()
        con.close()
        '''???? очень непонятно что дальше сделать и как вывести переменную типа T ????'''
        if result:
            return result
        else:
            return None

    def delete(self, pk: int) -> None:
        with sqlite3.connect(self.db_file) as con:
            cur = con.cursor()
            cur.execute('PRAGMA foreign_keys = ON')
            cur.execute(f'DELETE FROM {self.table_name} WHERE pk = ?', (pk,))
        con.commit()
        con.close()

    def update(self, obj: T) -> None:
        if obj.pk == 0:
            raise ValueError('attempt to update object with unknown primary key')
        names = ', '.join(self.fields.keys())
        p = ', '.join("?" * len(self.fields))
        values = [getattr(obj, x) for x in self.fields]
        with sqlite3.connect(self.db_file) as con:
            cur = con.cursor()
            cur.execute('PRAGMA foreign_keys = ON')
            cur.execute(f'UPDATE {self.table_name} SET  WHERE pk = ?', (obj.pk,))
        con.commit()
        con.close()


'''
    def get(self, pk: int) -> T | None:
        return self._container.get(pk)

    def get_all(self, where: dict[str, Any] | None = None) -> list[T]:
        if where is None:
            return list(self._container.values())
        return [obj for obj in self._container.values()
                if all(getattr(obj, attr) == value for attr, value in where.items())]

    def update(self, obj: T) -> None:
        if obj.pk == 0:
            raise ValueError('attempt to update object with unknown primary key')
        self._container[obj.pk] = obj

    def delete(self, pk: int) -> None:
        self._container.pop(pk)
'''
