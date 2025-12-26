#!/usr/bin/env python3
"""
Calculator Script for Agent Skills
Safely evaluates mathematical expressions.
"""

import sys
import math
import re
from typing import Union

def safe_eval(expression: str) -> Union[float, int]:
    """
    Safely evaluate a mathematical expression.
    
    Args:
        expression: A string containing a mathematical expression
        
    Returns:
        The calculated result
        
    Raises:
        ValueError: If the expression is invalid or unsafe
        ZeroDivisionError: If division by zero is attempted
    """
    # Remove whitespace
    expression = expression.strip()
    
    if not expression:
        raise ValueError("Empty expression provided")
    
    # Define allowed names (functions and constants)
    allowed_names = {
        # Math functions
        'abs': abs,
        'round': round,
        'min': min,
        'max': max,
        'sum': sum,
        'pow': pow,
        # Math module functions
        'sqrt': math.sqrt,
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'asin': math.asin,
        'acos': math.acos,
        'atan': math.atan,
        'sinh': math.sinh,
        'cosh': math.cosh,
        'tanh': math.tanh,
        'log': math.log,
        'log10': math.log10,
        'log2': math.log2,
        'exp': math.exp,
        'floor': math.floor,
        'ceil': math.ceil,
        'radians': math.radians,
        'degrees': math.degrees,
        'factorial': math.factorial,
        # Constants
        'pi': math.pi,
        'e': math.e,
        'tau': math.tau,
    }
    
    # Check for disallowed characters/patterns
    disallowed_patterns = [
        r'__',  # Double underscore (access to private attributes)
        r'import',  # Import statements
        r'exec',  # Code execution
        r'eval',  # Eval function
        r'open',  # File operations
        r'input',  # User input
    ]
    
    for pattern in disallowed_patterns:
        if re.search(pattern, expression, re.IGNORECASE):
            raise ValueError(f"Disallowed pattern detected: {pattern}")
    
    try:
        # Evaluate the expression with allowed names only
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return result
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero is not allowed")
    except SyntaxError as e:
        raise ValueError(f"Invalid syntax in expression: {e}")
    except NameError as e:
        raise ValueError(f"Unknown function or variable: {e}")
    except Exception as e:
        raise ValueError(f"Error evaluating expression: {e}")

def main():
    """Main entry point for the calculator script."""
    if len(sys.argv) < 2:
        print("Error: No expression provided", file=sys.stderr)
        print("Usage: python calculate.py \"expression\"", file=sys.stderr)
        print("Example: python calculate.py \"2 + 2\"", file=sys.stderr)
        sys.exit(1)
    
    expression = sys.argv[1]
    
    try:
        result = safe_eval(expression)
        
        # Format the result nicely
        if isinstance(result, float):
            # Remove unnecessary decimal places
            if result.is_integer():
                result = int(result)
            else:
                # Round to reasonable precision
                result = round(result, 10)
        
        print(f"Result: {result}")
        sys.exit(0)
        
    except ZeroDivisionError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()