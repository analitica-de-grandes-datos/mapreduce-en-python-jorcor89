#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for linea in sys.stdin:
    numero, caracteres = linea.split('\t')

    for caracter in caracteres:
        if caracter != ',':
            print(f'{caracter},{numero}')