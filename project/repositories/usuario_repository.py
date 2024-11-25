from project.models.usuario_model import Usuario
from sqlalchemy.orm import Session

class UsuarioRepository:
    def __init__(self, session: Session):
        self.session = session

    def salvar_usuario(self, usuario: Usuario):

        try:
            self.session.add(usuario)
            self.session.commit()
        except Exception as erro:
            self.session.rollback()
            print(f"Erro ao salvar usuário: {erro}")
            raise erro

    def listar_usuarios(self):
        try:
            return self.session.query(Usuario).all()
        except Exception as erro:
            print(f"Erro ao listar usuários: {erro}")
            raise erro

    def pesquisar_usuario_por_email(self, email: str):
        try:
            return self.session.query(Usuario).filter_by(email=email).first()
        except Exception as erro:
            print(f"Erro ao pesquisar usuário: {erro}")
            raise erro

    def excluir_usuario(self, usuario: Usuario):
        try:
            self.session.delete(usuario)
            self.session.commit()
        except Exception as erro:
            self.session.rollback()
            print(f"Erro ao excluir usuário: {erro}")
            raise erro

    def atualizar_usuario(self, usuario, novos_dados):
        if not isinstance(novos_dados, dict):
            raise TypeError("novos_dados deve ser um dicionário")
        if not hasattr(usuario, '__dict__'):
            raise TypeError("usuario deve ser um objeto com atributos modificáveis")
    
        try:
            for key, value in novos_dados.items():
                setattr(usuario, key, value)
            return usuario  
        except AttributeError as erro:
            raise AttributeError(f"Erro ao atualizar o atributo '{key}' do usuário: {erro}")