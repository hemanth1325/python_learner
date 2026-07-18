import pytest
from tempfile import TemporaryDirectory
from pathlib import Path
import cards
@pytest.fixture(scope="module")
def cards_db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db  #test runs here
        db.close() #tear down code runs here



def test_empty_db(cards_db):
    assert cards_db.count() == 0
def add_card():
    card1 = cards.Card(summary="card1", owner="hemanth")
    return card1

def add_card2():   
    card2 = cards.Card(summary="card2", owner="sachin")
    return card2
def test_two(cards_db):
    c1 = add_card()
    c2 = add_card2()
    
    cards_db.add_card(c1)
    cards_db.add_card(c2)
    assert cards_db.count() == 2