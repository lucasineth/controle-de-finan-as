from enum import Enum

class Bancos(Enum):
    NUBANK = 'NUBANK'
    INTER = 'INTER'
    PICPAY = 'PICPAY'

class Status(Enum):
    ATIVO = 'ATIVO'
    INATIVO = 'INATIVO'

class Tipos(Enum):
    ENTRADA = 'ENTRADA'
    SAIDA = 'SAIDA'
