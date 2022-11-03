from privbird.exceptions.shared.ApiException import ApiException


class NoteNotFoundException(ApiException):
    status_code = 404
    en = 'Could not find a note'
    ru = 'Не удалось найти заметку'
