from typing import Tuple

from models import EscapeRoom
from models.visit import IncorrectDurationError, IncorrectRatingError, EscapeRoomClosedError, IncorrectDateError

messages = {IncorrectDurationError: "Nie można zarejestrować wizyty: czas wizyty nie może być mniejszy od 0.",
            IncorrectRatingError: "Nie można zarejestrować wizyty: ocena musi być z przedziału 1-5.",
            IncorrectDateError: "Nie można zarejestrować wizyty: podana data jest nieprawidłowa."}


def get_error_message(exception: Exception, escape_room: EscapeRoom) -> Tuple[str, str]:
    if exception.__class__ == EscapeRoomClosedError:
        return (f"Nie można zarejestrować wizyty: wybany Escape Room był nieczynny w podanej dacie.",
               f"\n(data otwarcia: {escape_room.opening_date}"
               f"{'' if escape_room.closing_date is None else ', data zamknięcia: '+ escape_room.closing_date.__str__()})")
    return messages.get(exception.__class__, "Wystąpił nieznany błąd. Wizyta nie została zarejestrowana"), ""
