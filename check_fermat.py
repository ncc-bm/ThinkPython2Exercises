def power(a, n):
    if (n != 0):
        print(a, n)
        n = n - 1
        return a * power(a, n)
    else:
        return 1

def check_fermat(a, b, c, n):
    if (n > 2):
        pass


print(power(2,2))
