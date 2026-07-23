# Movie Tracker

Um projeto desenvolvido em Python com o objetivo de registrar filmes assistidos, marcar favoritos e persistir os dados em um arquivo JSON.

O principal objetivo deste projeto é desenvolver habilidades em engenharia de software, organização de código, refatoração e arquitetura de aplicações, evoluindo gradualmente até uma aplicação backend utilizando Django.

---

## Funcionalidades

* Adicionar filmes.
* Listar todos os filmes cadastrados.
* Marcar filmes como favoritos.
* Listar apenas os filmes favoritos.
* Remover filmes dos favoritos.
* Persistir os dados automaticamente em um arquivo JSON.

---

## Tecnologias utilizadas

* Python 3
* JSON
* Módulo `json`
* Módulo `os`
* Git
* GitHub

---

## Estrutura do projeto

```text
Movie_Tracker/
│
├── main.py
├── movies_list.json
├── README.md
├── .gitignore
│
├── Movies/
│   └── movies.py
│
├── Storage/
│   └── storage.py
│
└── UI/
    └── ui.py
```

### Responsabilidade de cada módulo

#### `main.py`

Ponto de entrada da aplicação. Inicializa o sistema, carrega os dados e controla o fluxo principal do programa.

#### `Movies/movies.py`

Contém as regras de negócio relacionadas aos filmes, como:

* adicionar filmes;
* alterar o status de favorito;
* filtrar listas;
* selecionar filmes.

#### `UI/ui.py`

Responsável pela interação com o usuário, incluindo:

* exibição do menu;
* exibição de listas;
* limpeza da tela;
* mensagens;
* espera por confirmação do usuário.

#### `Storage/storage.py`

Responsável pela persistência dos dados:

* carregar filmes do arquivo JSON;
* salvar alterações no arquivo.

---

## Como executar

Clone o repositório:

```bash
git clone <url-do-repositório>
```

Entre na pasta do projeto:

```bash
cd Movie_Tracker
```

Execute:

```bash
python main.py
```

Na primeira execução, o arquivo `movies_list.json` será criado automaticamente quando os primeiros dados forem salvos.

---

## Objetivos de aprendizado

Este projeto está sendo desenvolvido com foco em aprender conceitos de desenvolvimento de software, incluindo:

* decomposição de problemas;
* separação de responsabilidades;
* organização de projetos;
* persistência de dados;
* refatoração;
* arquitetura de software;
* controle de versão com Git;
* evolução gradual para aplicações web com Django.

---

## Roadmap

### ✅ Versão 2

* Cadastro de filmes
* Sistema de favoritos
* Persistência em JSON
* Organização inicial em módulos

### 🔄 Próximos passos

* Remover filmes cadastrados
* Evitar cadastros duplicados
* Adicionar notas e avaliações
* Adicionar datas em que os filmes foram adicionados
* Evoluir para uma aplicação utilizando Django
