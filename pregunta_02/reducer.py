#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys


temporal = {}

for linea in sys.stdin:    
    purpose, amount = linea.split(',')

    if purpose not in temporal:
        temporal[purpose] = [int(amount)]
    else:
        temporal[purpose].append(int(amount))

for item in temporal:
    temporal[item] = max(temporal[item])

for item in temporal.items():
    print(item[0].rstrip() + '\t' + str(item[1]))