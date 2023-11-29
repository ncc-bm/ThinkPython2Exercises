def power(k, n):
    if (n != 0):
        n = n - 1
        return k * power(k, n)
    else:
        return 1

def check_fermat(a, b, c, n):
    if (n > 2):
        a_of_n = power(a, n)
        b_of_n = power(b, n)
        c_of_n = power(c, n)

        if (a_of_n + b_of_n) == c_of_n:
            print('Holly smokes, Fermat was wrong!')
        else:
            print("No, that doesn't work.")
    else:
        print("n must be greate than 2")

def read_function_values():
    a = int(input('Please enter the value for variable a='))
    b = int(input('Please enter the value for variable b='))
    c = int(input('Please enter the value for variable c='))
    n = int(input('Please enter the value for variable n='))

    check_fermat(a, b, c, n)

read_function_values()
