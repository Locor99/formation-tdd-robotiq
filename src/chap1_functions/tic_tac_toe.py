def tic_tac_toe(target, toe=None):
    """
    This function will count from 1 to target by printing
    tic each time it finds a multiple of 3 and
    tac each time it finds a multiple of 5.
    If toe is set to an integer, it will also say toe when it find a multiple of this number
    :returns the resulting string.
    """
    result = ""
    space = " "
    TIC = 3
    TAC = 5

    for value in range(1, target + 1):
        to_append = ""
        if _is_a_multiple(value, TIC):
            to_append = to_append + "tic"

        if _is_a_multiple(value, TAC):
            to_append = to_append + "tac"

        if toe and _is_a_multiple(value, toe):
            to_append = to_append + "toe"

        if not to_append:
            to_append = str(value)

        result = result + space + to_append

    return result.strip()

def _is_a_multiple(value, factor):
    return value % factor == 0
