def print_all_machine_numbers_base2(t, L, U):
    """
    t: dígitos significativos
    L: mínimo exponente
    U: máximo exponente
    """

    for i in range(L, U+1):
        for j in range(2**(t-1)):
            repr_str = "0.1"
            repr_str += f"{j:0{t-1}b}"
            repr_str += " x 2^" + str(i)
            print(repr_str)

def total_machine_numbers(beta, t, L, U):
    return 2 * (beta - 1) * beta**(t-1) * (U - L + 1)

print_all_machine_numbers_base2(3, -2, 2)
# print(total_machine_numbers(2, 3, -2, 2))
