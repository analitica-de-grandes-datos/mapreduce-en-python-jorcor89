#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

temporal = {}

for linea in sys.stdin:    
    if linea != '\n':
        key, value = linea.split(',')
        temporal[key] = value.rstrip()


temporal = sorted(temporal.items(), key=lambda x: x[1])

for item in temporal:
    print(f'{item[0]},{item[1]}')