from bookkeeper.bookkeeper.repository.sqlite_repository import SQLiteRepository

import pytest

@pytest.fixture
def custom_class():
    class Custom():
        pk = 0

    return Custom

@pytest.fixture
def custom_db_file():
    db_file = 'db_file.db'

    return db_file

@pytest.fixture
def custom_class():
    class Custom():
        pk = 0

    return Custom

@pytest.fixture
def repo():
    return SQLiteRepository()