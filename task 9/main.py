from Rational import Rational
from RationalList import RationalList


def evaluate_expression(tokens):
    processed = []
    i = 0
    while i < len(tokens):
        current = tokens[i]
        if isinstance(current, str) and current == '*':
            left = processed.pop()
            i += 1
            right = tokens[i]
            processed.append(left * right)
        else:
            processed.append(current)
        i += 1

    result = processed[0]
    i = 1
    while i < len(processed):
        op = processed[i]
        right = processed[i + 1]
        if op == '+':
            result += right
        elif op == '-':
            result -= right
        i += 2
    return result

if __name__ == "__main__":
    filenames = ["input01.txt", "input02.txt", "input03.txt"]
    outputnames = ["output01.txt", "output02.txt", "output03.txt"]

    for i in range(len(filenames)):
        input_file = filenames[i]
        output_file = outputnames[i]

        with open(input_file, encoding='utf-8') as f_in:
            with open(output_file, "w", encoding='utf-8') as f_out:
                f_out.write(f"{input_file}:\n")
                for line in f_in:
                    line = line.strip()
                    if not line:
                        continue
                    tokens = line.split()
                    parsed_tokens = []
                    try:
                        for token in tokens:
                            if token in ('+', '-', '*'):
                                parsed_tokens.append(token)
                            else:
                                if '/' in token:
                                    parsed_tokens.append(Rational(token))
                                else:
                                    parsed_tokens.append(Rational(int(token)))

                        # Обчислюємо вираз
                        result = evaluate_expression(parsed_tokens)
                        f_out.write(f"{line} = {result}\n")

                    except Exception as e:
                        f_out.write(f"Помилка у виразі '{line}': {e}\n")