# run_code.py
from exec_code import exec_code

def normalize_output(s):
    """Normaliza el output para comparación robusta"""
    if not s:
        return ''
    return '\n'.join(line.rstrip() for line in s.replace('\r\n', '\n').splitlines()).strip()

def run(code, tests, TL):
    for i, (code_input, expected_output) in enumerate(tests):
        # Asegurarse de recibir exactamente dos valores
        execution_result = exec_code(code, code_input, TL)
        
        # Verificación de seguridad
        if not isinstance(execution_result, tuple) or len(execution_result) != 2:
            print(f"Error: exec_code no devolvió (output, time). Devuelve: {execution_result}")
            return 0
            
        output, elapsed_time = execution_result
        
        # Conversión explícita a float
        try:
            elapsed_time = float(elapsed_time)
        except (TypeError, ValueError):
            print(f"Error: tiempo de ejecución no es numérico: {elapsed_time}")
            elapsed_time = TL  # Tratar como timeout
            
        if elapsed_time >= TL:
            print(f"Time Limit Exceeded, >{TL:.3f} seconds.")
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
            print(f"Wrong Answer on test {i}, running time: {elapsed_time:.3f} seconds.")
            return 0
    return 1