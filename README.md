# Todo_List

Gerenciador de Tarefas em Python (CLI)

Este é um gerenciador de tarefas simples, executado no terminal, feito com Python. Ele permite que você adicione, visualize, edite e remova tarefas, com salvamento automático em um arquivo .json.

Como usar:

# 1. Execute o script

Abra o terminal e rode:

python tarefas.py

# 2. Menu de Opções

Ao iniciar o programa, será exibido um menu:

  * 1 - Ver Tarefas
  * 2 - Adicionar Tarefa
  * 3 - Remover Tarefa 
  * 4 - Marcar Tarefa como Concluída 
  * 5 - Marcar Tarefa em Progresso 
  * 6 - Desmarcar Tarefa 
  * 7 - Sair

Escolha uma opção digitando o número correspondente.

# 3. Status das Tarefas

✅ Tarefa concluída

⏳ Tarefa em progresso

❌ Tarefa pendente

# 4. Salvamento automático

As tarefas são salvas automaticamente no arquivo tarefas.json.

Ao reiniciar o programa, as tarefas serão carregadas deste arquivo.

Sobre o arquivo tarefas.json

Este arquivo contém os dados salvos de cada tarefa no formato JSON:

{
  "id": 1,
  "titulo": "Estudar Python",
  "status": "✅",
  "criado_em": "2025-04-08 14:03:49"
}

Cada tarefa é um dicionário com:

id: identificador único

titulo: descrição da tarefa

status: estado atual (❌, ⏳ ou ✅)

criado_em: data e hora da criação

#Requisitos

Python 3.x

Bibliotecas usadas: datetime, json, os (todas da biblioteca padrão)

# URL DO PROJETO:
https://roadmap.sh/projects/task-tracker
