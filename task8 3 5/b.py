def product_generator(n):
    P = 1.0
    yield P  # P_0 = 1
    for k in range(1, n + 1):
        P *= 1 + 1 / (k ** 2)
        yield P


def compute_product(n):
    if n < 0:
        raise ValueError("n має бути невід'ємним")
    P = 1.0
    for k in range(1, n + 1):
        P *= 1 + 1 / (k ** 2)
    return P


def compute_product_epsilon(epsilon=1e-6):
    P = 1.0
    k = 1
    while True:
        term = 1 + 1 / (k ** 2)
        P *= term
        next_k = k + 1
        if next_k ** (-2) < epsilon:
            break
        k += 1
    return P, k


def save_results(n, filename="result_b.txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("Цикл з лічильником (від 1 до 5):\n")
        P = 1.0
        for k in range(1, n + 1):
            P *= 1 + 1 / (k ** 2)
            f.write(f"P_{k} = {P}\n")

        f.write("\nГенератор-функція:\n")
        gen = product_generator(n)
        for k in range(n + 1):
            f.write(f"P_{k} = {next(gen)}\n")

        P_final, iterations = compute_product_epsilon()
        f.write("\nЦикл з умовою (до 1/k² < 1e-6):\n")
        f.write(f"Остаточний P = {P_final}\n")
        f.write(f"Кількість ітерацій: {iterations}")


if __name__ == "__main__":
    n = 5
    save_results(n)