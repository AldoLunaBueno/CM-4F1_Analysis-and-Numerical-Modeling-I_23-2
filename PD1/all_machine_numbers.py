def print_all_machine_numbers(beta, t, L, U):
    """
    t: dígitos significativos
    L: mínimo exponente
    U: máximo exponente
    """

    beta = 2 # No está implementado en otras bases

    for i in range(L, U+1):
        for j in range(2**(t-1)):
            repr_str = "0.1"
            repr_str += f"{j:0{t-1}b}"
            repr_str += " x 2^" + str(i)
            print(repr_str)

def total_machine_numbers(beta, t, L, U):
    return 2 * (beta - 1) * beta**(t-1) * (U - L + 1) + 1

def machine_number_bounds(beta, t, L, U):
    x_min = beta**(L-1)
    x_max = beta**(U) * (1-beta**(-t))
    return f"[{-x_max}, {-x_min}] U {{0}} U [{x_min}, {x_max}]"

beta = 2
t = 3
L = -2
U = 2

print("Conjunto de números máquina:")
print(f"F({beta}, {t}, {L}, {U})")
print()

print("Total de números máquina: ")
print(total_machine_numbers(beta, t, L, U))
print()

print("Expresión del conjunto de números máquina: ")
print(machine_number_bounds(beta, t, L, U))
print()

print("Todos los números máquina positivos: ")
print_all_machine_numbers(beta, t, L, U)
print()
