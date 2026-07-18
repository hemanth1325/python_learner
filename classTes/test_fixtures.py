import pytest
from cards import CardsDB
from tempfile import TemporaryDirectory
from pathlib import Path
import cards
@pytest.fixture()
def cards_db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db  #test runs here
        db.close() #tear down code runs here
def test_empty_db(cards_db):
    assert cards_db.count() == 0