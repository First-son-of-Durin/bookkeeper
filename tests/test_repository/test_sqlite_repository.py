from bookkeeper.bookkeeper.repository.sqlite_repository import SQLiteRepository

import pytest


@pytest.fixture
def custom_class():
    class Expense():
        amount: int = 0
        category: int = 0
        expense_date: str = ''
        added_date: str = ''
        comment: str = ''
        pk: int = 0

        def __eq__(self, other) -> bool:
            return (self.pk == other.pk
                    and self.amount == other.amount
                    and self.category == other.category
                    and self.expense_date == other.expense_date
                    and self.added_date == other.added_date
                    and self.comment == other.comment)

    return Expense


@pytest.fixture
def custom_db_file():
    db_file = 'db_file.db'

    return db_file


@pytest.fixture
def repo(custom_db_file, custom_class):
    return SQLiteRepository(custom_db_file, custom_class)


def test_crud(repo, custom_class):

    obj = custom_class()
    pk = repo.add(obj)
    assert obj.pk == pk
    assert repo.get(pk) == obj
    obj2 = custom_class()
    obj2.pk = pk
    repo.update(obj2)
    assert repo.get(pk) == obj2
    repo.delete(pk)
    assert repo.get(pk) is None


def test_cannot_add_with_pk(repo, custom_class):
    obj = custom_class()
    obj.pk = 1
    with pytest.raises(ValueError):
        repo.add(obj)


def test_cannot_add_without_pk(repo):
    with pytest.raises(ValueError):
        repo.add(0)


def test_cannot_delete_unexistent(repo):
    with pytest.raises(KeyError):
        repo.delete(1)


def test_get_all(repo, custom_class):
    objects = [custom_class() for i in range(5)]
    for o in objects:
        repo.add(o)
    obj = repo.get_all()
    assert obj == objects

def test_get_all_with_condition(repo, custom_class):
    objects = []
    for i in range(5):
        o = custom_class()
        o.amount = 0
        o.category = i
        o.expense_date = 'test'
        o.added_date = ''
        o.comment = ''
        repo.add(o)
        objects.append(o)
    res_get_all = repo.get_all({'category': '2'})
    print(res_get_all)
    print([objects[2]])
    assert res_get_all == [objects[2]]

    res_get_all = repo.get_all({'expense_date': 'test'})
    print(res_get_all)
    print([objects])
    assert res_get_all == objects
