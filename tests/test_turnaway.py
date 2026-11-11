from avphdresearch.turnaway import matches_turnaway, normalise_text


def test_denied_entry():
    assert matches_turnaway("We were denied access to the lounge.")


def test_turn_away():
    assert matches_turnaway("They turned us away.")


def test_unrelated():
    assert not matches_turnaway("The lounge had comfortable seats.")


def test_cleanup():
    assert normalise_text("lin Access x000D denied") == "Access denied"
