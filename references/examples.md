# Domain-Specific Calculation Examples

This document provides practical examples of using the calculator skill across different domains.

## Physics Calculations

### Projectile Motion
Calculate the range of a projectile with initial velocity and angle:
```python
# Given: initial velocity = 20 m/s, angle = 45 degrees
# Range formula: (v^2 * sin(2*theta)) / g
python scripts/calculate.py "(20**2 * sin(2 * radians(45))) / 9.8"
# Result: 40.816326530612244
```

### Kinetic Energy
Calculate kinetic energy (KE = 0.5 * m * v²):
```python
# Mass = 10 kg, Velocity = 15 m/s
python scripts/calculate.py "0.5 * 10 * 15**2"
# Result: 1125.0
```

### Wave Frequency
Calculate frequency from wavelength (f = c / λ):
```python
# Speed of light = 3e8 m/s, wavelength = 500e-9 m (500 nm)
python scripts/calculate.py "3e8 / 500e-9"
# Result: 6e14 (600 THz)
```

## Finance Calculations

### Compound Interest
Calculate compound interest (A = P(1 + r)^t):
```python
# Principal = $1000, Rate = 5% (0.05), Time = 10 years
python scripts/calculate.py "1000 * (1 + 0.05)**10"
# Result: 1628.89
```

### Monthly Payment (approximation)
Simple interest calculation:
```python
# Loan = $100,000, Annual rate = 4.5%, Years = 30
# Monthly payment approximation
python scripts/calculate.py "(100000 * 0.045 * 30) / (30 * 12)"
# Result: 375.0
```

### Return on Investment (ROI)
```python
# Initial investment = $5000, Final value = $7500
python scripts/calculate.py "((7500 - 5000) / 5000) * 100"
# Result: 50.0 (50% ROI)
```

## Engineering Calculations

### Electrical Power
Calculate power from voltage and current (P = V * I):
```python
# Voltage = 120V, Current = 5A
python scripts/calculate.py "120 * 5"
# Result: 600 (watts)
```

### Ohm's Law
Calculate resistance (R = V / I):
```python
# Voltage = 12V, Current = 0.5A
python scripts/calculate.py "12 / 0.5"
# Result: 24.0 (ohms)
```

### Area of a Circle
```python
# Radius = 5 meters
python scripts/calculate.py "pi * 5**2"
# Result: 78.53981633974483
```

### Volume of a Cylinder
```python
# Radius = 3m, Height = 10m
python scripts/calculate.py "pi * 3**2 * 10"
# Result: 282.7433388230814
```

## Statistics Calculations

### Mean (Average)
```python
# Values: 10, 20, 30, 40, 50
python scripts/calculate.py "(10 + 20 + 30 + 40 + 50) / 5"
# Result: 30.0
```

### Percentage
```python
# What is 15% of 200?
python scripts/calculate.py "200 * 0.15"
# Result: 30.0
```

### Percentage Change
```python
# From 50 to 75
python scripts/calculate.py "((75 - 50) / 50) * 100"
# Result: 50.0 (50% increase)
```

## Geometry Calculations

### Pythagorean Theorem
Calculate hypotenuse (c = √(a² + b²)):
```python
# Sides: a=3, b=4
python scripts/calculate.py "sqrt(3**2 + 4**2)"
# Result: 5.0
```

### Surface Area of a Sphere
```python
# Radius = 4m
python scripts/calculate.py "4 * pi * 4**2"
# Result: 201.06192982974676
```

### Volume of a Sphere
```python
# Radius = 3m
python scripts/calculate.py "(4/3) * pi * 3**3"
# Result: 113.09733552923255
```

## Computer Science

### Binary to Decimal
```python
# Binary 1101 = ?
python scripts/calculate.py "1*2**3 + 1*2**2 + 0*2**1 + 1*2**0"
# Result: 13
```

### Powers of 2
```python
# 2^10 (1 KB in bytes)
python scripts/calculate.py "2**10"
# Result: 1024
```

### Logarithmic Complexity
Calculate iterations for binary search:
```python
# Array size = 1,000,000
python scripts/calculate.py "log2(1000000)"
# Result: 19.931568569324174 (approximately 20 steps)
```

## Chemistry Calculations

### Molar Mass Calculation
Example: Water (H₂O) - 2H + 1O:
```python
# H = 1.008, O = 16.00
python scripts/calculate.py "2 * 1.008 + 16.00"
# Result: 18.016
```

### pH Calculation
```python
# [H+] = 1e-7 (neutral)
python scripts/calculate.py "-log10(1e-7)"
# Result: 7.0
```

## Conversion Examples

### Temperature Conversion
Celsius to Fahrenheit:
```python
# 25°C to Fahrenheit
python scripts/calculate.py "25 * 9/5 + 32"
# Result: 77.0
```

### Speed Conversion
km/h to m/s:
```python
# 100 km/h to m/s
python scripts/calculate.py "100 * 1000 / 3600"
# Result: 27.77777777777778
```

### Energy Conversion
Calories to Joules:
```python
# 100 calories to joules
python scripts/calculate.py "100 * 4.184"
# Result: 418.4
```

## Complex Expressions

### Quadratic Formula
Calculate roots using (-b ± √(b²-4ac)) / 2a:
```python
# For x² + 2x - 3 = 0 (a=1, b=2, c=-3)
# Positive root:
python scripts/calculate.py "(-2 + sqrt(2**2 - 4*1*(-3))) / (2*1)"
# Result: 1.0

# Negative root:
python scripts/calculate.py "(-2 - sqrt(2**2 - 4*1*(-3))) / (2*1)"
# Result: -3.0
```

### Standard Deviation (simplified)
For small datasets:
```python
# Values: 2, 4, 4, 4, 5, 5, 7, 9
# Mean = 5, calculate variance first
python scripts/calculate.py "sqrt(((2-5)**2 + (4-5)**2 + (4-5)**2 + (4-5)**2 + (5-5)**2 + (5-5)**2 + (7-5)**2 + (9-5)**2) / 8)"
# Result: 2.0
```