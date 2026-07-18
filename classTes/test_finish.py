import pytest
from cards import Card, InvalidCardId
 
pytestmark = pytest.mark.finish
 
@pytest.mark.smoke
class TestFinish:
   
    def test_finish_from_todo(self, cards_db):
        i = cards_db.add_card(Card("foo", state="todo"))
        cards_db.finish(i)
        assert cards_db.get_card(i).state == "done"
 
    def test_finish_from_in_prog(self, cards_db):
        i = cards_db.add_card(Card("foo", state="in prog"))
        cards_db.finish(i)
        assert cards_db.get_card(i).state == "done"
 



    def test_finish_from_done(self, cards_db):
        i = cards_db.add_card(Card("foo", state="done"))
        cards_db.finish(i)
        assert cards_db.get_card(i).state == "done"





@pytest.mark.parametrize(
    "start_state", ["todo",pytest.param("in prog", marks=pytest.mark.smoke), "done"],

)

def test_finish_param(cards_db, start_state):
    i = cards_db.add_card(Card("foo", state=start_state))
    cards_db.finish(i)
    assert cards_db.get_card(i).state == "done"


@pytest.fixture(
    params=["todo",pytest.param("in prog", marks=pytest.mark.smoke), "done"],


)

def start_fixture(request):
    return request.param

def test_finish_fix(cards_db, start_fixture):
    i = cards_db.add_card(Card("foo", state=start_fixture))
    cards_db.finish(i)
    c= cards_db.get_card(i)
    assert cards_db.get_card(i).state == "done"



@pytest.mark.smoke
@pytest.mark.exception
def test_finish_non_existent(cards_db):
    any_number=123
    with pytest.raises(InvalidCardId):
        cards_db.finish(any_number)