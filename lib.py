def is_creditabele (age, salary):
    # первый тест - всегда True
    """
    >>> is_creditabele(30, 40_000)
    True

    >>> is_creditabele(20, 40_000)
    False

    >>> is_creditabele(34, 20_000)
    False
    """
    min_age = 21
    max_age = 60
    min_salary = 30_000

    if age >= min_age:
        if age < max_age:
            if salary>= min_salary:
                return True

            else:
                return False
        else:
            return False
    else:
        return False