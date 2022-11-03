from privbird.exceptions.shared.ApiException import ApiException


class InvalidPasswordException(ApiException):
    status_code = 403
    en = 'You have entered the wrong password. Try again'
    ru = 'Ты ввел неправильный пароль. Пробуй снова'
