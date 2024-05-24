# crie um programa em que o usuário crie uma lista de tarefas a ser executada no dia

# Inicializa a lista de tarefas
tarefas = []

while True:
    # Usuário adiciona uma tarefa
    nova_tarefa = input('Adicione uma tarefa ou deixe vazo para encerrar e exibir a lista): ')
    
    # Verifica se o usuário quer sair
    if nova_tarefa != '':
        tarefas.append(nova_tarefa)
        continue
    else:
        break

# Exibe na tela a lista de tarefas atualizada
for tarefa in tarefas:
    print(tarefa)
