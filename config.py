import os


class CONFIG:
    DEV = (os.environ.get('DEBUG') == 'ENABLE')

    class DB:

        class DEVELOPMENT:
            schema = 'mysql+pymysql'
            username = 'acque2two'
            password = 'password'
            hostname = '127.0.0.1'
            database = 'actasker'
            settings = {"charset": 'utf8mb4'}

            def generate_uri(schema, username, password, hostname, database, settings):
                uri = ('%s://%s:%s@%s/%s' % (schema, username, password, hostname, database))
                f = False
                for s in settings.items():
                    uri += '?%s=%s' % (s[0], s[1]) if not f else '&%s=%s' % (s[0], s[1])
                    f = True
                return uri

            uri = generate_uri(schema, username, password, hostname, database, settings)

        class PRODUCTION:
            schema = 'mysql+pymysql'
            username = 'acque2two'
            password = 'database_connect'
            hostname = ''
            database = 'actasker'

            settings = {"unix_socket": '/cloudsql/' + os.environ.get('DB_PATH') if os.environ.get('DB_PATH') is not None else "",
                        "charset":     'utf8mb4'}

            def generate_uri(schema, username, password, hostname, database, settings):
                uri = ('%s://%s:%s@%s/%s' % (schema, username, password, hostname, database))
                f = False
                for s in settings.items():
                    uri += '?%s=%s' % (s[0], s[1]) if not f else '&%s=%s' % (s[0], s[1])
                    f = True
                return uri

            uri = generate_uri(schema, username, password, hostname, database, settings)

    class CACHE:
        pass

    class FLASK:
        class DEVELOPMENT:
            DEBUG = True
            TESTING = True
            SECRET_KEY = "DEBUGGING_KEY"
            SESSION_COOKIE_NAME = "SESSION"
            SESSION_COOKIE_HTTPONLY = False
            PORT = 28888
            pass

        class PRODUCTION:
            SECRET_KEY = "yy81wiBuqVEbWTxao7YcdT9JZDXbuL1Efj7EarGvA3Gv1Gyum1crSh90VMNroeAu" \
                         "frF3ynar6s6WT4edbaNXsvgpbmOq0LemKylSwsn4KEIX8qFHJBEbRBLxyjT3B43w" \
                         "gQN6NNufJSRPYwbfbblRf9lnaOEZWpA2PqdjWoONcJS0JUIcGINGpC7gP62tReiA" \
                         "Ac1WALGRscS5Z1jYjkqdQuWtDKf8Ij8oVE12w4LeUeIpk7UGYovu0QtjxxrJlds3" \
                         "wSdvDEGowgdPT4iZOy9IXFLq95UmkjbXNglWVni3CkRhcyRiXr914sz7fGGmY1GR" \
                         "Z3lFvk76ojAtVuPnqqZMbLgg6ya71kfeHJ2qykrlg9vR7i1zIoJzktqeVAfJETVM" \
                         "WskdN9iKFViebqKOoQF5mATUtmhQ9tDrdqUG4QYZST2s25rLWOhO6Gjkt7KPBkBl" \
                         "XkHhOmbOjz8mGNHihgbjI0m5I5GkoLagYGF7bd1MmpAF2MRH89VKeAmJRKh9VLNB"
            SESSION_COOKIE_NAME = "nkUqAqGk01uQVrSjEwXaRpZz"
            SESSION_COOKIE_HTTPONLY = False
            PORT = 8080

            pass
