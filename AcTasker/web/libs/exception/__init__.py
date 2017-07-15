class NotFoundException(Exception):
    code = 404

    def __init__(self, message):
        self.message = message


class BadRequestException(Exception):
    code = 400

    def __init__(self, message):
        self.message = message


class ForbiddenException(Exception):
    code = 403

    def __init__(self, message):
        self.message = message


class UnauthorizedException(Exception):
    code = 401

    def __init__(self, message):
        self.message = message
