def int_to_ip(n):
    digits = [0, 0, 0, 0]
    for i in range(4):
        digits[3 - i] = int(n % 256)
        n //= 256
    return ".".join(map(str, digits))
