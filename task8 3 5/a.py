def sequence_generator(x):
    xk = 1.0
    yield xk
    k = 1
    while True:
        xk *= (x ** 2) / ((2 * k) * (2 * k - 1))
        yield xk
        k += 1


def compute_with_counter(x, max_k):
    results = [1.0]  # k=0
    if max_k == 0:
        return results
    xk = 1.0
    for k in range(1, max_k + 1):
        xk *= (x ** 2) / ((2 * k) * (2 * k - 1))
        results.append(xk)
    return results


def compute_with_condition(x, epsilon=1e-6):
    results = []
    gen = sequence_generator(x)
    while True:
        current = next(gen)
        results.append(current)
        if abs(current) < epsilon:
            break
    return results


def save_to_file(x, max_k, filename="result_a.txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("Цикл з лічильником (від 0 до 10):\n")
        results_counter = compute_with_counter(x, max_k)
        for k, val in enumerate(results_counter):
            f.write(f"Xk_{k} = {val}\n")

        f.write("\nЦикл з умовою (до |a_k| < 1e-6):\n")
        results_condition = compute_with_condition(x)
        for k, val in enumerate(results_condition):
            f.write(f"Xk_{k} = {val}\n")


if __name__ == "__main__":
    x = 2.0
    max_k = 10
    save_to_file(x, max_k)