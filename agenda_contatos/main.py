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
    print(agenda)
    return

#Função de visualizar os contatos existentes
def ver_contatos(agenda):
    for indice, contato in enumerate(agenda, start=1):
        contato_favorito = "★" if contato["favorito"] else ""
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        print(f"{indice}. {nome}{contato_favorito}")
        print(f"E-mail: {email} | Telefone: {telefone}")
        print("")

    return

#Menu de funcionalidades da agenda
while True:
    print("1. Criar novo contato.")
    print("2. Visualizar contatos existentes.")
    print("3. Editar contato.")
    print("5. Apagar contato.")
    print("6. Favoritar contato.")
    print("7. Contatos favoritados.")
    print("8. Finalizar programa.")

    opcao_escolhida = input("Digite a opção desejada: ")

    if opcao_escolhida == "8":
        break
    elif opcao_escolhida == "1":
        criar_novo_contato(agenda)
    elif opcao_escolhida == "2":
        ver_contatos(agenda)

print("Programa finalizado com sucesso.")