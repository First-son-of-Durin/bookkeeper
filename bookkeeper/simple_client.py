"""
Простой тестовый скрипт для терминала
"""

from bookkeeper.bookkeeper.models.category import Category
from bookkeeper.bookkeeper.models.expense import Expense
from bookkeeper.bookkeeper.repository.memory_repository import MemoryRepository
from bookkeeper.bookkeeper.repository.sqlite_repository import SQLiteRepository
from bookkeeper.bookkeeper.utils import read_tree

cat_repo = MemoryRepository[Category]()
exp_repo = MemoryRepository[Expense]()

#cat_repo = SQLiteRepository('db_file.db',Category)
#exp_repo = SQLiteRepository('db_file.db',Expense)

cats = '''
продукты
    мясо
        сырое мясо
        мясные продукты
    сладости
книги
одежда
'''.splitlines()

Category.create_from_tree(read_tree(cats), cat_repo)

while True:
    try:
        cmd = input('$> ')
    except EOFError:
        break
    if not cmd:
        continue
    if cmd == 'категории':
        print(*cat_repo.get_all(), sep='\n')
    elif cmd == 'расходы':
        print(*exp_repo.get_all(), sep='\n')
    elif cmd[0].isdecimal():
        amount, name = cmd.split(maxsplit=1)
        try:
            cat = cat_repo.get_all({'name': name})[0]
        except IndexError:
            print(f'категория {name} не найдена')
            continue
        exp = Expense(float(amount), cat.pk)
        exp_repo.add(exp)
        print(exp)
