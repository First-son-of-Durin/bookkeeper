'''
from bookkeeper.repository.memory_repository import MemoryRepository

class Custom():
    pk = 0

MyRepo = MemoryRepository()

obj1 = Custom()
pk1 = MyRepo.add(obj1)
print(MyRepo.get(pk1))

obj2 = Custom()
pk2 = MyRepo.add(obj2)

print(MyRepo.get_all())
'''

import sqlite3

con = sqlite3.connect('test.db')
cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
        ProductID INTEGER PRIMARY KEY,
        ProductName TEXT,
        CaloriesPer100g REAL
    )
''')
con.commit()
con.close()


from bookkeeper.repository.sqlite_repository import SQLiteRepository

class Custom():
    pk = 0

SQLRepo = SQLiteRepository('test.db',)