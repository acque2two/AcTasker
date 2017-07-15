from flask import request, render_template


class Error(dict):
    class Detail(dict):
        def __init__(self, title='Unknown', message='Unknown error. Please contact us.'):
            self['title'] = title
            self['message'] = message

    def __init__(self, type='', code=-1, title='', detail='', details=None, __dict=None):
        if __dict is not None:
            self['type'] = __dict.get(type, None)
            self['title'] = __dict.get(title, None)
            self['detail'] = __dict.get(detail, None)
            self['details'] = __dict.get(details, None) if __dict.get(type, None) is not None else []
        else:
            self['type'] = type
            self['title'] = title
            self['detail'] = detail
            self['details'] = details if details is not None else []

        self['status'] = code
        self['endpoint'] = request.path

    def add_detail(self, title, message):
        self['details'].append({'title': title, 'message': message})

    @staticmethod
    def common_error(title='', detail='', details=None, code=-1):
        if details is None:
            details = []
        return render_template("error.html", **Error(title=title, detail=detail, details=details, code=code))

    @staticmethod
    def not_implemented(title='Not implemented', detail='This endpoint isn\'t implemented.', details=None):
        return Error.common_error(title=title, detail=detail, details=details, code=501), 501

    @staticmethod
    def unauthorized(title='Unauthorized', detail='You are unauthorized. Please login.', details=None):
        return Error.common_error(title=title, detail=detail, details=details, code=400), 400

    @staticmethod
    def not_found(title='requested data not found.', detail='The request was understanding. but requested data is not '
                                                            'found. Please check your request.', details=None):
        return Error.common_error(title=title, detail=detail, details=details, code=404), 404

    @staticmethod
    def forbidden(title='Operation not permitted.', detail='You not have permission access this endpoint. Please '
                                                           'contact administrator if you need permission for use this'
                                                           ' endpoint.', details=None):
        return Error.common_error(title=title, detail=detail, details=details, code=403), 403

    @staticmethod
    def bad_request(title='Bad request', detail='Your requests coundn\'t understanding. Please check your requests.',
                    details=None):
        return Error.common_error(title=title, detail=detail, details=details, code=401), 401
