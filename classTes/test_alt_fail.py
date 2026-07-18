import pytest
from cards import Card

def test_with_fail():
    c1 = Card(summary="something", owner="hemanth")
    c2 = Card(summary="send email", owner="sachin")
    if c1 != c2:
        pytest.fail("they are not equal")