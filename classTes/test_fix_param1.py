import pytest
from cards import Card
 
@pytest.fixture(params=["done", "in prog", "todo"])
def start_state(request):
    return request.param
@pytest.fixture(params=["write a book", "write a letter", "write a poem"])
def start_summary(request):
    return request.param
 
def test_finish(cards_db, start_state, start_summary):
    c = Card(summary=start_summary, state=start_state)
    index = cards_db.add_card(c)
    cards_db.finish(index)
    assert cards_db.get_card(index).state == "done"