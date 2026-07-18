import pytest
import cards
from packaging.version import parse
from cards import Card

def test_less_than():
    c1 = Card("task a"); c2 = Card("task b")
    assert c1 < c2

@pytest.mark.xfail(reason="xpass demo")
def test_xpass():
    c1 = Card("task a"); c2 = Card("task a")
    assert c1 == c2

@pytest.mark.xfail(reason="strict demo",strict=True)
def test_xfail_strict():
    c1 = Card("task a"); c2 = Card("task a")
    assert c1 == c2