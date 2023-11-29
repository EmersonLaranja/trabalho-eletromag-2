import numpy as np
import matplotlib.pyplot as plt

# Função para calcular a média das diferenças entre duas iterações
def calcular_erro(v, v_novo):
    return np.mean(np.abs(v - v_novo))

# Função para realizar as iterações do método de diferenças finitas até que o erro seja abaixo do limite
def simulacao_diferencas_finitas(nx, ny, ni_max, limite_erro, placas):
    # Inicialização dos valores iniciais como zero
    v = np.zeros((nx, ny))

    # Adição de placas ao potencial inicial
    for placa in placas:
        v[placa['inicio'][0]:placa['fim'][0]+1, placa['inicio'][1]:placa['fim'][1]+1] = placa['potencial']

    # Inicializa listas para armazenar resultados ao longo das iterações
    erros = []

    # Realiza iterações do método de diferenças finitas até que o erro seja abaixo do limite
    ni = 0
    erro = float('inf')
    while ni < ni_max and erro > limite_erro:
        v_novo = np.copy(v)
        for i in range(1, nx-1):
            for j in range(1, ny-1):
                v_novo[i, j] = 0.25 * (v[i+1, j] + v[i-1, j] + v[i, j+1] + v[i, j-1])

        # Atualização considerando as placas
        for placa in placas:
            v_novo[placa['inicio'][0]:placa['fim'][0]+1, placa['inicio'][1]:placa['fim'][1]+1] = placa['potencial']

        ni += 1
        erro = calcular_erro(v, v_novo)
        v = np.copy(v_novo)

        # Armazena o erro para análise posterior
        erros.append(erro)

    return v, ni, erros

# Parâmetros para a simulação
nx = 70
ny = 70
ni_max = 10000
limite_erro = 0.01

# Definição das placas
placas = [
    {'inicio': (10, 10), 'fim': (20, 20), 'potencial': 50},  # Exemplo de uma placa com potencial 50V
    {'inicio': (40, 30), 'fim': (50, 40), 'potencial': 50},  # Exemplo de outra placa com potencial 50V
]

# Realiza a simulação de diferenças finitas
resultado, iteracoes, erros = simulacao_diferencas_finitas(nx, ny, ni_max, limite_erro, placas)

# Imprime os resultados
print("Número de Iterações:", iteracoes)
print("Erro Final:", erros[-1])

# Plotagem do mapa escalar de tensão
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
hContour = plt.contourf(resultado, cmap='viridis')
hColorbar = plt.colorbar()
plt.ylabel('Potencial Eletrico (V)')
plt.title('Mapa Escalar de Tensão com Placas')

# Plotagem do gráfico de erro em função do número de iterações
plt.subplot(1, 2, 2)
plt.plot(range(1, iteracoes + 1), erros, marker='o', linestyle='-', color='b')
plt.xlabel('Número de Iterações')
plt.ylabel('Erro Médio')
plt.title('Variação do Erro ao Longo das Iterações')

plt.tight_layout()
plt.show()
