import numpy as np
import matplotlib.pyplot as plt

# USING FINITE DIFFERENCE (ITERATION) METHOD
# THIS PROGRAM SOLVES THE TWO-DIMENSIONAL BOUNDARY-VALUE
# PROBLEM (LAPLACE’S EQUATION) SHOWN IN FIG. 14.14.

# Constants
pv = 0 * 1e-12  # Densidade volumétrica de cargas livres
eo = 1e-9 / (36 * np.pi)  # Permissividade elétrica do vácuo
er = 80  # Permissividade elétrica relativa do meio
eps = er * eo

# Corner of the TROUGH
v1 = 0  # Valor da tensão na barra a esquerda
v2 = 10  # Valor da tensão na barra superior
v3 = 0  # Valor da tensão na barra a direita
v4 = -10  # Valor da tensão na barra inferior

ni = 900
nx = 90
ny = 90

# SET INITIAL VALUES EQUAL TO ZEROES
v = np.zeros((nx, ny))

# FIX POTENTIALS ARE FIXED NODES
for i in range(1, nx-1):
    v[i, 0] = v1
    v[i, ny-1] = v3

for j in range(1, ny-1):
    v[0, j] = v4
    v[nx-1, j] = v2

v[0, 0] = 0.5 * (v1 + v4)
v[nx-1, 0] = 0.5 * (v1 + v2)
v[0, ny-1] = 0.5 * (v3 + v4)
v[nx-1, ny-1] = 0.5 * (v2 + v3)

# NOW FIND v(i,j) USING EQ. (14.15) AFTER ni ITERATIONS
for k in range(ni):
    for i in range(1, nx-1):
        for j in range(1, ny-1):
            v[i, j] = 0.25 * (v[i+1, j] + v[i-1, j] + v[i, j+1] + v[i, j-1] + pv/eps)

# Output specific values
print([v[5, 5], v[8, 8], v[10, 5], v[8, 2]])

# Plotting
plt.figure(1)
hContour = plt.contourf(v)
hColorbar = plt.colorbar()
plt.ylabel('Potencial Eletrico (V)')
plt.show()
