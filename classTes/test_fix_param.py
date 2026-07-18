import pytest
import cards
 
 
@pytest.fixture(params=["done", "in prog", "todo"])
def start_state(request):
    return request.param
 
 
def test_finish(cards_db, start_state):
    c = cards.Card("write a book", state=start_state)
    index = cards_db.add_card(c)
    cards_db.finish(index)
    assert cards_db.get_card(index).state == "done"