import numpy as np
from sympy import Eq, Matrix, Symbol
from sympy.abc import x, y, a, b

eq = Eq('')

Ab = np.array([[-2, 0, 1, -4], [-1, 7, 1, -50], [5, -1, 1, -26]])

print("Matriz aumentada (A|b)")
print(Ab)

# PROCEDIMIENTO

# Evitar truncamiento en operaciones
Ab = np.array(Ab, dtype=float)
# Pivoteo parcial por filas
size = np.shape(Ab)
row_numb = size[0]
col_numb = size[1]

# Para cada fila en A
for i in range(0, row_numb - 1):
    # columna desde diagonal i en adelante
    columna = abs(Ab[i:, i])
    ind_max = np.argmax(columna)

    # dondemax no está en diagonal
    if ind_max != 0:
        # intercambia filas
        temporal = np.copy(Ab[i, :])
        Ab[i, :] = Ab[ind_max + i, :]
        Ab[ind_max + i, :] = temporal

Ab1 = np.copy(Ab)

# eliminacion hacia adelante
for i in range(0, row_numb - 1, 1):
    pivot = Ab[i, i]
    ind_next = i + 1
    for k in range(ind_next, row_numb, 1):
        factor = Ab[k, i] / pivot
        Ab[k, :] = Ab[k, :] - Ab[i, :] * factor
Ab2 = np.copy(Ab)

# elimina hacia atras
last_row = row_numb - 1
last_col = col_numb - 1
for i in range(last_row, 0 - 1, -1):
    pivot = Ab[i, i]
    ind_prev = i - 1
    for k in range(ind_prev, 0 - 1, -1):
        factor = Ab[k, i] / pivot
        Ab[k, :] = Ab[k, :] - Ab[i, :] * factor
    # diagonal a unos
    Ab[i, :] = Ab[i, :] / Ab[i, i]
X = np.copy(Ab[:, last_col])
X = np.transpose([X])

# SALIDA
print("Pivoteo parcial por filas")
print(Ab1)
print("eliminacion hacia adelante")
print(Ab2)
print("eliminación hacia atrás")
print(Ab)
print("solución de X: ")
print(X)