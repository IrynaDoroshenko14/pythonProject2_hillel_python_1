import datetime


def wrap_validate(func):
    def wrapper(*args, **kwargs):
        pw = kwargs.get("password")
        if not pw:
            raise AttributeError(f'no parameter "password" in arguments of function {func.__name__}')
        is_str = is_string(pw)
        valid_len = is_valid_length(pw)
        letters = has_any_symbols(pw, symbols='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
        digits = has_any_symbols(pw, symbols='1234567890')
        specs = has_any_symbols(pw, symbols='!')
        is_secure = is_str and valid_len and letters and digits and specs

        func_str = str(func(*args, **kwargs))
        func_str = truncate_with_dots(func_str)
        result = {'result': func_str,
                  'is_secure': is_secure,
                  }
        return result

    return wrapper


def is_string(password):
    return isinstance(password, str)


def is_valid_length(password, length=10):
    return len(password) >= length


def has_any_symbols(password, symbols):
    contains_symbols = False

    for letter in password:
        if letter in symbols:
            contains_symbols = True

    return contains_symbols


def truncate_with_dots(string, length=100):
    if len(string) > length:
        string = string[:97] + "..."
    return string


@wrap_validate
def registration(id, login, notes, password):
    date = datetime.date.today()
    return f'User {login} created account on {date} with password "{password}". Additional information: {notes}'


if __name__ == '__main__':
    assert is_string("string")
    assert not is_string(123)
    assert not is_string(["string_in_list"])

    assert is_valid_length("1234567890")
    assert is_valid_length("12345678901")
    assert not is_valid_length("123456789")

    assert has_any_symbols("a1!", "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
    assert has_any_symbols("a1!", "1234567890")
    assert has_any_symbols("a1!", "!")
    assert not has_any_symbols("a1!", "?")

    assert len(truncate_with_dots("1234567890"*11)) == 100
    assert truncate_with_dots("1234567890"*11).endswith("...")
    assert len(truncate_with_dots("1234567890" * 9)) == 90

    reg = registration(1, "user_login", "add info", password="abc12345678!")

    assert reg["is_secure"]
    assert "user_login" in reg["result"]
    assert "add info" in reg["result"]
    assert "abc12345678" in reg["result"]
