#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

contar = {}

for linea in sys.stdin:
    if linea in contar:
        contar[linea] = contar[linea] + 1
    else:
        contar[linea] = 1

for item in contar.items():
    print(item[0].rstrip() + '\t' + str(item[1]))