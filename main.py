from bookkeeper.repository.memory_repository import MemoryRepository

class Custom():
    pk = 0

MyRepo = MemoryRepository()

obj1 = Custom()
pk1 = MyRepo.add(obj1)
#print(pk1)
#print(type(pk1))
#print(type(MyRepo.get(pk1)))

obj2 = Custom()
pk2 = MyRepo.add(obj2)

#print(MyRepo.get_all())

import sqlite3
from inspect import get_annotations
from bookkeeper.repository.sqlite_repository import SQLiteRepository

class Custom():
        pk: int = 0
        ID: int = 2
        Name: str = 'orange'
        Value: float = 50

SQLRepo = SQLiteRepository('db_file.db', Custom)

con = sqlite3.connect('db_file.db')
cursor = con.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS custom(ID INTEGER, Name TEXT, VALUE REAL)')
con.commit()
con.close()

obj1 = Custom()

cls_type = obj1.__class__
print(cls_type)
values = [get_annotations(cls_type, eval_str=True)]
print(values)

obj2 = cls_type()
print(obj2)
print(getattr(obj2,'Name'))
setattr(obj2,'Name','FUUUUUCK')
print(getattr(obj2,'Name'))



pk1 = SQLRepo.add(obj1)
#print(SQLRepo.get(pk1))

'''

con = sqlite3.connect('test.db')
cursor = con.cursor()

cursor.execute(
    CREATE TABLE IF NOT EXISTS Products(
        ProductID INTEGER PRIMARY KEY,
        ProductName TEXT,
        CaloriesPer100g REAL
    )
)
con.commit()
con.close()

class Custom():
    pk: int = 0

class Products():
    pk: int = 0
    ProductID: int = 2
    ProductName: str = 'orange'
    CaloriesPer100g: float = 50

#print(Custom_cls.__name__.lower())
#print(get_annotations(Custom_cls, eval_str=True))

SQLRepo = SQLiteRepository('test.db',Products)

obj1 = Products()
pk1 = SQLRepo.add(obj1)
# print(SQLRepo.get(pk1))
'''
