#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for linea in sys.stdin:
    print(f"{linea.split(',')[3]},{linea.split(',')[4]}")