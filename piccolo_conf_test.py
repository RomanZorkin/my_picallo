from piccolo_conf import *  # noqa


DB = PostgresEngine(
    config={
        "database": "piccolo_admin",
        "user": "vasy",
        "password": "123",
        "host": "0.0.0.0",
        "port": 5432,
    }
)
