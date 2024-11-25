from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from project.config.database import db

Base = declarative_base()

class Usuario(Base):
    #Definindo Características da tabela no banco.
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(180))
    email = Column(String(180))
    senha = Column(String(100))

    #Definindo Características da Classe.;
    def __init__(self, nome:str, email:str, senha:str):
        self.nome = nome
        self.email = email
        self.senha = senha

    def __repr__(self):
        return f"Usuario: \nID: {self.id}\nNome: {self.nome}\nEmail: {self.email}"

Base.metadata.create_all(bind=db)