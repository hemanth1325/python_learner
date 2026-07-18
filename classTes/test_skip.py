import pytest
from cards import Card
@pytest.mark.skip(reason="Not implemented ")
def test_less_than():
    c1 = Card("task a")
    c2 = Card("task b")
    assert c1 < c2