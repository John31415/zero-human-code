from read_test_cases import read_test_cases
from ask_LLM import ask
from run_code import run
import re
import os
import time

PROMPT1 = "Eres programador competitivo. Gran Maestro Legendario en Codeforces. Resuelve el siguiente problema, escribe el codigo en python, asegurate de implementarlo de manera eficiente en cuanto a tiempo y memoria:\n"
PROMPT2_1 = "\n\nPara resolver este problema:\n\n"
PROMPT2_2 = "\n\nPropusiste el siguiente codigo:\n\n"
PROMPT2_3 = "\n\nPero obtuvo el veredicto:\n\n"
PROMPT2_4 = "\n\nIntentalo de nuevo.\n\n"
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
    attempts = 10
    PROMPT = PROMPT1 + problem_statement + HINT1 #+ HINT2 + HINT3
    VEREDICTO = ""
    while attempts:
        attempts -= 1
        ans_LLM = ask(PROMPT) 
        print(ans_LLM)
        code = get_code(ans_LLM)
        with open("LLM_solution.py", 'w') as f:
            f.write(code)
        tests = read_test_cases()
        TL = 10.0
        band = run(code, tests, TL)
        if band == 1:
            VEREDICTO = "ACCEPTED"
            break
        veredicto = "TIEMPO LIMITE EXCEDIDO"
        if band == 0:
            veredicto = "RESPUESTA INCORRECTA"
        PROMPT = PROMPT2_1 + problem_statement + PROMPT2_2 + code + PROMPT2_3 + veredicto + PROMPT2_4 + HINT1 #+ HINT2 + HINT3
        VEREDICTO = veredicto
    if VEREDICTO == "ACCEPTED":
        print(f"\033[32m{VEREDICTO}\033[0m")
    if VEREDICTO == "TIEMPO LIMITE EXCEDIDO":
        print("\033[34mTIME LIMIT EXCEECED\033[0m")
    if VEREDICTO == "RESPUESTA INCORRECTA":
        print("\033[31mWROND ANSWER\033[0m")
        

if __name__ == "__main__":
    main()