def is_triangle(a, b, c):
    if (a < (b+c) and b < (a+c) and c < (a+b)):
        return "Yes"
    else:
        return "No"

def get_triangle_params():
    a = input("Get the value for a side 'a'=")
    b = input("Get the value for a side 'b'=")
    c = input("Get the value for a side 'c'=")

    print(is_triangle(int(a), int(b), int(c)))

get_triangle_params()