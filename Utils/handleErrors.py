from rest_framework import status
from rest_framework.exceptions import APIException

class AppException(APIException):
    def __init__(self, source, code, message):
        super().__init__(message)
        self.status_code = code
        self._source = source

    @property
    def source(self):
        return self._source

class BadRequestException(AppException):
    def __init__(self, errors=None):
        if not errors:
            errors = 'Bad request'

        super().__init__(source='', code=status.HTTP_400_BAD_REQUEST, message=errors)