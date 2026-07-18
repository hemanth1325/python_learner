import cards

def test_non_empty(non_empty_db):
    assert non_empty_db.count() > 0