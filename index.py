# Projeto Gerenciador de Tarefas
# Desenvolvido por Nathali Cardoso | GitHub: github.com/Nathali-Cardoso

import sys

#lista global onde as tarefas serão armazenadas
tarefas = []


#função para exibir um título centralizado com bordas
def nome_comando(txt):
    largura = 50
    print('=' * largura)
    print(txt.upper().center(largura))
    print('=' * largura)

#função que exibe o menu principal e direciona para as opções
def menu():
    nome_comando('menu')
    print('1 - Adicionar Tarefa\n'
          '2 - Remover \n'
          '3 - Mostrar Tarefas \n'
          '4 - Apagar Tudo \n'
          '0 - Sair \n')

    while True:
        try:
            num=int(input('Selecione uma das opções acima: ').strip())
            if num == 1:
                adicionar()

            elif num == 2:
                remover()

            elif num == 3:
                mostrar_tarefas()

            elif num == 4:
                excluir()

            elif num == 0:
                encerrar()

            else:
                print('Opção inválida!')
                continue

        except ValueError:
            print('Digite apenas números.')
            continue

#função para adicionar tarefas à lista
def adicionar():
    nome_comando('adicionar tarefa')

    while True:
        try:
            n=int(input('Quantas tarefas deseja adicionar? ').strip())
            if n > 0:
                for t in range (1,1+n):
                    tarefa=input(f'{t} - Tarefa: ').strip().lower()
                    tarefas.append(tarefa)

                print('Tarefas adicionadas!')
                print('-'*50)
                voltar_menu()

            else:
                print('Valor inválido.')
                continue

        except ValueError:
            print('Digite apenas números.')
            continue

#função para remover uma tarefa da lista
def remover():
    nome_comando('remover tarefa')

    if not tarefas:
        print('Nada a ser removido \nSua lista de tarefas está vazia!')
        print('-'*50)
        voltar_menu()

    else:
        print('Verifique a lista para remover a opção correta: ')

        for i, n in enumerate(tarefas, start=1):
            print(f'{i}º- {n}')
        print('-'*50)
        while True:
            try:
                num = int(input('Digite o número da tarefa que deseja remover: ').strip())
                if 1 <= num <= len(tarefas):
                    rem_tarefa = tarefas.pop(num-1)
                    print(f'Tarefa: {rem_tarefa}, removida com sucesso!')
                    print('-'*50)
                    voltar_menu()

                else:
                    print('Opção inválida! Digite apenas uma das opções disponíveis.')
                    continue

            except ValueError:
                print('Digite apenas números.')

#função para exibir todas as tarefas da lista
def mostrar_tarefas():
    nome_comando('lista de tarefas')
    if not tarefas:
        print('Hmm... Parece que sua lista de tarefas está vazia.')
        while True:
            try:
                lista_vazia = int(input('O que quer fazer? \n'
                            '1 - Adicionar tarefas \n'
                            '2 - Voltar ao Menu Principal \n'
                            '3 - Sair \n'
                            'Opção: ').strip())

                if lista_vazia == 1:
                    adicionar()
                    break

                elif lista_vazia == 2:
                    menu()
                    break

                elif lista_vazia == 3:
                    encerrar()
                    break

                else:
                    print('Por favor digite apenas uma das opções disponíveis.')

            except ValueError:
                print('Opção inválida... Digite apenas números.')
    else:
        for i,t in enumerate(tarefas,start=1):
            print(f'{i}º- {t}')
        print('-'*50)
        voltar_menu()

#função para excluir todas as tarefas da lista
def excluir():
    nome_comando('excluir todas tarefas')
    if not tarefas:
        print('Nada a ser excluído\nSua lista de tarefas está vazia\n')
        print('-'*50)
        voltar_menu()

    else:
        while True:
            try:
                confirme=input('Tem certeza que deseja apagar todos os itens \nda lista? [S/N]: ').strip().lower()
                if confirme == 's':
                    tarefas.clear()
                    print('-'*50)
                    print('Todas as tarefas foram removidas com sucesso!')
                    print('-'*50)
                    voltar_menu()

                elif confirme == 'n':
                    print('Procedimento cancelado.')
                    print('-'*50)
                    voltar_menu()

                else:
                    print('Por favor, responda apenas com S/N')
                    continue

            except ValueError:
                print('Resposta inválida.')
                continue

#função para encerrar o programa
def encerrar():
    print('-'*50)
    print('Programa encerrado... Até breve!')
    print('-'*50)
    sys.exit()

#função que pergunta ao usuário se deseja retornar ao menu ou sair do programa
def voltar_menu():
    while True:
        try:
            confirme = int(input('Você deseja: \n'
                             '1 - Retornar ao Menu Principal\n'
                             '2 - Sair \n'
                             'Selecione uma opção: ').strip())

            if confirme == 1:
                menu()

            elif confirme == 2:
                encerrar()

            else:
                print('Opção inválida!')
                continue

        except ValueError:
            print('Digite apenas números.')
            continue

#função inicial que pergunta o nome do usuário e inicia o programa
def iniciar_programa():
    while True:
        try:
            nome=input('Insira seu nome para iniciarmos: ').lower().strip().split()
            nome = [p.capitalize() for p in nome]
            novo_nome = ' '.join(nome)

            print(f'Olá, {novo_nome}\nSeja bem-vinda(o) !!!\n')
            menu()

        except ValueError:
            print('Erro: dados inválidos.')
            continue

#ponto de entrada do programa
if __name__ == "__main__":
    iniciar_programa()







