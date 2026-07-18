import cards
import pytest
from cards import Card
from packaging.version import parse


@pytest.mark.skipif(
        parse(cards.__version__).major < 2, 
        reason="Not implemented ")


def test_less_than():
    c1 = Card("task a")
    c2 = Card("task b")
    assert c1 < c2