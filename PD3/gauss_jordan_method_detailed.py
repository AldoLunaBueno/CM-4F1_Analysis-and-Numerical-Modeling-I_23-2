import numpy as np

Ab = np.array([[120, 200, 80, 100, 2020], [1, 1, 1, 1, 14], [1, -1, 0, 1, 0], [0, 1, -3, 0, 0]])

print("Matriz aumentada (A|b)")
print(Ab)
print("\n")

# Operaciones elementales

def swap(A, row1, row2):
    A = A.copy()
    temp = A.copy()[row1, :]
    A[row1, :] = A[row2, :]
    A[row2, :] = temp
    return A
def rowScale(A, row, k):
    A = A.copy()
    A[row, :] = k * A[row, :]
    return A
def addRowScaled(A, row, k, endRow):
    A = A.copy()
    temp = k * A[row, :]
    A[endRow, :] = A[endRow, :] + temp
    return A

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
        I = np.identity(row_numb)
        E = swap(I, i, ind_max +i)
        
        print("Multiplicando la matriz de operación elemental...")
        print(E)
        print("por...")
        print(Ab)
        print("igual:")
        Ab = swap(Ab, i, ind_max +i)
        print(Ab)
print("\n")

print("Eliminación hacia adelante")
for i in range(0, row_numb - 1, 1):
    pivot = Ab[i, i]
    ind_next = i + 1
    for k in range(ind_next, row_numb, 1):
        factor = Ab[k, i] / pivot
        I = np.identity(row_numb)
        E = addRowScaled(Ab, i, -factor, k)
        print("Multiplicando la matriz de operación elemental...")
        print(E)
        print("por...")
        print(Ab)
        print("igual:")
        Ab = addRowScaled(Ab, i, -factor, k)
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
        I = np.identity(row_numb)
        E = addRowScaled(I, i, -factor, k)
        print("Multiplicando la matriz de operación elemental...")
        print(E)
        print("por...")
        print(Ab)
        print("igual:")
        Ab = addRowScaled(Ab, i, -factor, k)
    # diagonal a unos
    I = np.identity(row_numb)
    E = rowScale(I, i, 1/Ab[i, i])
    print("Multiplicando la matriz de operación elemental...")
    print(E)
    print("por...")
    print(Ab)
    print("igual:")
    Ab = rowScale(Ab, i, 1/Ab[i, i])
    print(Ab)
X = np.copy(Ab[:, last_col])
X = np.transpose([X])

print("\nSolución: ")
print(X)

