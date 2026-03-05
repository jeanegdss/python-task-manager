arquivo = "tarefas.txt"

def carregar_tarefas():
    try:
        with open(arquivo, "r") as f:
            return f.read().splitlines()
    except:
        return []

def salvar_tarefas(tarefas):
    with open(arquivo, "w") as f:
        for t in tarefas:
            f.write(t + "\n")

tarefas = carregar_tarefas()

while True:
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        salvar_tarefas(tarefas)
        print("Tarefa adicionada!")

    elif opcao == "2":
        for i, t in enumerate(tarefas):
            print(i+1, "-", t)

    elif opcao == "3":
        numero = int(input("Número da tarefa: "))
        tarefas.pop(numero-1)
        salvar_tarefas(tarefas)
        print("Tarefa removida!")

    elif opcao == "4":
        break
