from django.contrib.auth import get_user_model


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username="deleted")[0]


class NotMatchingPasswordsError(ValueError):
    """raise this when two passwords in registration form are not matching"""


def check_passwords_match(password, password2):
    if password != password2:
        raise NotMatchingPasswordsError("passwords are not the same")


ERROR_MESSAGE = {
    "user_exists": "Podany użytkownik istnieje w naszej bazie. Zaloguj się na swoje konto.",
    "passwords_not_matching": "Wpisz dwukrotnie to samo hasło.",
    "empty_email": "Pole email nie może byc puste.",
    "not_authenticted": "Spróbuj ponownie.",
    "no_user": "Brak użytkownika o podamym loginie"
}
SUCCESS_MESSAGE = {
    "new_user": "Utworzono użytkownika. Zaloguj się.",
    "authenticated": "Zalogowano",
}
