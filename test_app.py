from app import add

def test_addition():
    # Wir prüfen: Ist 2 + 3 wirklich 5?
    assert add(2, 3) == 5
    # Wir prüfen: Ist 10 + 0 wirklich 10?
    assert add(10, 0) == 10