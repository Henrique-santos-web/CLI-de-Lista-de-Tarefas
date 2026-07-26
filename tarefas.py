import json, os, sys

comando = sys.argv[1]

def carregar_tarefas():
    if not os.path.exists("tarefas.json"):
        return []

    with open("tarefas.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_tarefas(tarefas):
    with open("tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)


def adicionar_tarefa(titulo):
    tarefas = carregar_tarefas()

    nova_tarefa = {
        "id" : len(tarefas) + 1,
        "titulo" : titulo,
        "concluida" : False
    }

    tarefas.append(nova_tarefa)

    salvar_tarefas(tarefas)


def listar_tarefas():
    tarefas = carregar_tarefas()

    if not tarefas:
        print("Você ainda não definiu nenhuma tarefa")
        return

    for tarefa in tarefas:

        if tarefa["concluida"]:
            status = "✅ concluída"
        else:
            status = "⏳ pendente"  

        print(f'[{tarefa["id"]}] {tarefa["titulo"]} — {status}')


def concluir_tarefa(id):
    tarefas = carregar_tarefas()
    encontrada = False

    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa["concluida"] = True
            encontrada = True

    if encontrada:
        salvar_tarefas(tarefas)
        print("Parabéns por concluir essa tarefa!")
    else:
        print("Tarefa não localizada")


def deletar_tarefa(id):
    tarefas = carregar_tarefas()

    tarefas = [t for t in tarefas if t["id"] != id] 
    #[O QUE FAZER   for ITEM in LISTA   if CONDIÇÃO]
    #mantem t para cada t in tarefas se t(id) for direfente, ou seja
    #ele atualiza a lista mantendo apenas os id q forem diferentes do id que recebeu como parametro
    #se o id for igual ao id que recebeu como parametro, ele será deletado da lista 
    salvar_tarefas(tarefas)
    print("Tarefa deletada com sucesso!")


if len(sys.argv) < 2:
    print("Uso: python tarefas.py [add|list|done|delete]")
    #* Se o usuário apenas digitar o comando para rodar o arquivo, o código printa uma mensagem mostrando os comando que pode usar
else:
    comando = sys.argv[1]

    if comando == "add":
        adicionar_tarefa(sys.argv[2])
    elif comando == "list":
        listar_tarefas()
    elif comando == "done":
        concluir_tarefa(int(sys.argv[2]))
    elif comando == "delete":
        deletar_tarefa(int(sys.argv[2]))
    else:
        print("Comando não reconhecido")