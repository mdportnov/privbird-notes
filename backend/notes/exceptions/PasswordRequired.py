from privbird.exceptions.shared.ApiException import ApiException


class PasswordRequiredException(ApiException):
    status_code = 403
    en = 'This note has a password. You must enter it to view the information'
    ru = 'Эта заметка защищена паролем. Тебе нужно ввести его, чтобы просмотреть информацию'
