def adicionar_tarefa(lista):
    nova_tarefa = input('Nova tarefa: ').strip()  # strip remove os espaços da frente e atrás

    if nova_tarefa == "":
        print("Esta tarefa está vazia!")
    else:
        lista.append(nova_tarefa)  # adiciona uma nova tarefa na lista

def listar_tarefas(lista):
    if len(lista) == 0:
        print('Não há tarefas...')
    else:
        for indice, item_tarefa in enumerate(lista, start=1):
            print(indice, '-', item_tarefa)     # lista as tarefas registradas começando pelo 1

def remover_tarefa(lista):
    listar_tarefas(lista)

    if len(lista) == 0:     # confirma se lista está vazia e encerra a função
        return

    try:
        numero_tarefa = int(input('Número da tarefa: '))  # try-except para tratar entradas inválidas para o casting
    except ValueError:
        print('Formato inválido!')
        return

    indice_tarefa = numero_tarefa - 1  # subtrai 1 para adaptar ao índice da tarefa escolhida

    if numero_tarefa > len(lista) or indice_tarefa < 0:  # se o número é maior que a lista ou o índice menor que 0, é inválido
        print('Opção [', numero_tarefa, '] é inválida')
    else:
        tarefa_removida = lista.pop(indice_tarefa)  # remove a tarefa da lista
        print('Tarefa [', tarefa_removida, '] foi removida!')

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
            opcao = int(input('> '))    # converte(casting) de str para int
        except ValueError:
            print('Formato inválido!')
            continue    # pula as condicionais(if-else) e volta ao começo do laço(menu)

        if opcao == 1:
            adicionar_tarefa(tarefas)
        elif opcao == 2:
            remover_tarefa(tarefas)
        elif opcao == 3:
            listar_tarefas(tarefas)
        elif opcao == 4:
            break   # sai do menu
        else:
            print(opcao, 'é inválido!')

if __name__ == '__main__':
    main()