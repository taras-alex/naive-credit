def is_creditable(age, salary):
    # позитивный тест со всеми валидными вводными
    """
    >>> is_creditable(30,40_000)
    True

    >>> is_creditable(70,40_000)
    False

    >>> is_creditable(30,10_000)
    False

    """
    min_age = 21
    max_age = 60
    min_salary = 30_000

    if age >= min_age:
        if age <= max_age
            if salary >= min_salary:  # magic numbers
                return True
            else:
                return False
    else:
        return False  # True - истинна, False - ложь
