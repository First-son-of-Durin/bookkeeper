from bookkeeper.bookkeeper.repository.sqlite_repository import SQLiteRepository

import pytest

@pytest.fixture
def custom_class():
    class Custom():
        pk: int = 0
        ID: int = 2
        Name: str = 'orange'
        Value: float = 50

        def __eq__(self, other) -> bool:
            return (self.pk == other.pk
                    and self.ID == other.ID
                    and self.Name == other.Name
                    and self.Value == other.Value)

    return Custom

@pytest.fixture
def custom_obj():
    class Obj():
        pk: int = 0
        ID: int = 2
        Name: str = 'orange'
        Value: float = 50

    return Obj

@pytest.fixture
def custom_db_file():
    db_file = 'db_file.db'

    return db_file


@pytest.fixture
def repo(custom_db_file, custom_class):
    return SQLiteRepository(custom_db_file, custom_class)


def test_crud(repo, custom_class,custom_obj):
    obj = custom_class()
    pk = repo.add(obj)
#    print(pk)
    obj2 = custom_class()
    pk2 = repo.add(obj2)
#    print(pk2)
    assert obj.pk == pk
#    print(repo.get(pk))
#    print(obj)
    assert repo.get(pk) == obj
    obj2 = custom_class()
    obj2.pk = pk
    repo.update(obj2)
    assert repo.get(pk) == obj2
    repo.delete(pk)
    assert repo.get(pk) is None
