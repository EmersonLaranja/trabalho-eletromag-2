# Trabalho de Simulação Eletrostática ⚡️

## Descrição 📚

Este repositório contém o código fonte e os resultados de um trabalho de simulação eletrostática usando o método de diferenças finitas para resolver a equação de Laplace. O objetivo do trabalho é simular o mapa escalar de tensão em uma cuba eletrolítica com diferentes configurações.

O trabalho se divide em 2 etapas (parte1 e parte2) descritas abaixo.

## Parte 1 🧮

Na **Parte 1**, a simulação é realizada considerando quatro paredes com fontes de tensão nas bordas verticais da cuba eletrolítica. O código é implementado em Python, utilizando o método de diferenças finitas para resolver a equação de Laplace. O mapa escalar de tensão e a variação do erro ao longo das iterações são analisados.

## Parte 2 ⚙️

Na **Parte 2**, o problema é refeito, agora considerando a presença de duas ou mais placas dentro da cuba eletrolítica, em vez de nas bordas. O código é adaptado para a nova configuração, e os resultados, incluindo o mapa escalar de tensão e a variação do erro ao longo das iterações, são apresentados.

## Principais Funcionalidades 🛠️

### 1. Função de Diferenças Finitas

A implementação do método de diferenças finitas é encapsulada na função `simulacao_diferencas_finitas`. Esta função realiza as iterações necessárias para resolver a equação de Laplace e calcular o mapa escalar de tensão.

```python
def simulacao_diferencas_finitas(nx, ny, ni_max, limite_erro, placas):
    # ... (código da função)
    return v, ni, erros
```

### 2. Cálculo de Erro

A função `calcular_erro` é responsável por calcular o erro médio entre duas iterações consecutivas. O critério de parada para as iterações é baseado neste erro, garantindo a convergência da solução.

```python
def calcular_erro(v, v_novo):
    return np.mean(np.abs(v - v_novo))
```

### 3. Configuração das Placas (Parte 2)

Na **Parte 2**, o código permite a adição de placas dentro da cuba. Modifique as coordenadas e potenciais das placas no código conforme necessário.

```python
placas = [
    {'inicio': (10, 10), 'fim': (20, 20), 'potencial': 10},
    {'inicio': (40, 30), 'fim': (50, 40), 'potencial': -5},
    # Adicione mais placas conforme necessário
]
```

## Estrutura do Repositório 📂

- **`codigo_parte1.py`**: Código-fonte da Parte 1 da simulação.
- **`codigo_parte2.py`**: Código-fonte da Parte 2 da simulação.
- **`trabalho.pdf`**: Arquivo com a descrição fornecida pelo professor quanto ao que deveria ser feito.
- **`relatório.pdf`**: Arquivo com os resultados da execução de ambas as partes do código, atendendo o trabalho.
- **`README.md`**: Este arquivo, fornecendo uma visão geral do trabalho.

## Como Executar 🚀

1. Clone este repositório.
2. Execute `codigo_parte1.py` ou `codigo_parte2.py` para realizar a simulação.

## Dependências 🛠️

- Python 3.x
- Biblioteca Matplotlib para visualização de gráficos (instale com `pip install matplotlib`).

## Resultados 📊

Os resultados da simulação, incluindo mapas escalares de tensão e gráficos de erro, são armazenados no arquivo `relatório.pdf`.

## Autores 🧑‍💻

| [<img src="https://github.com/EmersonLaranja.png" width="100"><br><sub>Emerson Laranja</sub>](https://github.com/EmersonLaranja) | [<img src="https://github.com/BrunoAngeloti.png" width="100"><br><sub>Bruno Angeloti</sub>](https://github.com/BrunoAngeloti) |
| :------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------: |

## **Divirta-se simulando e explorando a eletrostática!** ⚡️🔍
