def reverse(x: int) -> int:
    rev_string = ""
    int_string = str(x)
    neg = False

    if int_string[0] == '-':
        int_string = int_string[1::]
        neg = True

    if not int_string[-1]:
        int_string = int_string[0:-1]

    for num in reversed(int_string):
        rev_string += num

    if neg:
        new_string = '-' + rev_string
        return int(new_string) if int(new_string) >= -2 ** 31 else 0
    else:
        return int(rev_string) if int(rev_string) <= 2 ** 31 - 1 else 0
