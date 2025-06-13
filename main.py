from read_test_cases import read_test_cases
from ask_LLM import ask
from run_code import run
import re
import os

PROMPT = "Eres programador competitivo. Gran Maestro Legendario en Codeforces. Resuelve el siguiente problema, escribe el codigo en python, asegurate de implementarlo de manera eficiente en cuanto a tiempo y memoria:\n"
HINT1 = "\nLos numeros con cantidad impar de divisores son los cuadrados perfectos\n"
HINT2 = "\nLa suma de los cuadrados perfectos tiene formula cerrada\n"
HINT3 = "\nLa respuesta puede ser muy grande\n"

def get_problem_statement():
    with open('problem_statement.txt', 'r', encoding='latin-1') as archivo:
        contenido = archivo.read()
    return contenido

def get_code(text):
    code = re.findall(r"```(?:python)?\n(.*?)```", text, re.DOTALL)
    return "\n".join(code)

def main():
    problem_statement = get_problem_statement()
    ans_LLM = ask(PROMPT + problem_statement + HINT1 + HINT2 + HINT3) 
    print(ans_LLM)
    code = get_code(ans_LLM)
    with open("LLM_solution.py", 'w') as f:
        f.write(code)
    tests = read_test_cases()
    run(code, tests)

if __name__ == "__main__":
    main()