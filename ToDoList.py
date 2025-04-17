from datetime import datetime, timedelta
import pyautogui
import json, os, tkinter as tk

NOME_ARQUIVO = "tarefas_nogui.json"
LOCAL_ARQUIVO = r"C:\Users\BushG\OneDrive\Área de Trabalho\Programas\python\Python\Pessoal\ListaTarefaJSON\Save"

ARQUIVO = os.path.join(LOCAL_ARQUIVO, NOME_ARQUIVO)

def mostrar_tarefa_formatada(i, tarefa):
    prazo = tarefa.get("prazo_limite", "Sem prazo")
    print(f"{i}. [{tarefa['status']}] {tarefa['titulo']} {tarefa['id']} | \n (Criado em: {tarefa['criado_em']} | prazo: {prazo})\n ")

def ver_tarefas(tarefas):

    tarefas_vencidas = []
    tarefas_nvencidas = []    
    
    for tarefa in tarefas: 
        prazo = tarefa.get("prazo_limite")
        if prazo and prazo != "Sem prazo":
            try:
                prazo_dt = datetime.strptime(prazo, "%Y-%m-%d %H:%M:%S")
                if prazo_dt < datetime.now() and tarefa["status"] != "✅":
                    tarefas_vencidas.append(tarefa)
                else:
                    tarefas_nvencidas.append(tarefa)
            except ValueError:
                print(f"⚠️ Prazo inválido na tarefa '{tarefa['titulo']}', ignorando para ordenação.")
                tarefas_nvencidas.append(tarefa)
                continue
        else:   
            tarefas_nvencidas.append(tarefa)
            
    if tarefas_nvencidas:
        for i, tarefa in enumerate(tarefas_nvencidas, start=1):
            mostrar_tarefa_formatada(i, tarefa)
    else:
        print("Nenhuma tarefa não vencida")
        
    if tarefas_vencidas:
        mensagem_alerta = "Tarefas vencidas:\n\n"
        for i, tarefa in enumerate(tarefas_vencidas, start=1):
            mensagem_alerta += f"{i}. {tarefa['titulo']} (Venceu em: {tarefa['prazo_limite']})\n"
        pyautogui.alert(text=mensagem_alerta, title="⚠️ Tarefas Vencidas", button="OK")
    else:
        print("Nenhuma tarefa vencida")

def add_tarefas(tarefas):
    titulo = input("Digite uma nova tarefa: ")
    prazo_input = input(("Digite o prazo da tarefa (formato: YYYY-MM-DD HH:MM) ou deixe em branco para sem prazo: "))
    
    prazo = "Sem prazo"
    if prazo_input.strip():
        try:
            prazo_dt = datetime.strptime(prazo_input.strip(), "%Y-%m-%d %H:%M")
            prazo = prazo_dt.strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("⚠️ Prazo inválido! Use o formato: YYYY-MM-DD HH:MM")
    
    novo_id = tarefas[-1]["id"] + 1 if tarefas else 1
    nova_tarefa = {
        "id": novo_id,
        "titulo": titulo,
        "status": "❌",
        "criado_em": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "prazo_limite": prazo
    }
    tarefas.append(nova_tarefa)
    print("Tarefa adicionada com o ID:", novo_id)

def remov_tarefa(tarefas):
    if tarefas:
        ver_tarefas(tarefas)
        try:
            ID_remov = int(input("Digite o ID da tarefa a ser removida: "))
            tarefa = next((t for t in tarefas if t["id"] == ID_remov), None)
            if tarefa:
                tarefas.remove(tarefa)
                print(f"Tarefa '{tarefa['titulo']}' foi removida.")
            else:
                print("ID não encontrado")
        except ValueError:
            print("Entrada inválida. Digite um número.")
    else:
        print("Nenhuma tarefa para remover")

def marcar_prnt(tarefas):
    if tarefas:
        ver_tarefas(tarefas)
        try:
            id_conclui = int(input("Digite o ID da tarefa a ser marcada como concluída: "))
            tarefa = next((t for t in tarefas if t["id"] == id_conclui), None)
            if tarefa:
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
            id_prog = int(input("Digite o ID da tarefa a ser marcada como em progresso: "))
            tarefa = next((t for t in tarefas if t["id"] == id_prog), None)
            if tarefa:
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
            id_desmarca = int(input("Digite o ID da tarefa a ser desmarcada: "))
            tarefa = next((t for t in tarefas if t["id"] == id_desmarca), None)
            if tarefa:
                tarefa["status"] = "❌"
                print(f"Tarefa '{tarefa['titulo']}' marcada como não concluída.")
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
        
def tempo_limite(tarefas):
    print("\nTarefas com prazo vencido:")
    agora = datetime.now()
    vencidas = []

    for tarefa in tarefas:
        prazo = tarefa.get("prazo_limite")
        if prazo:
            prazo_dt = datetime.strptime(prazo, "%Y-%m-%d %H:%M:%S")
            if prazo_dt < agora and tarefa["status"] != "✅":
                vencidas.append(tarefa)
    if vencidas:
        for i, tarefa in enumerate(vencidas, start=1):
            mostrar_tarefa_formatada(i, tarefa)
    else:
        print("Nenhuma tarefa com prazo vencido.")


def menu():
    tarefas = carregar_tarefas()

    opcoes = {
        1: ("Ver Tarefas", lambda: ver_tarefas(tarefas)),
        2: ("Adicionar Tarefa", lambda: add_tarefas(tarefas)),
        3: ("Remover Tarefa", lambda: remov_tarefa(tarefas)),
        4: ("Marcar Tarefa como Concluída", lambda: marcar_prnt(tarefas)),
        5: ("Marcar Tarefa em Progresso", lambda: marcar_prog(tarefas)),
        6: ("Desmarcar Tarefa", lambda: desmarcar(tarefas)),
        7: ("Ver Tarefas Com Prazo Vencido", lambda: tempo_limite(tarefas)),
        8: ("Sair", None)
    }

    while True:
        print("\nMenu:")
        for i in range(1, 9):
            print(f"{i} - {opcoes[i][0]}")
        try:
            op = int(input("Escolha uma opção: "))
            if op == 8:
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


