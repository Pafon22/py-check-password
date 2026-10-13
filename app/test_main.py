import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password: str, result: str",
    [
        ("Pass@word1", True),
        ("54#Ds@word1", True),
        ("TeStInGH&R3", True)
    ]
)
def test_check_password(password: str, result: str) -> None:
    assert check_password(password) == result


@pytest.mark.parametrize(
    "password: str, result: str",
    [
        ("noSpeci4lSymb0ls", False),
        ("N0Symb0ls", False),
        ("DontPut5ymb0ls", False)
    ]
)
def test_check_password_without_symbols(password: str, result: str) -> None:
    assert check_password(password) == result


@pytest.mark.parametrize(
    "password: str, result: str",
    [
        ("Nodigits!", False),
        ("Str@ng", False)
    ]
)
def test_check_password_without_numbers(password: str, result: str) -> None:
    assert check_password(password) == result


@pytest.mark.parametrize(
    "password: str, result: str",
    [
        ("noupperc4se?", False),
        ("1twork3d#", False)
    ]
)
def test_check_password_without_upper_case(password: str, result: str) -> None:
    assert check_password(password) == result


@pytest.mark.parametrize(
    "password: str, result: str",
    [
        ("$h0rT", False),
        ("L1tTl#", False)
    ]
)
def test_check_short_password(password: str, result: str) -> None:
    assert check_password(password) == result


@pytest.mark.parametrize(
    "password: str, result: str",
    [
        ("$0L0ngN0W$0L0ngN0W", False),
        ("L0NG#P4$$Word$N0W##", False)
    ]
)
def test_check_long_password(password: str, result: str) -> None:
    assert check_password(password) == result
