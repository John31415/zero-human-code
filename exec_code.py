import sys
from io import StringIO
import time

def exec_code(codigo: str, entrada: str) -> str:
    try:
        compile(codigo, "<string>", "exec")
    except SyntaxError as e:
        return (f"Traceback (most recent call last):\n"
                f"  File \"<string>\", line {e.lineno}\n"
                f"    {e.text.strip()}\n"
                f"    {' '*(e.offset-1)}^\n"
                f"{type(e).__name__}: {e}")
    original_stdin = sys.stdin
    original_stdout = sys.stdout
    try:
        sys.stdin = StringIO(entrada)
        output_capture = StringIO()
        sys.stdout = output_capture
        start = time.time()
        exec(codigo, {})
        end = time.time()
        elapsed = end - start
        output = output_capture.getvalue()
        return (output, elapsed)
    except Exception as e:
        return (f"Traceback (most recent call last):\n"
                f"  File \"<string>\", line 1\n"
                f"{type(e).__name__}: {e}", 0.0)
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout