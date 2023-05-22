#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

temporal = {}

for linea in sys.stdin:    
    linea = linea.rstrip()
    if linea not in temporal:
        temporal[linea] = [linea]
    else:
        temporal[linea].append(linea)

for item in temporal:
    temporal[item] = len(temporal[item])

for item in temporal.items():
    print(f'{item[0]}\t{str(item[1])}')