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
            temporal[key] = [float(value)]
        else:
            temporal[key].append(float(value))

for item in temporal:
    temporal[item] = [sum(temporal[item]), sum(temporal[item]) / len(temporal[item])]

for item in temporal.items():
    print(f'{str(item[0])}\t{item[1][0]}\t{item[1][1]}')