import numpy as np
import matplotlib.pyplot as plt

# Função para calcular a média das diferenças entre duas iterações
def calcular_erro(v, v_novo):
    return np.mean(np.abs(v - v_novo))

# Função para realizar as iterações do método de diferenças finitas até que o erro seja abaixo do limite
def simulacao_diferencas_finitas(nx, ny, v1, v2, v3, v4, ni_max, limite_erro):
    # INICIALIZAÇÃO DOS VALORES INICIAIS COMO ZERO
    v = np.zeros((nx, ny))
    
    # Define potenciais fixos nas bordas
    for i in range(1, nx-1):
        v[i, 0] = v1 # Barra a esquerda
        v[i, ny-1] = v3 # Barra a direita

    for j in range(1, ny-1):
        v[0, j] = v4 # Barra superior
        v[nx-1, j] = v2 # Barra inferior

# Define potenciais fixos nos cantos
    v[0, 0] = 0.5 * (v1 + v2) # Canto superior esquerdo
    v[nx-1, 0] = 0.5 * (v1 + v4) # Canto inferior esquerdo
    v[0, ny-1] = 0.5 * (v3 + v2) # Canto superior direito
    v[nx-1, ny-1] = 0.5 * (v3 + v4) # Canto inferior direito

    # Inicializa variáveis
    ni = 0
    erro = float('inf')

    # Inicializa listas para armazenar resultados ao longo das iterações
    erros = []

    # Realiza iterações do método de diferenças finitas até que o erro seja abaixo do limite
    while ni < ni_max and erro > limite_erro:
        v_novo = np.copy(v)
        for i in range(1, nx-1):
            for j in range(1, ny-1):
                v_novo[i, j] = 0.25 * (v[i+1, j] + v[i-1, j] + v[i, j+1] + v[i, j-1])
        ni += 1
        erro = calcular_erro(v, v_novo)
        v = np.copy(v_novo)
# Armazena o erro para análise posterior
        erros.append(erro)
    return v, ni, erros

# Parâmetros para a simulação
nx = 70
ny = 70
v1 = 50  # Tensão na barra a esquerda
v2 = 0  # Tensão na barra superior
v3 = 50  # Tensão na barra a direita
v4 = 0  # Tensão na barra inferior
ni_max = 10000  # Número máximo de iterações
limite_erro = 0.01  # Limite de erro

# Realiza a simulação de diferenças finitas
resultado, iteracoes, erros = simulacao_diferencas_finitas(nx, ny, v1, v2, v3, v4, ni_max, limite_erro)

# Imprime os resultados
print("Número de Iterações:", iteracoes)
print("Erro Final:", erros[-1])

# Plotagem do mapa escalar de tensão
plt.figure(1)
hContour = plt.contourf(resultado, cmap='viridis')
hColorbar = plt.colorbar()
plt.ylabel('Potencial Eletrico (V)')
plt.title('Simulação por Diferenças Finitas')
plt.show()
# Plotagem do gráfico de erro em função do número de iterações
plt.subplot(1, 2, 2)
plt.plot(range(1, iteracoes + 1), erros, linestyle='-', color='b')
plt.xlabel('Número de Iterações')
plt.ylabel('Erro Médio')
plt.title('Variação do Erro ao Longo das Iterações')

plt.tight_layout()
plt.show()