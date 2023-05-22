#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

temporal = []

for linea in sys.stdin:    
    if linea != '\n':
        char, date, number = linea.split('   ')
        mapped_tuple = (char, date, int(number))

        temporal.append(mapped_tuple)

temporal = sorted(temporal, key=lambda x: x[2])[:6]

for item in temporal:
    print(f'{str(item[0])}   {item[1]}   {item[2]}')