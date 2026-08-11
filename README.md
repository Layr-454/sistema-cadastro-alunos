
# Sistema de Cadastro de Alunos

Sistema simples em Python, feito via terminal, para cadastrar alunos, registrar notas e calcular a situação (Aprovado/Reprovado) com base na média.

Projeto desenvolvido por mim, Layr, estudante do 2º semestre de Ciência da Computação, como forma de praticar lógica de programação, estruturas de dados e boas práticas de código.

## Funcionalidades

- Cadastrar aluno (nome, idade) com geração automática de ID único
- Listar todos os alunos cadastrados
- Buscar aluno por ID
- Excluir aluno por ID
- Adicionar notas e calcular média/situação automaticamente

## Como rodar

Pré-requisito: ter o Python 3 instalado.

```bash
python sistema_cadastro_alunos.py
```

Depois é só seguir o menu interativo no terminal.

## Tecnologias

- Python

## O que aprendi com esse projeto

- Diferença entre variável local e global (`global`)
- Como validar entrada de dados do usuário com `try/except`
- Bugs sutis de fluxo de controle (código posicionado depois de um `break`, ou indentado dentro do loop errado) e como identificá-los revisando linha por linha
- Importância de usar identificadores únicos (ID) em vez de campos como nome, que podem se repetir
- Convenções de nomenclatura em Python (snake_case, sem acentos em variáveis)

## Próximos passos (ideias para evoluir o projeto)

- Persistir os dados em arquivo (JSON ou CSV) para não perder o cadastro ao fechar o programa
- Migrar o armazenamento para um banco de dados usando SQL
- Adicionar testes automatizados

