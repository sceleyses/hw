def a_k_generator():
    """Генерує послідовність a_k за правилом:
    a_1 = 1, a_2 = 1, a_3 = 1,
    a_k = a_{k-1} + a_{k-3} для k >= 4."""
    a = [1, 1, 1]  # Відповідає a_1, a_2, a_3
    for num in a:
        yield num
    while True:
        next_val = a[-1] + a[-3]  # Обчислення a_k
        a.append(next_val)
        yield next_val


def compute_Sn_counter(n):
    """Обчислює суму S_n = sum_{k=1}^n (a_k / 2^k)."""
    if n < 1:
        return 0.0
    gen = a_k_generator()
    S = 0.0
    for k in range(1, n + 1):
        a_k = next(gen)
        S += a_k / (2 ** k)
    return S


def compute_Sn_epsilon(epsilon=1e-6, max_iter=1000):
    """Обчислює суму S до збіжності (|S_n - S_{n-1}| < epsilon)."""
    gen = a_k_generator()
    S = 0.0
    prev_S = 0.0
    for k in range(1, max_iter + 1):
        a_k = next(gen)
        term = a_k / (2 ** k)
        S += term
        if k > 1 and abs(S - prev_S) < epsilon:  # Перевірка з k=2
            return S, k
        prev_S = S
    return S, max_iter


def save_results(n_values, filename="result_d.txt"):
    """Зберігає результати у файл."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("Цикл з лічильником (від 1 до 10):\n")
        for n in n_values:
            Sn = compute_Sn_counter(n)
            f.write(f"S_{n} = {Sn}\n")

        f.write("\nГенератор послідовності a_k:\n")
        gen = a_k_generator()
        for k in range(1, max(n_values) + 1):
            f.write(f"a_{k} = {next(gen)}\n")

        final_sum, iterations = compute_Sn_epsilon()
        f.write("\nЦикл з умовою (ε=1e-6):\n")
        f.write(f"Остаточна сума: {final_sum}\n")
        f.write(f"Кількість ітерацій: {iterations}")


if __name__ == "__main__":
    n_values = range(1, 11)
    save_results(n_values)