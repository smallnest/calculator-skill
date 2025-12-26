---
name: calculator-skill
description: Perform mathematical calculations including basic arithmetic, advanced operations, and expression evaluation. Use when the user needs to calculate numbers, solve math problems, or evaluate mathematical expressions.
license: MIT
metadata:
  author: example-author
  version: "1.0.0"
allowed-tools: Bash(python:scripts/calculate.py)
---

# Calculator Skill

A comprehensive calculator skill that performs various mathematical operations through a Python script.

## When to Use This Skill

Use this skill when:
- The user asks to calculate or compute mathematical expressions
- Basic arithmetic is needed (addition, subtraction, multiplication, division)
- Advanced operations are required (exponents, square roots, logarithms)
- Complex expressions need to be evaluated
- The user mentions math, calculations, or numbers that need processing

## Supported Operations

### Basic Arithmetic
- Addition: `5 + 3`
- Subtraction: `10 - 4`
- Multiplication: `6 * 7`
- Division: `20 / 4`

### Advanced Operations
- Exponentiation: `2 ** 8` (2 to the power of 8)
- Square root: `sqrt(16)`
- Trigonometry: `sin(0)`, `cos(0)`, `tan(45)`
- Logarithms: `log(100)`, `log10(100)`
- Absolute value: `abs(-5)`

### Constants
- Pi: `pi` (3.14159...)
- Euler's number: `e` (2.71828...)

For a complete list of all available functions, see [references/functions.md](references/functions.md).

## How to Use

1. Identify the mathematical operation the user wants to perform
2. Format the expression as a valid mathematical expression
3. Run the calculation script with the expression as an argument
4. Return the result to the user

### Running the Script
```bash
python scripts/calculate.py "expression"
```

## Quick Examples

### Basic Calculation
```bash
python scripts/calculate.py "125 + 237"
# Result: 362
```

### Complex Expression
```bash
python scripts/calculate.py "2**10 / 4"
# Result: 256.0
```

For more detailed examples across different domains, see [references/examples.md](references/examples.md).

## Additional Resources

- **[references/REFERENCE.md](references/REFERENCE.md)** - Complete technical reference and implementation details
- **[references/functions.md](references/functions.md)** - Full list of supported mathematical functions
- **[references/examples.md](references/examples.md)** - Domain-specific calculation examples

## Edge Cases and Error Handling

The script handles common mathematical errors:
- **Division by zero:** Returns an error message
- **Invalid expressions:** Reports syntax errors clearly
- **Undefined operations:** Catches mathematical domain errors
- **Invalid input:** Validates the expression before evaluation

## Safety

The script uses Python's restricted `eval()` to safely evaluate mathematical expressions without executing arbitrary code. Only mathematical operations are allowed.