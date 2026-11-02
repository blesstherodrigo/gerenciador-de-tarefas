tarefas = []

while True:
    print(
        '\n'
        'MENU DE TAREFAS\n'
        '[1]Adicionar\n'
        '[2]Listar\n'
        '[3]Sair'
    )

    try:
        opcao = int(input('> '))    # converte(casting) de str para int
    except ValueError:
        print('Formato inválido!')
        continue    # pula as condicionais(if-else) e volta ao começo do laço(menu)

    if opcao == 1:
        nova_tarefa = input('Nova tarefa: ').strip()    # strip remove os espaços da frente e atrás
        if nova_tarefa == "":
            print("Esta tarefa está vazia!")
        else:
            tarefas.append(nova_tarefa)     # adiciona uma nova tarefa na lista

    elif opcao == 2:
        if len(tarefas) == 0:
            print('Não há tarefas...')
        else:
            for indice, item_tarefa in enumerate(tarefas, start=1):
                print(indice, item_tarefa)      # lista as tarefas registradas começando pelo 1

    elif opcao == 3:
        break   # sai do menu

    else:
        print(opcao, 'é inválido!')