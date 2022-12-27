from enum import Enum


class Network(Enum):
    HTTPS = 'HTTPS'
    TOR = 'TOR'
    I2P = 'I2P'

    def __str__(self) -> str:
        return self.name
