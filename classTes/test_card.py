from cards import Card 

def test_field_access():
    c = Card(summary="something", owner="hemanth",id=123)
    assert c.summary == "something"
    assert c.owner == "hemanth"
    assert c.state == "todo"
    assert c.id == 123

def test_default_values():
    c = Card()
    assert c.summary is None
    assert c.owner is None
    assert c.state == "todo"
    assert c.id is None


def test_equality():
    c1 = Card(summary="something", owner="hemanth",id=123)
    c2 = Card(summary="something", owner="hemanth",id=123)
    assert c1 == c2


def test_equality_with_diff_ids():
    c1 = Card(summary="something", owner="hemanth",id=123)
    c2 = Card(summary="something", owner="hemanth",id=456)
    assert c1 == c2


def test_inequality():
    c1 = Card(summary="something", owner="hemanth",id=123)
    c2 = Card(summary="sending an email", owner="John",state="in prog" ,id=123)
    assert c1 != c2


def test_from_dict():
    c1 = Card(summary="something", owner="hemanth",state="todo", id=123)
    c2_dict = {"summary": "something", "owner": "hemanth", "state": "todo", "id": 123}
    c2 = Card.from_dict(c2_dict)
    assert c1 == c2

def test_to_dict():
    c1= Card(summary="something", owner="hemanth",state="todo", id=123)
    c2_dict = c1.to_dict()
    c2_expected = {"summary": "something", "owner": "hemanth", "state": "todo", "id": 123}
    assert c2_dict == c2_expected