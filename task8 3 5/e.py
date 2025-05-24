import math

def taylor_terms(x):
    term = x
    yield 2 * term
    k = 1
    while True:
        term *= (x ** 2) * (2 * k - 1) / (2 * k + 1)
        yield 2 * term
        k += 1

def taylor_sum_counter(x, n):
    if abs(x) >= 1:
        raise ValueError("|x| має бути менше 1")
    gen = taylor_terms(x)
    total = 0.0
    for _ in range(n):
        total += next(gen)
    return total

def taylor_sum_epsilon(x, epsilon=1e-6, max_iter=1000):
    if abs(x) >= 1:
        raise ValueError("|x| має бути менше 1")
    gen = taylor_terms(x)
    total = 0.0
    prev_total = 0.0
    for k in range(max_iter):
        term = next(gen)
        total += term
        if k > 0 and abs(total - prev_total) < epsilon:
            return total, k + 1
        prev_total = total
    return total, max_iter

def save_results(x_values, n=10, filename="result_e.txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("Цикл з лічильником (n=10):\n")
        f.write("x\tНаближене\tMath\t\tРізниця\n")
        f.write("----------------------------------------\n")
        for x in x_values:
            try:
                approx = taylor_sum_counter(x, n)
                exact = math.log((1 + x) / (1 - x))
                f.write(f"{x:.3f}\t{approx:.8f}\t{exact:.8f}\t{abs(approx - exact):.2e}\n")
            except ValueError:
                f.write(f"{x:.3f}\tНедопустиме значення\n")

        f.write("\nЦикл з умовою (ε=1e-6):\n")
        f.write("x\tНаближене\tІтерації\tMath\t\tРізниця\n")
        f.write("------------------------------------------------\n")
        for x in x_values:
            try:
                approx, iterations = taylor_sum_epsilon(x)
                exact = math.log((1 + x) / (1 - x))
                f.write(f"{x:.3f}\t{approx:.8f}\t{iterations}\t\t{exact:.8f}\t{abs(approx - exact):.2e}\n")
            except ValueError:
                f.write(f"{x:.3f}\tНедопустиме значення\n")

if __name__ == "__main__":
    test_values = [0.1, 0.3, 0.5, 0.7, 0.9]
    save_results(test_values)