agenda = []

#Função de criar novo contato
def criar_novo_contato(agenda):
    nome = input("Digite o nome: ")
    telefone = input("Digite o n° de telefone: ")
    email = input("Digite o E-mail: ")
    print("Deseja marcar como favorito?")
    print("1. Sim")
    print("2. Não")
    print("")
    favorito_sim_nao = input("Escolha a opção desejada: ")
    print("")
    favorito = favorito_sim_nao == "1"
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": favorito
    }
    agenda.append(contato)
    print("")
    print("Contato adicionado com sucesso.")
    return

#Função de visualizar os contatos existentes
def ver_contatos(agenda):
    for indice, contato in enumerate(agenda, start=1):
        contato_favorito = "★" if contato["favorito"] else ""
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        print("")
        print(f"{indice}. {nome}{contato_favorito}")
        print(f"E-mail: {email} | Telefone: {telefone}")
        print("")

    return

#Função de editar contato
def editar_contato(agenda, contato_escolhido):
    for indice, contato in enumerate(agenda, start=1):
        if indice == int(contato_escolhido):
            print("1. Nome do contato.")
            print("2. N° de telefone.")
            print("3. E-mail.")
            print("")
            opcao_editar_contato = input("Digite a opção que você deseja editar: ")

            if int(opcao_editar_contato) == 1:
                novo_nome = input("Digite o novo nome do contato: ")
                antigo_nome = contato["nome"]
                contato["nome"] = novo_nome
                print(f"{antigo_nome} editado para: {novo_nome}")
            elif int(opcao_editar_contato) == 2:
                novo_telefone = input("Digite o novo telefone do contato: ")
                antigo_telefone = contato["telefone"]
                contato["telefone"] = novo_telefone
                print(f"{antigo_telefone} editado para: {novo_telefone}")
            elif int(opcao_editar_contato) == 3:
                novo_email = input("Digite o novo email do contato: ")
                antigo_email = contato["email"]
                contato["email"] = novo_email
                print(f"{antigo_email} editado para: {novo_email}")
    return

#Menu de funcionalidades da agenda
while True:
    print("")
    print("1. Criar novo contato.")
    print("2. Visualizar contatos existentes.")
    print("3. Editar contato.")
    print("5. Apagar contato.")
    print("6. Favoritar contato.")
    print("7. Contatos favoritados.")
    print("8. Finalizar programa.")
    print("")

    opcao_escolhida = input("Digite a opção desejada: ")
    print("")

    if opcao_escolhida == "8":
        break
    elif opcao_escolhida == "1":
        criar_novo_contato(agenda)
    elif opcao_escolhida == "2":
        if len(agenda) != 0:
            ver_contatos(agenda)
        else:
            print("")
            print("Não há contatos existentes.")
            print("")
    elif opcao_escolhida == "3":
        if len(agenda) != 0:
            ver_contatos(agenda)
            print("")
            contato_escolhido = input("Digite qual contato você deseja editar: ")
            print("")
            editar_contato(agenda, contato_escolhido)
        else:
            print("")
            print("Não há contatos existentes.")
            print("")

print("Programa finalizado com sucesso.")