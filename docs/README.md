# Table of Contents

* [circle](#circle)
  * [area](#circle.area)
  * [perimeter](#circle.perimeter)
* [triangle](#triangle)
  * [perimeter](#triangle.perimeter)
  * [area](#triangle.area)
* [rectangle](#rectangle)
  * [area](#rectangle.area)
  * [perimeter](#rectangle.perimeter)
* [square](#square)
  * [area](#square.area)
  * [perimeter](#square.perimeter)

<a id="circle"></a>

# circle

<a id="circle.area"></a>

#### area

```python
def area(r: float) -> float
```

Вычисляет площадь круга по его радиусу.

**Arguments**:

- `r` _float_ - радиус круга.
  

**Returns**:

- `float` - площадь круга.
  

**Example**:

  >>> area(2)
  12.566370614359172

<a id="circle.perimeter"></a>

#### perimeter

```python
def perimeter(r: float) -> float
```

Вычисляет длину окружности по её радиусу.

**Arguments**:

- `r` _float_ - радиус круга.
  

**Returns**:

- `float` - длина окружности.
  

**Example**:

  >>> perimeter(2)
  12.566370614359172

<a id="triangle"></a>

# triangle

<a id="triangle.perimeter"></a>

#### perimeter

```python
def perimeter(a: float, b: float, c: float) -> float
```

Считает периметр треугольника.

**Arguments**:

- `a` _float_ - первая сторона
- `b` _float_ - вторая сторона
- `c` _float_ - третья сторона
  

**Returns**:

- `float` - периметр
  

**Example**:

  >>> perimeter(1, 1, 1)
  3

<a id="triangle.area"></a>

#### area

```python
def area(a: float, h: float) -> float
```

Считает площадь треугольника по стороне и высоте.

**Arguments**:

- `a` _float_ - сторона
- `h` _float_ - высота
  

**Returns**:

- `float` - площадь
  

**Example**:

  >>> area(1, 2)
  1.0

<a id="rectangle"></a>

# rectangle

<a id="rectangle.area"></a>

#### area

```python
def area(a: float, b: float) -> float
```

Считает площадь прямоугольника.

**Arguments**:

- `a` _float_ - длина
- `b` _float_ - ширина
  

**Returns**:

- `float` - площадь
  

**Example**:

  >>> area(3, 4)
  12

<a id="rectangle.perimeter"></a>

#### perimeter

```python
def perimeter(a: float, b: float) -> float
```

Считает периметр прямоу
гольника.

**Arguments**:

- `a` _float_ - длина
- `b` _float_ - ширина
  

**Returns**:

- `float` - периметр
  

**Example**:

  >>> perimeter(3, 4)
  14

<a id="square"></a>

# square

<a id="square.area"></a>

#### area

```python
def area(a: float) -> float
```

Вычисляет площадь квадрата по длине его стороны.

**Arguments**:

- `a` _float_ - длина стороны квадрата.
  

**Returns**:

- `float` - площадь квадрата.
  

**Example**:

  >>> area(2)
  4

<a id="square.perimeter"></a>

#### perimeter

```python
def perimeter(a: float) -> float
```

Вычисляет периметр квадрата по длине его стороны.

**Arguments**:

- `a` _float_ - длина стороны квадрата.
  

**Returns**:

- `float` - периметр квадрата.
  

**Example**:

  >>> perimeter(2)
  8

