import pytest, cards
 
 
def test_no_path_raises():
    with pytest.raises(TypeError):
        cards.CardsDB()
 
def test_raises_with_info():
    match_regex = "missing 1 .* positional argument"
    with pytest.raises(TypeError, match=match_regex):
        cards.CardsDB()
 
def test_raises_with_info_alt():
    with pytest.raises(TypeError) as exc_info:
        cards.CardsDB()
 
    assert "missing 1 required" in str(exc_info.value)

