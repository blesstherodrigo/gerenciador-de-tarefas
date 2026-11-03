def adicionar_tarefa(lista):
    nova_tarefa = input('Nova tarefa: ').strip()  # strip remove os espaços desnecessários da string

    if not nova_tarefa:
        print("Esta tarefa está vazia!")
    else:
        lista.append(nova_tarefa)


def listar_tarefas(lista):
    if not lista:
        print('Não há tarefas...')
    else:
        for indice, item_tarefa in enumerate(lista, start=1):
            print(f'{indice} - {item_tarefa}')


def remover_tarefa(lista):
    listar_tarefas(lista)

    if not lista:   # verifica se a lista está vazia([]) e encerra a função
        return

    try:
        numero_tarefa = int(input('Número da tarefa: '))
    except ValueError:
        print('Formato inválido!')
        return

    if not (1 <= numero_tarefa <= len(lista)):
        print(f'Número de tarefa "{numero_tarefa}" inválido!')
    else:
        indice_tarefa = numero_tarefa - 1
        tarefa_removida = lista.pop(indice_tarefa)
        print(f'Tarefa "{tarefa_removida}" foi removida!')


def main():
    tarefas = []

    while True:
        print(
            '\n'
            'MENU DE TAREFAS\n'
            '[1]Adicionar\n'
            '[2]Remover\n'
            '[3]Listar\n'
            '[4]Sair'
        )

        try:
            opcao = int(input('> '))
        except ValueError:
            print('Formato inválido!')
            continue

        if opcao == 1:
            adicionar_tarefa(tarefas)
        elif opcao == 2:
            remover_tarefa(tarefas)
        elif opcao == 3:
            listar_tarefas(tarefas)
        elif opcao == 4:
            break
        else:
            print(f'"{opcao}" é inválido!')


if __name__ == '__main__':
    main()