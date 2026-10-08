def perimeter(a: float, b: float, c: float) -> float:
    """Считает периметр треугольника.

    Args:
        a (float): первая сторона
        b (float): вторая сторона
        c (float): третья сторона

    Returns:
        float: периметр

    Example:
        >>> perimeter(1, 1, 1)
        3
    """
    return a + b + c

def area(a: float, h: float) -> float:
    """Считает площадь треугольника по стороне и высоте.

    Args:
        a (float): сторона
        h (float): высота

    Returns:
        float: площадь

    Example:
        >>> area(1, 2)
        1.0
    """
    return (a * h) / 2

