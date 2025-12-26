# Complete Function Reference

This document lists all available mathematical functions and constants in the calculator skill.

## Basic Functions

### abs(x)
Returns the absolute value of x.
```python
abs(-5)    # Result: 5
abs(3.14)  # Result: 3.14
```

### round(x[, n])
Rounds x to n decimal places (default: 0).
```python
round(3.7)      # Result: 4
round(3.14159, 2)  # Result: 3.14
```

### min(*args)
Returns the smallest of the input values.
```python
min(5, 2, 8, 1)  # Result: 1
```

### max(*args)
Returns the largest of the input values.
```python
max(5, 2, 8, 1)  # Result: 8
```

### pow(x, y)
Returns x raised to the power y. Equivalent to `x ** y`.
```python
pow(2, 8)   # Result: 256
2 ** 8      # Result: 256
```

## Trigonometric Functions

All trigonometric functions work in radians. Use `radians()` to convert from degrees.

### sin(x)
Returns the sine of x (in radians).
```python
sin(0)           # Result: 0.0
sin(pi/2)        # Result: 1.0
sin(radians(30)) # Result: 0.5
```

### cos(x)
Returns the cosine of x (in radians).
```python
cos(0)           # Result: 1.0
cos(pi)          # Result: -1.0
cos(radians(60)) # Result: 0.5
```

### tan(x)
Returns the tangent of x (in radians).
```python
tan(0)           # Result: 0.0
tan(pi/4)        # Result: 1.0
tan(radians(45)) # Result: 1.0
```

### asin(x), acos(x), atan(x)
Inverse trigonometric functions. Return value in radians.
```python
asin(0.5)        # Result: 0.5236 (30 degrees)
degrees(asin(0.5))  # Result: 30.0
```

### sinh(x), cosh(x), tanh(x)
Hyperbolic trigonometric functions.
```python
sinh(0)  # Result: 0.0
cosh(0)  # Result: 1.0
```

## Exponential and Logarithmic Functions

### sqrt(x)
Returns the square root of x. x must be non-negative.
```python
sqrt(16)   # Result: 4.0
sqrt(2)    # Result: 1.4142135623730951
```

### exp(x)
Returns e raised to the power x.
```python
exp(0)   # Result: 1.0
exp(1)   # Result: 2.718281828459045 (e)
```

### log(x[, base])
Returns the logarithm of x to the given base (default: e).
```python
log(e)      # Result: 1.0
log(100, 10)  # Result: 2.0
```

### log10(x)
Returns the base-10 logarithm of x.
```python
log10(100)   # Result: 2.0
log10(1000)  # Result: 3.0
```

### log2(x)
Returns the base-2 logarithm of x.
```python
log2(8)    # Result: 3.0
log2(1024) # Result: 10.0
```

## Rounding Functions

### floor(x)
Returns the largest integer less than or equal to x.
```python
floor(3.7)   # Result: 3
floor(-2.3)  # Result: -3
```

### ceil(x)
Returns the smallest integer greater than or equal to x.
```python
ceil(3.2)   # Result: 4
ceil(-2.7)  # Result: -2
```

## Angle Conversion

### radians(x)
Converts angle x from degrees to radians.
```python
radians(180)  # Result: 3.141592653589793 (pi)
radians(90)   # Result: 1.5707963267948966 (pi/2)
```

### degrees(x)
Converts angle x from radians to degrees.
```python
degrees(pi)    # Result: 180.0
degrees(pi/2)  # Result: 90.0
```

## Special Functions

### factorial(x)
Returns x! (factorial of x). x must be a non-negative integer.
```python
factorial(5)  # Result: 120
factorial(0)  # Result: 1
```

## Constants

### pi
The mathematical constant π (pi) ≈ 3.14159.
```python
pi           # Result: 3.141592653589793
2 * pi       # Result: 6.283185307179586
```

### e
The mathematical constant e (Euler's number) ≈ 2.71828.
```python
e            # Result: 2.718281828459045
log(e)       # Result: 1.0
```

### tau
The mathematical constant τ (tau) = 2π ≈ 6.28318.
```python
tau          # Result: 6.283185307179586
```

## Operator Precedence

1. Parentheses: `()`
2. Exponentiation: `**`
3. Unary plus and minus: `+x`, `-x`
4. Multiplication, Division: `*`, `/`
5. Addition, Subtraction: `+`, `-`

Example:
```python
2 + 3 * 4      # Result: 14 (not 20)
(2 + 3) * 4    # Result: 20
2 ** 3 ** 2    # Result: 512 (2^(3^2), right associative)
```