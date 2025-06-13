# run_code.py
from exec_code import exec_code

def normalize_output(s):
    if not s:
        return ''
    return '\n'.join(line.rstrip() for line in s.replace('\r\n', '\n').splitlines()).strip()

def run(code, tests, TL):
    for i, (code_input, expected_output) in enumerate(tests):
        output, elapsed_time = exec_code(code, code_input, TL)
        elapsed_time = float(elapsed_time)
        if elapsed_time >= TL:
            print(f"Time Limit Exceeded on test {i}, >{TL:.3f} seconds.")
            return -1
        norm_output = normalize_output(output)
        norm_expected = normalize_output(expected_output)
        if norm_output == norm_expected:
            print(f"Test {i} passed, running time: {elapsed_time:.3f} seconds.")
        else:
            if i == 0:
                print("=== Diferencia ===")
                print(f"Esperado: {repr(norm_expected)}")
                print(f"Obtenido: {repr(norm_output)}")
                print(f"Obtenido2: {repr(output)}")
            print(f"Wrong Answer on test {i}, running time: {elapsed_time:.3f} seconds.")
            return 0
    return 1