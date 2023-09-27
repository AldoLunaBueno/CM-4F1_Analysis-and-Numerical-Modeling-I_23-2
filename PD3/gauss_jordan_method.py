import numpy as np

Ab = np.array([[-2, 0, 1, -4], [-1, 7, 1, -50], [5, -1, 1, -26]])

print("Matriz aumentada (A|b)")
print(Ab)
print("\n")

# PROCEDIMIENTO

# Evitar truncamiento en operaciones
Ab = np.array(Ab, dtype=float)
print("Pivoteo parcial por filas")
size = np.shape(Ab)
row_numb = size[0]
col_numb = size[1]

for i in range(0, row_numb - 1):
    print(f"\nColumna desde fila {i} en adelante")
    columna = abs(Ab[i:, i])
    ind_max = np.argmax(columna)

    if ind_max != 0:
        print(f"\nEl máximo no está en la diagonal. Intercambia filas {i} y {i+ind_max}")
        temporal = np.copy(Ab[i, :])
        Ab[i, :] = Ab[ind_max + i, :]
        Ab[ind_max + i, :] = temporal
        print(Ab)
print("\n")

print("Eliminación hacia adelante")
for i in range(0, row_numb - 1, 1):
    pivot = Ab[i, i]
    ind_next = i + 1
    for k in range(ind_next, row_numb, 1):
        factor = Ab[k, i] / pivot
        Ab[k, :] = Ab[k, :] - Ab[i, :] * factor
        print(Ab)
        print("\n")

print("Eliminación hacia atrás")
last_row = row_numb - 1
last_col = col_numb - 1
for i in range(last_row, 0 - 1, -1):
    print("\n")
    pivot = Ab[i, i]
    ind_prev = i - 1
    for k in range(ind_prev, 0 - 1, -1):
        factor = Ab[k, i] / pivot
        Ab[k, :] = Ab[k, :] - Ab[i, :] * factor
    # diagonal a unos
    Ab[i, :] = Ab[i, :] / Ab[i, i]
    print(Ab)
X = np.copy(Ab[:, last_col])
X = np.transpose([X])

print("\nSolución: ")
print(X)