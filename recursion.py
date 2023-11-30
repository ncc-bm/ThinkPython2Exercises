def recurse(n, s):
    """ Gets two number n and s. If number n is not equal to 0 then
    call the function recursively with dicreased n-1 and n+s. If n is equal to 0
    print s
    """
    if n == 0:
        print(s)
    else:
        print(n, s)
        recurse(n-1, n+s)

recurse(3, 0)
