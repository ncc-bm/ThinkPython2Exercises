def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_twice(f, val):
    f(val)
    f(val)

def print_spam(val):
    print(val)

def do_four(f, val):
    do_twice(f, val)
    do_twice(f, val)

do_four(print, 'spam')