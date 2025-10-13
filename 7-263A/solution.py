rows = 5
beautiful_position = 2

for row in range(rows):
    columns = input().split()
    if '1' in columns:
        column = columns.index('1')
        beautiful_row_steps = int(row) - beautiful_position
        beautiful_column_steps = int(column) - beautiful_position
        print(abs(beautiful_row_steps) + abs(beautiful_column_steps))
        break
