import pytest
from src.app.core.database import get_db


def test_database_url_replacement(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgres://placeholder_url")

    import importlib
    import src.app.core.database

    importlib.reload(src.app.core.database)

    assert src.app.core.database.DATABASE_URL.startswith("postgresql://")


def test_get_db_generator():
    generator = get_db()
    db_session = next(generator)

    assert db_session is not None

    with pytest.raises(StopIteration):
        next(generator)
