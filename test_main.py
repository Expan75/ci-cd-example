from main import welcome_message


def test_welcome_message():
    res = welcome_message("Erik")
    assert "Welcome Erik" in res
