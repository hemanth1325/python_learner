import pytest
from cards import Card,InvalidCardId

@pytest.mark.smoke
def test_start(cards_db):
    """ start change start from todo to in prog to done """
    c = Card("write a book", state="todo")
    i = cards_db.add_card(c)
    cards_db.start(i)
    assert cards_db.get_card(i).state == "in prog"
@pytest.mark.exception
def test_start_non_existent(cards_db):
    any_number=123
    with pytest.raises(InvalidCardId):
        cards_db.start(any_number)

