# Calculator Skill - Technical Reference

This document provides detailed technical information about the calculator skill implementation.

## Architecture

The calculator skill consists of:
1. A Python script (`calculate.py`) that safely evaluates mathematical expressions
2. A security layer that prevents code injection
3. A comprehensive set of mathematical functions from Python's `math` module

## Security Model

### Safe Evaluation

The script uses Python's `eval()` function with restricted globals and locals:
```python
result = eval(expression, {"__builtins__": {}}, allowed_names)
```

This approach:
- Disables all built-in functions by setting `__builtins__` to an empty dict
- Only allows explicitly whitelisted functions and constants
- Prevents import statements, file operations, and arbitrary code execution

### Blocked Patterns

The following patterns are automatically rejected:
- Double underscores (`__`) - Prevents access to magic methods
- `import` statements
- `exec`, `eval` calls
- `open` file operations
- `input` functions

### Error Types

The script distinguishes between:

1. **ZeroDivisionError**: Division by zero
   - Example: `1 / 0`
   - Handled with specific error message

2. **SyntaxError**: Invalid Python syntax
   - Example: `2 +* 3`
   - Reports syntax issues clearly

3. **NameError**: Undefined function or variable
   - Example: `unknown_func(5)`
   - Indicates what name is not recognized

4. **ValueError**: General mathematical errors
   - Example: `sqrt(-1)` (domain error)
   - Catches other calculation issues

## Precision and Limitations

### Floating Point Precision

Results are rounded to 10 decimal places to avoid floating-point artifacts:
```python
result = round(result, 10)
```

Integer results are automatically converted:
```python
if result.is_integer():
    result = int(result)
```

### Large Numbers

- Python handles arbitrarily large integers
- Floating-point numbers follow IEEE 754 double precision
- Very large exponents may result in `inf`

### Domain Restrictions

Some functions have domain restrictions:
- `sqrt(x)`: requires x ≥ 0
- `log(x)`: requires x > 0
- `asin(x)`, `acos(x)`: require -1 ≤ x ≤ 1
- `factorial(x)`: requires x ≥ 0 and x is an integer

## Performance

- Single expression evaluation: < 1ms for most operations
- Memory usage: Minimal (< 10MB)
- No external dependencies beyond Python standard library

## Extending the Calculator

To add new functions:

1. Import the function (if from a module)
2. Add it to the `allowed_names` dictionary
3. Document it in the main SKILL.md
4. Add examples to references/examples.md

Example:
```python
allowed_names = {
    # ... existing functions ...
    'gcd': math.gcd,  # Add greatest common divisor
}
```

## Exit Codes

- `0`: Successful calculation
- `1`: Error occurred (check stderr for details)

## Command Line Interface
```bash
python scripts/calculate.py "expression"
```

- Accepts a single argument: the expression to evaluate
- Returns result to stdout
- Returns errors to stderr