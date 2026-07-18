
# import pytest
# import cards


# @pytest.mark.parametrize("start_state", ["done", "in prog", "todo"])
# def test_finish_simple(cards_db, start_state):
#     c = cards.Card("write a book", state=start_state)
#     index = cards_db.add_card(c)
#     cards_db.finish(index)
#     assert cards_db.get_card(index).state == "done"





import pytest
import cards
 
 
@pytest.mark.parametrize(
    "start_summary, start_state",
    [
        ("write a book", "done"),
        ("second edition", "in prog"),
        ("create a course", "todo"),
    ],
)
def test_finish(cards_db, start_summary, start_state):
    initial_card = cards.Card(summary=start_summary, state=start_state)
    index = cards_db.add_card(initial_card)
    cards_db.finish(index)
    assert cards_db.get_card(index).state == "done"