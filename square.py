def area(a: float) -> float:
    """Вычисляет площадь квадрата по длине его стороны.

    Args:
        a (float): длина стороны квадрата.

    Returns:
        float: площадь квадрата.

    Example:
        >>> area(2)
        4
    """
    return a * a


def perimeter(a: float) -> float:
    """Вычисляет периметр квадрата по длине его стороны.

    Args:
        a (float): длина стороны квадрата.

    Returns:
        float: периметр квадрата.

    Example:
        >>> perimeter(2)
        8
    """
    return 4 * a
