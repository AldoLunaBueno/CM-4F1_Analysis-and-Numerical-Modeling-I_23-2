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
    return 2 * (beta - 1) * beta**(t-1) * (U - L + 1)

beta = 2
t = 3
L = -2
U = 2
print("Conjunhto de números máquina:")
print(f"F({beta}, {t}, {L}, {U})")
print()

print("Total de números máquina: ")
print(total_machine_numbers(beta, t, L, U))
print()

print("Todos los números máquina: ")
print_all_machine_numbers(beta, t, L, U)
print()
