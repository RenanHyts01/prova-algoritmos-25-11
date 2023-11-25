# Olá Professor Fabio, escolhemos o termo Munícipes como se fosse uma Agenda de Endereços de um município ok? Onde já cadastro na prefeitura.

agenda_de_dados = []


# Professor fábio, abaixo vou declarar as funções solicitadas pelo programa para o menu principal, que será feito logo abaixo das mesmas!

# Professor fábio, esta função abaixo server para coletar os dados do novo Munícipe que será registrado da Agenda de Endereços!
# Esta função foi feita por Renan Augusto - 202311388


def inserir_municipe():
    nome = input("Informe o nome do Munícipe: ")
    endereço = input("Informe o Endereço do munícipe: ")
    telefone_de_contato = input("Insira o Número de Telefone do Munícipe: ")
    agenda_de_dados.append(
        {"Nome": nome, "Endereço": endereço, "Telefone de Contato": telefone_de_contato}
    )
    print("O munícipe foi Inserido na Agenda de Endereços")
    print("Retornando ao Menu Principal")


# Professor Fábio, segue abaixo a função que foi feita para consultar os Munícipes inseridos na lista que guarda os dados da agenda de endereços!
# Esta Função foi feita por Renan AUgusto - 202311388


def consultar_municipe():
    nome = input(" Digite o nome completo do munícipe para consulta de endereço: ")
    for cadastrado in agenda_de_dados:
        if cadastrado["Nome"] == nome:
            print(
                " O Munícipe se encontra cadastrado na Agenda de Endereços, seguem seus dados abaixo "
            )
            print("Nome: ", cadastrado["Nome"])
            print("Endereço", cadastrado["Endereço"])
            print("Telefone de Contato", cadastrado["Telefone de Contato"])

            print("Retornando ao Menu Principal")
            return

    print("Não foram encontrados Registros")


# Professor, seguind adiante temos a função de Remover munícipes já inseridos na lista que armazena este dado para a agenda de endereços!
# Esta função foi feita por Maria Eduarda - xxxxxxxxxx


def excluir_municipe():
    nome = input("Digite o nome do municipe a ser excluído da agenda de endereços: ")
    for cadastrado in agenda_de_dados:
        if cadastrado["Nome"] == nome:
            agenda_de_dados.remove(cadastrado)
            print(" Municipe removido da Agenda de Endereços")
            return

    print("Não foram encontrados Registros")


def listar_municipes():
    for cadastrado in agenda_de_dados:
        print("Munícipe Cadastrado Encontrado")
        print("Nome: ", cadastrado["Nome"])
        print("Endereço: ", cadastrado["Endereço"])
        print("Telefone de Contato: ", cadastrado["Telefone de Contato"])
        print("-----------")


def zerar_agenda():
    agenda_de_dados.clear()
    print("Agenda zerada!")


def mostrar_desenvolvedores():
    print("Desenvolvedores:")
    print("Matrícula: 202311388 - Nome: Renan Augusto Santos Silva")
    print("Matrícula: 67890 - Nome: Gabriel Fernandes Duarte")
    print("Matrícula: xxxxxxx - Nome: Maria Eduarda Franklin")


# Segue abaixo o Menu principal da Agenda de Endereços Municipal

while True:
    print("#------------------------------------------------------------------------#")
    print("#        A G E N D A  D E  E N D E R E Ç O S  M U N I C I P A L          #")
    print("#------------------------------------------------------------------------#")
    print("#                 Escolha uma dentre as opções abaixo                    #")
    print("#------------------------------------------------------------------------#")

    print("# 1 – CADASTRAR NOME #")
    print("# 2 – CONSULTAR NOME #")
    print("# 3 – EXCLUIR NOME #")
    print("# 4 – LISTAR TODOS OS NOMES #")
    print("# 5 – ZERAR AGENDA #")
    print("# 6 - DESENVOLVEDORES #")
    print("# 7 – SAIR #")
    print("#------------------------------------------------------------------------#")

    # Abaixo a Variável para digitarmos o valor correspondente a opção desejada.

    opcao = input("Digite o Número da opção que deseja realizar: ")

    # Abaixo as condicionantes para que sejam acessadas as opções desejadas.

    if opcao == "1":
        inserir_municipe()

    elif opcao == "2":
        consultar_municipe()

    elif opcao == "3":
        excluir_municipe()

    elif opcao == "4":
        listar_municipes()

    elif opcao == "5":
        zerar_agenda()

    elif opcao == "6":
        mostrar_desenvolvedores()

    elif opcao == "7":
        print(" Você saiu do programa Agenda de Endereços, até mais")
        break

    else:
        print(
            " Opção Inválida, Digite caracteres correspondetes a opção que deseja realizar, de 1 á 7 "
        )
