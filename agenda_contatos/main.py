agenda = []

#Função de criar novo contato
def criar_novo_contato(agenda):
    nome = input("Digite o nome: ")
    telefone = input("Digite o n° de telefone: ")
    email = input("Digite o E-mail: ")
    print("Deseja marcar como favorito?")
    print("1. Sim")
    print("2. Não")
    favorito_sim_nao = input("Escolha a opção desejada: ")
    favorito = favorito_sim_nao == "1"
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": favorito
    }
    agenda.append(contato)
    print("Contato adicionado com sucesso.")

    return

#Menu de funcionalidades da agenda
while True:
    print("1. Criar novo contato.")
    print("2. Visualizar contatos existentes.")
    print("3. Editar contato.")
    print("4. Apagar contato.")
    print("5. Contatos favoritados.")
    print("6. Finalizar programa.")

    opcao_escolhida = input("Digite a opção desejada: ")

    if opcao_escolhida == "6":
        break
    elif opcao_escolhida == "1":
        criar_novo_contato(agenda)

print("Programa finalizado com sucesso.")