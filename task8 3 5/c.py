def det_generator(a, b):
    d_prev, d_curr = 1.0, a + b
    yield d_prev
    yield d_curr
    while True:
        d_next = (a + b) * d_curr - a * b * d_prev
        yield d_next
        d_prev, d_curr = d_curr, d_next


def det_by_counter(n, a, b):
    if n < 0:
        raise ValueError("n має бути невід'ємним")
    if n == 0:
        return 1.0
    if n == 1:
        return a + b
    d_prev, d_curr = 1.0, a + b
    for _ in range(2, n + 1):
        d_next = (a + b) * d_curr - a * b * d_prev
        d_prev, d_curr = d_curr, d_next
    return d_curr


def det_by_epsilon(a, b, eps=1e-6, max_iter=1000):
    gen = det_generator(a, b)
    prev = next(gen)  # D_0
    curr = next(gen)  # D_1
    for n in range(2, max_iter + 1):
        next_val = next(gen)
        if abs(next_val - curr) < eps:
            return next_val, n
        prev, curr = curr, next_val
    return curr, max_iter


def save_det_results(a, b, max_n, filename="result_c.txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("Цикл з лічильником (від 0 до 10):\n")
        for n in range(max_n + 1):
            det = det_by_counter(n, a, b)
            f.write(f"D_{n} = {det}\n")

        f.write("\nГенератор-функція:\n")
        gen = det_generator(a, b)
        for n in range(max_n + 1):
            f.write(f"D_{n} = {next(gen)}\n")

        final_val, iterations = det_by_epsilon(a, b)
        f.write("\nЦикл з умовою (ε=1e-6):\n")
        f.write(f"Остаточне значення: {final_val}\n")
        f.write(f"Кількість ітерацій: {iterations}")


if __name__ == "__main__":
    a, b = 2, 3
    max_n = 10
    save_det_results(a, b, max_n)