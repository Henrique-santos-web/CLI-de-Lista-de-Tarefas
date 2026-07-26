# 📋 CLI de Lista de Tarefas

> Gerenciador de tarefas pela linha de comando feito em Python — meu primeiro desafio após concluir o curso de backend.

---

## 🚀 Sobre o projeto

Uma aplicação de linha de comando (CLI) simples e eficiente para gerenciar suas tarefas do dia a dia direto pelo terminal. As tarefas são salvas em um arquivo `.json`, garantindo persistência entre as execuções.

---

## 🛠️ Tecnologias utilizadas

- **Python 3.14**
- **json** — persistência de dados
- **os** — verificação de arquivos
- **sys** — leitura de argumentos do terminal

---

## ⚙️ Como instalar

**1. Clone o repositório**

**2. Crie e ative o ambiente virtual**

**3. Pronto! Nenhuma dependência externa necessária.**

---

## 💻 Como usar

| Comando | Descrição |
|--------|-----------|
| `python tarefas.py add "Título"` | Adiciona uma nova tarefa |
| `python tarefas.py list` | Lista todas as tarefas |
| `python tarefas.py done <id>` | Marca uma tarefa como concluída |
| `python tarefas.py delete <id>` | Remove uma tarefa da lista |

---

## 📁 Estrutura do projeto

cli-tarefas/
├── tarefas.py      # lógica principal e ponto de entrada
├── tarefas.json    # banco de dados local (gerado automaticamente)
└── README.md

---

## 👨‍💻 Autor

Feito com 💚 por **Henrique Miranda**

[![GitHub](https://img.shields.io/badge/GitHub-Henrique--santos--web-181717?style=flat&logo=github)](https://github.com/Henrique-santos-web)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Henrique%20Miranda-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/henrique-miranda-5503b0294)