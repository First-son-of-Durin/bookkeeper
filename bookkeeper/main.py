"""
Модуль содержит запуск приложения
"""

import sys
import sqlite3

from bookkeeper.bookkeeper.repository.memory_repository import MemoryRepository
from bookkeeper.bookkeeper.repository.sqlite_repository import SQLiteRepository
from bookkeeper.bookkeeper.models.expense import Expense
from bookkeeper.bookkeeper.models.category import Category
from bookkeeper.bookkeeper.view.presenter import Presenter
from bookkeeper.bookkeeper.utils import read_tree

# Bookkeeper.db - БД (SQL), где содержатся списки расходов, категорий и бюджетов

SQLRepoExpenses = SQLiteRepository('Bookkeeper.db', Expense)
con = sqlite3.connect(SQLRepoExpenses.db_file)
cursor = con.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS expense(amount INT, category INT, '
               'expense_date TEXT, added_date TEXT, comment TEXT)')
con.commit()
con.close()

SQLRepoCategories = SQLiteRepository('Bookkeeper.db', Category)
con = sqlite3.connect(SQLRepoCategories.db_file)
cursor = con.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS category(name TEXT, parent INTEGER)')
con.commit()
con.close()

cats = '''
продукты
    мясо
        сырое мясо
        мясные продукты
    сладости
книги
одежда
'''.splitlines()

Category.create_from_tree(read_tree(cats), SQLRepoCategories)

"""
SQLRepoBudget = SQLiteRepository('Bookkeeper.db', Expense)
con = sqlite3.connect(SQLRepoBudget.db_file)
cursor = con.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS budget(duration TEXT, budget REAL)')
con.commit()
con.close()
"""
bookkeeper = Presenter(SQLRepoExpenses,SQLRepoCategories)
bookkeeper.view.window.show()
sys.exit(bookkeeper.view.app.exec())

