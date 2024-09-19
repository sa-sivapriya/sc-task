from dataclasses import dataclass

@dataclass
class DBData:
    host: str = "localhost"
    dbname: str = "Ransomware"
    user: str = "postgres"
    password: str = "password"
    port: int = 5432