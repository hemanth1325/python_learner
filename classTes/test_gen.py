from cards import Card

def pytest_generate_tests(metafunc):
    if "start_state" in metafunc.fixturenames:
        metafunc.parametrize("start_state", ["done", "in prog", "todo"])
    if "start_summary" in metafunc.fixturenames:
        metafunc.parametrize(
            "start_summary", ["write a book", "write a letter", "write a poem","testing"]
        )

def test_finish(cards_db, start_state, start_summary):
    c = Card(summary=start_summary, state=start_state)
    index = cards_db.add_card(c)
    cards_db.finish(index)
    assert cards_db.get_card(index).state == "done"