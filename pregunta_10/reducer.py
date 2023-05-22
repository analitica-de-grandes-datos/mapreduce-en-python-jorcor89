#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

temporal = {}

for linea in sys.stdin:    
    if linea != '\n':
        key, value = linea.split(',')

        if key != '':
            value = value.rstrip()

            if key not in temporal:
                temporal[key] = [int(value)]
            else:
                temporal[key].append(int(value))

for item in temporal.items():
    print(f'{item[0]}\t{",".join(list(map(lambda x: str(x), sorted(item[1]))))}')