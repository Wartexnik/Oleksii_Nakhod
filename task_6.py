def next_bigger(n):
    n = [int(el) for el in str(n)]
    swap_1 = -1
    swap_2 = -1

    # Traverse the number from the right, find the first digit that is less than the previous one
    for i in range(len(n)-1, 0, -1):
        if n[i] > n[i-1]:
            swap_1 = i-1
            break

    # If reached the start of the number, the digits are in descending order
    if swap_1 == -1:
        return -1

    # Traverse the number from the right, find the first digit that is greater than the previously found one
    for i in range(len(n)-1, swap_1, -1):
        if n[i] > n[swap_1]:
            swap_2 = i
            break

    # Swap the two digits
    n[swap_1], n[swap_2] = n[swap_2], n[swap_1]

    # Sort the last part of the number
    n[swap_1+1:] = sorted(n[swap_1+1:])

    return int("".join(map(str, n)))