#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for linea in sys.stdin:
    print(linea.split('   ')[1].split('-')[1])