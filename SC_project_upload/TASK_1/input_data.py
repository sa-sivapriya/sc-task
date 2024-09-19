from dataclasses import dataclass

class DBData:
    host: str = "localhost"
    dbname: str = "Product"
    user: str = "postgres"
    password: str = "password"
    port: int = 5432

class AccessData:
    secret_key: str = 'abcdefgh'
    jwt_secret_key: str = 'zyxwvuts'
    jwt_secret_admin_key: str = 'zyxwvutskk'
    jwt_token_location: list = ['headers']
    