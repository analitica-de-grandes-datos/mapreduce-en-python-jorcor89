#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

temporal = {}

for linea in sys.stdin:    
    if linea != '\n':
        key, value = linea.split(',')
        value = value.rstrip()

        if key not in temporal:
            temporal[key] = [value]
        else:
            temporal[key].append(value)

for item in temporal:
    temporal[item] = [max(temporal[item]), min(temporal[item])]

for item in temporal.items():
    print(f'{str(item[0])}\t{item[1][0]}\t{item[1][1]}')