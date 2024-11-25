from project.models.usuario_model import Usuario
from project.repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
            if not nome or not email or not senha:
                print("Todos os campos (nome, email e senha) são obrigatórios!")
                return

            usuario = Usuario(nome=nome, email=email, senha=senha)

            cadastrado = self.repository.pesquisar_usuario_por_email(email=usuario.email)

            if cadastrado:
                print("Usuário já cadastrado!")
                return
            
            self.repository.salvar_usuario(usuario=usuario)
            print("Usuário cadastrado com sucesso!")

        except TypeError as erro:
            print(f"Erro ao salvar o usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def listar_todos_usuarios(self):

        try:
            usuarios = self.repository.listar_usuarios()

            if not usuarios:
                print("Nenhum usuário cadastrado.")
                return []

            return usuarios

        except Exception as erro:
            print(f"Erro ao listar usuários: {erro}")
            return []
        