def print_cell_hor_line():
    print(' -' * 4, end='')
    print(' ', end='')

def print_cell_corner():
    print('+', end='')

def print_cell_top():
    print_cell_corner()
    print_cell_hor_line()

def print_cell_vert_line():
    print('|', ' ' * 8, end='')

def print_table_vert_one_line():
    do_twice(print_cell_vert_line)
    print('|')

def print_table_vert_line():
    do_twice(print_table_vert_one_line)
    do_twice(print_table_vert_one_line)

def do_twice(f):
    f()
    f()

def print_table_top():
    do_twice(print_cell_top)
    print_cell_corner()
    print()


print_table_top()
print_table_top()
print_table_vert_line()
print_table_top()
print_table_vert_line()
print_table_top()


def yacheyka_gorizontal_chizigi():
    print(' -'*4, ' ', end='', sep='')

def burchak(songi = False):
    if songi:
        print('+')
    else:
        print('+', end='')



# burchak()
# yacheyka_gorizontal_chizigi()
# burchak()
# yacheyka_gorizontal_chizigi()
# burchak()

# burchak()
# yacheyka_gorizontal_chizigi()
# burchak()
# yacheyka_gorizontal_chizigi()
# burchak('songi')
