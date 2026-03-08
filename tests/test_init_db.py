from src.app.core.init_db import init_db


def test_init_db_runs():
    init_db()
    assert True
