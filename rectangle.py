def area(a: float, b: float) -> float:
    """Считает площадь прямоугольника.

    Args:
        a (float): длина
        b (float): ширина

    Returns:
        float: площадь

    Example:
        area(3, 4)

    Return:
        12
    """
    return a * b


def perimeter(a: float, b: float) -> float:
    """Считает периметр прямоугольника.

    Args:
        a (float): длина
        b (float): ширина

    Returns:
        float: периметр

    Example:
        perimeter(3, 4)

    Return:
        14
    """
    return 2 * (a + b)