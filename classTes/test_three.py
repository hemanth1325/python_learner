import cards

def test_three(cards_db):
    cards_db.add_card(cards.Card("one"))
    cards_db.add_card(cards.Card("two"))
    cards_db.add_card(cards.Card("three"))