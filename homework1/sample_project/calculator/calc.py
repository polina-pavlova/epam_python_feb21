def check_power_of_2(a: int) -> bool:
    if (
        a > 0
    ):  # all powers of 2 are positive, function must not work with negative numbers. Also function returned True for 0, but 0 is not power of 2.
        return not (
            a & (a - 1)
        )  # it's not obligate to use bool(), because 0 -- Flase, other numbers -- True
    else:
        return False
