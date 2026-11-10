from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    cpf: str
    email: str
    idade: int
    altura: float