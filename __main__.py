from random import randrange

table = []

for i in range(2, 10):
    for j in range(2, 10):
        table.append((f'{i} * {j}', i * j))

total_count = len(table)
error_count = 0

while table:
    i = randrange(0, len(table))
    print(table[i][0])
    need = table[i][1]
    v = -1
    while v != need:
        v = int(input('Result: '))
        if v != need:
            error_count += 1
            print('Wrong, try again')
    table.remove(table[i])
    print(f'Right! {len(table)} left')

print(f'Finish. Errors count {error_count}, total count {total_count}')
