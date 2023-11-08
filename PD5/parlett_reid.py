#!/usr/bin/env python
import numpy as np


def limpiadorm(ma, n):
    for i in range(0, n):
        for j in range(0, n):
            if abs(ma[i][j]) < 0.00000001:
                ma[i][j] = 0


def limpiadorv(vec, n):
    for i in range(0, n):
        if abs(vec[i]) < 0.00000001:
            vec[i] = 0


def mayor(lista):
    sig = np.sign(lista[0])
    max = abs(lista[0])
    for x in lista:
        if abs(x) > max:
            max = x
    return max


def crear_elemtal(n, k):
    e_k = np.array([0] * n)
    e_k[k - 1] = 1
    return e_k


def crear_P_k(n, k1, k2):
    P = np.array([crear_elemtal(n, i) for i in range(1, n + 1)])
    P[k1] = crear_elemtal(n, k2 + 1)
    P[k2] = crear_elemtal(n, k1 + 1)
    return P


def parlet_raid(A):
    n = len(A)
    P = np.identity(n)
    L_1 = np.identity(n)
    L = np.identity(n)
    for i in range(0, n - 2):
        print("\nPaso ", i+1)
        b = np.zeros(n)
        for j in range(i, n - 1):
            b[1 + j] = A[j + 1][i]

        max = mayor(b)
        posimax = np.where(b == max)
        band = b[i + 1]
        b[i + 1] = max
        b[posimax] = band
        b[i + 1] = 0
        P_k = crear_P_k(n, i + 1, posimax[0][0])
        P = np.dot(P_k, P)
        limpiadorm(P, n)
        b = b / max
        limpiadorv(b, n)
        print("- vector b : \n", b)  ##############
        print("- matriz P : \n", P_k)  ###################
        e_k = crear_elemtal(n, i + 2)
        M_k = np.identity(n) - np.outer(b, e_k)
        limpiadorm(M_k, n)
        print("- matriz M : \n", M_k)  ##################
        L_1 = M_k @ P_k @ L_1
        limpiadorm(L, n)
        A = M_k @ P_k @ A @ P_k.T @ M_k.T
        limpiadorm(A, n)
        print("- matriz A : \n", np.around(A, 6))  #############
    L = np.linalg.inv(np.dot(L_1, P.T))
    print("Matriz P: \n", P)
    print("Matriz L: \n", L)
    print("Matriz T: \n", A)
    return (P, L, A)


A = np.array(
    [
        [1, 2, 4],
        [2, 3, 4],
        [4, 4, 1],
    ],
    dtype=np.float64,
)
b = np.array([35, 42, 34])

P, L, T = parlet_raid(A)

print("\nResolución del sistema Ax = b paso a paso:")

print("A = P^-1 L T Lt P")

print("1. Lz = Pb")
z = np.linalg.solve(L, P@b)
print(f"  z = {z}")

print("2. Tw = z")
w = np.linalg.solve(T, z)
print(f"  w = {w}")

print("3. Lt y = w")
y = np.linalg.solve(L.T, w)
print(f"  y = {y}")

print("4. x = Pt y")
x_sol_step_by_step = P.T@y
print(f"  x = {x_sol_step_by_step}")

x_sol = np.linalg.solve(A, b)
print("Solución hallada con np.linalg.solve:")
print(x_sol)


# 1. Lz = Pb
# 2. Tw = z
# 3. Lt y = w
# 4. x = Pt y

