from models.visit import IncorrectDurationError, IncorrectRatingError, EscapeRoomClosedError, IncorrectDateError

messages = {IncorrectDurationError: "Nie można zarejestrować wizyty: czas wizyty nie może być mniejszy od 0.",
            IncorrectRatingError: "Nie można zarejestrować wizyty: ocena musi być z przedziału 1-5.",
            EscapeRoomClosedError: "Nie można zarejestrować wizyty: wybany Escape Room był nieczynny w podanej dacie.",
            IncorrectDateError: "Nie można zarejestrować wizyty: podana data jest nieprawidłowa."}


def get_error_message(exception: Exception) -> str:
    return messages.get(exception.__class__, "Wystąpił nieznany błąd. Wizyta nie została zarejestrowana")
