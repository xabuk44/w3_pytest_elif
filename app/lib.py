def is_creditabele (age, salary):
    # первый тест - всегда True
    """
    >>> is_creditabele(30, 40_000)
    True

    >>> is_creditabele(20, 40_000)
    False

    >>> is_creditabele(65, 20_000)
    False

    >>> is_creditabele(25, 20_000)
    False
    """
    min_age = 21
    max_age = 60
    min_salary = 30_000


    # Alt + Ins    что то создать
    # Alt + Enter   что то поправить

    if age < min_age:
        return False     #early exit
    if age > max_age:
        return False
    if salary < min_salary:
        return False
    # если был Return False, то после мы не пойдем
    return True

# [pytest]
# addopts = --doctest-modules --doctest-continue-on-failure
# doctest_optionflags = ELLIPSIS NORMALIZE_WHITESPACE