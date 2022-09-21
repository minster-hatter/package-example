from foo import baz


def test_ouput():
    assert baz.pythons() == [
        "Idle",
        "Cleese",
        "Gilliam",
        "Jones",
        "Palin",
        "Chapman",
    ]
