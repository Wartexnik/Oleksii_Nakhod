def digital_root(n):
    """
    Finds recursive digit sum which is equal to
    n%9, if n%9 != 0
    n, if n == 0
    9, if n%9 == 0 and n != 0
    """
    return n%9 or (n and 9)