from cards import Card

def test_equality_fail():
    c1 = Card(summary="something", owner="hemanth")
    c2 = Card(summary="send email", owner="sachin")
    assert c1 == c2

if __name__ == "__main__":
    test_equality_fail()
    