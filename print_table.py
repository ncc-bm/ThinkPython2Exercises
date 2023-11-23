def print_table_top():
    print('+', ' -' * 4, ' +', ' -'*4, ' +')

def print_table_cell_line():
    print('|', ' ' * 9, '|', ' ' * 9, '|')

def print_table_cells():
    print_table_cell_line()
    print_table_cell_line()
    print_table_cell_line()
    print_table_cell_line()


print_table_top()
print_table_cells()
print_table_top()
print_table_cells()
print_table_top()
