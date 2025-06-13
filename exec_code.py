# exec_code.py
import sys
from io import StringIO
import time

def exec_code(code_str: str, input_str: str, TL: float) -> tuple[str, float]:
    original_stdin = sys.stdin
    original_stdout = sys.stdout
    
    # Preparamos el buffer de entrada
    input_buffer = StringIO(input_str)
    output_capture = StringIO()
    
    sys.stdin = input_buffer
    sys.stdout = output_capture
    
    start_time = time.time()
    output = ""
    elapsed = 0.0
    
    try:
        # Ejecutamos el código en un namespace limpio
        namespace = {'__name__': '__main__'}  # Para que `if __name__ == "__main__":` funcione
        exec(code_str, namespace)
        
        # Si hay una función main(), la ejecutamos
        if 'main' in namespace:
            # Rebobinamos el buffer de entrada antes de llamar a main()
            input_buffer.seek(0)
            namespace['main']()  # Ejecutamos main() directamente
        
        elapsed = time.time() - start_time
        output = output_capture.getvalue()
        
        # Verificamos timeout
        if elapsed > TL:
            output = f"Time Limit Exceeded (>{TL:.2f}s)"
            elapsed = TL
    
    except Exception as e:
        elapsed = time.time() - start_time
        output = f"Error: {str(e)}"
        if elapsed > TL:
            elapsed = TL
    
    finally:
        # Restauramos stdin y stdout
        sys.stdin = original_stdin
        sys.stdout = original_stdout
    
    return (output.strip(), float(elapsed))