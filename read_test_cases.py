import os
from pathlib import Path

def leer_primeros_caracteres(archivo, max_caracteres=20):
    with open(archivo, 'r') as f:
        contenido = f.read(max_caracteres)
    return contenido

def read_test_cases(carpeta = 'test cases'):
    carpeta_path = Path(carpeta)
    pares = {}
    for archivo in carpeta_path.glob('*.in'):
        nombre = archivo.stem
        num = int(nombre.split('.')[-1])
        if num not in pares:
            pares[num] = {}
        pares[num]['in'] = archivo
    for archivo in carpeta_path.glob('*.out'):
        nombre = archivo.stem
        num = int(nombre.split('.')[-1])
        if num not in pares:
            pares[num] = {}
        pares[num]['out'] = archivo
    lista = []
    for num in sorted(pares.keys()):
        arch_in = pares[num].get('in')
        arch_out = pares[num].get('out')
        with open(arch_in, 'r') as f_in, open(arch_out, 'r') as f_out:
            contenido_in = f_in.read()
            contenido_out = f_out.read()
            lista.append((contenido_in,contenido_out))
    return lista

# carpeta = 'test cases'