# exec_code.py
import sys
from io import StringIO
import time

def exec_code(code_str: str, input_str: str, TL: float) -> tuple[str, float]:
    """
    Devuelve una tupla con (output: str, elapsed_time: float)
    """
    original_stdin = sys.stdin
    original_stdout = sys.stdout
    
    sys.stdin = StringIO(input_str)
    output_capture = StringIO()
    sys.stdout = output_capture
    
    start_time = time.time()
    try:
        exec(code_str, {'__builtins__': __builtins__})
        elapsed = time.time() - start_time
        output = output_capture.getvalue()
    except Exception as e:
        elapsed = time.time() - start_time
        output = ""
        if elapsed > TL:
            elapsed = TL
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout
    
    # Asegurarse de devolver exactamente dos valores: str y float
    return str(output), float(elapsed)