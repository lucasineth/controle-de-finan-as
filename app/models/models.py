
from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from app.models.enums import Bancos, Status, Tipos
from app.models.database import engine

class Conta(SQLModel, table=True):
    id: int = Field(primary_key=True)
    valor: float
    banco: Bancos = Field(default=Bancos.NUBANK)
    status: Status = Field(default=Status.ATIVO)

class Historico(SQLModel, table=True):
    id: int = Field(primary_key=True)
    conta_id: int = Field(foreign_key="conta.id")
    conta: Conta = Relationship()
    tipo: Tipos = Field(default=Tipos.ENTRADA)
    valor: float
    data: date

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()
