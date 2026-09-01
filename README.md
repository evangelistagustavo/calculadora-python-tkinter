# calculadora-python-tkinter
Calculadora em Python com Tkinter

Projeto de uma calculadora simples desenvolvido durante os estudos de Python. Ele possui uma versão para terminal e uma interface gráfica criada com Tkinter.

## Funcionalidades

- Soma
- Subtração
- Multiplicação
- Divisão
- Tratamento de divisão por zero
- Validação de números na versão executada pelo terminal
- Reaproveitamento da lógica de cálculo na interface gráfica

## Tecnologias

- Python
- Tkinter

## Estrutura do projeto

```text
calculadora-python-tkinter/
├── calculadora_v1.py
├── interface_calculadora.py
└── README.md
```

- calculadora_v1.py: contém a lógica das operações e pode ser executado no terminal.
- interface_calculadora.py: cria a interface gráfica e utiliza a função de cálculo do arquivo principal.

## Como executar

É necessário ter o Python 3 instalado.

Para executar a versão no terminal:

python calculadora_v1.py

Para executar a interface gráfica:

python interface_calculadora.py

## Aprendizados

Neste projeto, pratiquei:

- Criação de funções em Python
- Condicionais para selecionar operações
- Tratamento de erros com try/except
- Importação e reaproveitamento de funções entre arquivos
- Criação de interfaces gráficas com Tkinter

## Próximos passos

- Melhorar o visual da interface
- Validar entradas não numéricas na interface gráfica
- Adicionar histórico de cálculos
- Criar uma versão com teclado numérico semelhante ao de uma calculadora convencional
