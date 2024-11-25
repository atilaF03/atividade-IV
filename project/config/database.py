
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

#Parâmetros para Conexão com o Banco.

db_user = "user"
db_password = "user_password"
db_host = "localhost"
db_port = "3306"
db_name = "my_database"

#Caminho de Conexão com o Banco de Dados.

DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

#Conetando ao Banco

db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=db)
session = Session()

#Gerenciando a Conexão com o Banco.

@contextmanager
def get_db():
    db = Session()
    try:
        yield db
        db.commit()
    except Exception as erro:
        db.rollback()
        raise erro
    finally: 
        db.close()
