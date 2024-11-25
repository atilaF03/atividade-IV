import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

from project.config.database import get_db
from project.repositories.usuario_repository import UsuarioRepository
from project.services.usuario_service import UsuarioService

def exibir_menu():
    print("=== SENAI SOLUTION ===")
    print("1 - Adicionar usuário")
    print("2 - Pesquisar um usuário")
    print("3 - Atualizar dados de um usuário")
    print("4 - Excluir um usuário")
    print("5 - Exibir todos os usuários cadastrados")
    print("0 - Sair")
    print("=======================")

def main():
    # Conexão com o banco e instância de serviço
    with get_db() as db_session:
        repository = UsuarioRepository(session=db_session)
        service = UsuarioService(repository=repository)

        while True:
            exibir_menu()
            opcao = input("Informe a opção desejada: ").strip()

            if opcao == "1":  # Adicionar usuário
                nome = input("Informe o nome do usuário: ").strip()
                email = input("Informe o email do usuário: ").strip()
                senha = input("Informe a senha do usuário: ").strip()
                service.criar_usuario(nome, email, senha)

            elif opcao == "2":  # Pesquisar um usuário
                email = input("Informe o email do usuário que deseja buscar: ").strip()
                usuario = repository.pesquisar_usuario_por_email(email)
                if usuario:
                    print(f"Usuário encontrado: ID={usuario.id}, Nome={usuario.nome}, Email={usuario.email}")
                else:
                    print("Usuário não encontrado.")

            elif opcao == "3":  # Atualizar dados de um usuário
                email = input("Informe o email do usuário a ser atualizado: ").strip()
                usuario = repository.pesquisar_usuario_por_email(email)
                if usuario:
                    print(f"Dados atuais: Nome={usuario.nome}, Email={usuario.email}")
                    novo_nome = input("Informe o novo nome (ou pressione Enter para manter o atual): ").strip() or usuario.nome
                    novos_dados = {"nome": novo_nome}  # Transforme em um dicionário
                    repository.atualizar_usuario(usuario, novos_dados)  # Apenas esta chamada
                    print("Usuário atualizado com sucesso!")
                else:
                    print("Usuário não encontrado.")

            elif opcao == "4":  # Excluir um usuário
                email = input("Informe o email do usuário que deseja excluir: ").strip()
                usuario = repository.pesquisar_usuario_por_email(email)
                if usuario:
                    repository.excluir_usuario(usuario)
                    print("Usuário excluído com sucesso!")
                else:
                    print("Usuário não encontrado.")

            elif opcao == "5":  # Exibir todos os usuários cadastrados
                usuarios = service.listar_todos_usuarios()
                if usuarios:
                    print("Usuários cadastrados:")
                    for usuario in usuarios:
                        print(f"ID={usuario.id}, Nome={usuario.nome}, Email={usuario.email}")
                else:
                    print("Nenhum usuário cadastrado.")

            elif opcao == "0":  # Sair
                print("Encerrando o programa. Até mais!")
                break

            else:
                print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()