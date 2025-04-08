from datetime import datetime
import json, os

ARQUIVO = "tarefas.json"

def mostrar_tarefa_formatada(i, tarefa):
    print(f"{i}. [{tarefa['status']}] {tarefa['titulo']} (Criado em: {tarefa['criado_em']})")

def ver_tarefas(tarefas):
    if tarefas:
        print("\nSuas tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            mostrar_tarefa_formatada(i, tarefa)
    else:
        print("Nenhuma tarefa cadastrada")

def add_tarefas(tarefas):
    titulo = input("Digite uma nova tarefa: ")
    novo_id = tarefas[-1]["id"] + 1 if tarefas else 1
    nova_tarefa = {
        "id": novo_id,
        "titulo": titulo,
        "status": "❌",
        "criado_em": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tarefas.append(nova_tarefa)
    print("Tarefa adicionada com o ID:", novo_id)

def remov_tarefa(tarefas):
    if tarefas:
        ver_tarefas(tarefas)
        try:
            ind = int(input("Digite o número da tarefa a ser removida: "))
            if 1 <= ind <= len(tarefas):
                removida = tarefas.pop(ind - 1)
                print(f"Tarefa '{removida['titulo']}' foi removida.")
            else:
                print("Número inválido")
        except ValueError:
            print("Entrada inválida. Digite um número.")
    else:
        print("Nenhuma tarefa para remover")

def marcar_prnt(tarefas):
    if tarefas:
        ver_tarefas(tarefas)
        try:
            ind = int(input("Digite o número da tarefa a ser marcada como concluída: "))
            if 1 <= ind <= len(tarefas):
                tarefa = tarefas[ind - 1]
                tarefa["status"] = "✅"
                print(f"Tarefa '{tarefa['titulo']}' marcada como concluída.")
            else:
                print("Número inválido")
        except ValueError:
            print("Entrada inválida. Digite um número.")
    else:
        print("Nenhuma tarefa para marcar como concluída")

def marcar_prog(tarefas):
    if tarefas:
        ver_tarefas(tarefas)
        try:
            ind = int(input("Digite o número da tarefa a ser marcada como em progresso: "))
            if 1 <= ind <= len(tarefas):
                tarefa = tarefas[ind - 1]
                tarefa["status"] = "⏳"
                print(f"Tarefa '{tarefa['titulo']}' marcada como em progresso.")
            else:
                print("Número inválido")
        except ValueError:
            print("Entrada inválida. Digite um número.")
    else:
        print("Nenhuma tarefa para marcar como em progresso")

def desmarcar(tarefas):
    if tarefas:
        ver_tarefas(tarefas)
        try:
            ind = int(input("Digite o número da tarefa a ser desmarcada: "))
            if 1 <= ind <= len(tarefas):
                tarefa = tarefas[ind - 1]
                tarefa["status"] = "❌"
                print(f"Tarefa '{tarefa['titulo']}' desmarcada como concluída.")
            else:
                print("Número inválido")
        except ValueError:
            print("Entrada inválida. Digite um número.")
    else:
        print("Nenhuma tarefa para desmarcar")

def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=4)

def menu():
    tarefas = carregar_tarefas()

    opcoes = {
        1: ("Ver Tarefas", lambda: ver_tarefas(tarefas)),
        2: ("Adicionar Tarefa", lambda: add_tarefas(tarefas)),
        3: ("Remover Tarefa", lambda: remov_tarefa(tarefas)),
        4: ("Marcar Tarefa como Concluída", lambda: marcar_prnt(tarefas)),
        5: ("Marcar Tarefa em Progresso", lambda: marcar_prog(tarefas)),
        6: ("Desmarcar Tarefa", lambda: desmarcar(tarefas)),
        7: ("Sair", None),
    }

    while True:
        print("\nMenu:")
        for i in range(1, 8):
            print(f"{i} - {opcoes[i][0]}")
        try:
            op = int(input("Escolha uma opção: "))
            if op == 7:
                print("Saindo...")
                salvar_tarefas(tarefas)
                break

            func = opcoes.get(op)
            if func:
                func[1]()
            else:
                print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

menu()
