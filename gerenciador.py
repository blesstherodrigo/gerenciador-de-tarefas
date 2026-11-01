''''
Criar a lista que armazenará as tarefas.
Criar o menu com as três opções.
Fazer o menu continuar aparecendo até o usuário escolher sair.
Implementar a opção de adicionar tarefas.
Implementar a opção de listar, incluindo a verificação da lista vazia.
'''

tarefas = []

while True:
    print(
        '\n'
        'MENU DE TAREFAS\n'
        '[1]Adicionar\n'
        '[2]Listar\n'
        '[3]Sair'
    )

    opcao = int(input('> '))

    if opcao == 1:
        nova_tarefa = input('Nova tarefa: ')
        tarefas.append(nova_tarefa)     # adiciona uma nova tarefa

    elif opcao == 2:
        if len(tarefas) == 0:
            print('Nenhuma tarefa registrada...')
        else:
            for indice, item_tarefa in enumerate(tarefas, start=1):
                print(indice, item_tarefa)      # lista as tarefas registradas

    elif opcao == 3:
        break       # sai do menu

    else:
        print('Opção inválida!')