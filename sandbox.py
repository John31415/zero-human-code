from llm_sandbox import CodeSandbox

# Configuración del sandbox
sandbox = CodeSandbox(
    allowed_modules=["math"],  # Lista blanca de módulos permitidos
    memory_limit=512,          # MB
    timeout=10,               # Segundos
)

# Código a ejecutar (como string)
code = """
import math
print(math.sqrt(16))
"""

# Ejecución
result = sandbox.execute(code)
print("Output:", result.output)
print("Errors:", result.errors)
print("Metrics:", result.metrics)  # Uso de CPU/memoria