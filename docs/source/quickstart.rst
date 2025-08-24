Quick Start
===========

This guide will help you get started with Eternal Math quickly.

Basic Usage
-----------

First, import the main modules:

.. code-block:: python

    from eternal_math import core, number_theory, symbolic, visualization

Core Mathematical Objects
--------------------------

Working with sets:

.. code-block:: python

    from eternal_math.core import Set

    # Create sets
    set_a = Set([1, 2, 3, 4, 5])
    set_b = Set([4, 5, 6, 7, 8])

    # Set operations
    union = set_a.union(set_b)
    intersection = set_a.intersection(set_b)
    print(f"Union: {union}")
    print(f"Intersection: {intersection}")

Working with functions:

.. code-block:: python

    from eternal_math.core import Function

    # Create a mathematical function
    f = Function(lambda x: x**2 + 2*x + 1)

    # Evaluate the function
    result = f.evaluate(3)  # Returns 16
    print(f"f(3) = {result}")

Number Theory
-------------

Generate prime numbers:

.. code-block:: python

    from eternal_math.number_theory import sieve_of_eratosthenes

    # Generate primes up to 30
    primes = sieve_of_eratosthenes(30)
    print(f"Primes up to 30: {primes}")

Calculate Fibonacci sequence:

.. code-block:: python

    from eternal_math.number_theory import fibonacci_sequence

    # Get first 10 Fibonacci numbers
    fib = fibonacci_sequence(10)
    print(f"First 10 Fibonacci numbers: {fib}")

Symbolic Mathematics
--------------------

Basic symbolic operations:

.. code-block:: python

    from eternal_math.symbolic import SymbolicMath

    # Create symbolic math instance
    sym = SymbolicMath()

    # Create symbols
    x, y = sym.create_symbols('x y')

    # Create and manipulate expressions
    expr = x**2 + 2*x + 1
    expanded = sym.expand((x + 1)**2)
    factored = sym.factor(x**2 - 1)

    print(f"Expression: {expr}")
    print(f"Expanded (x+1)²: {expanded}")
    print(f"Factored x²-1: {factored}")

Solve equations:

.. code-block:: python

    # Solve quadratic equation
    solutions = sym.solve(x**2 - 4, x)
    print(f"Solutions to x² - 4 = 0: {solutions}")

Visualization
-------------

Plot mathematical functions:

.. code-block:: python

    from eternal_math.visualization import MathVisualizer

    # Create visualizer
    viz = MathVisualizer()

    # Plot a function
    viz.plot_function("x**2 + 2*x + 1", x_range=(-5, 3))

    # Plot Fibonacci sequence
    viz.plot_sequence([1, 1, 2, 3, 5, 8, 13, 21], "Fibonacci Sequence")

Command Line Interface
----------------------

Eternal Math includes a powerful CLI for interactive exploration:

.. code-block:: bash

    # Start interactive session
    eternal-math

    # Generate prime numbers
    eternal-math> primes 50

    # Calculate Fibonacci numbers
    eternal-math> fibonacci 10

    # Solve symbolic equations
    eternal-math> solve "x**2 - 4"

    # Plot functions
    eternal-math> plot_function "sin(x)" -5 5

Example Session
---------------

Here's a complete example combining multiple features:

.. code-block:: python

    from eternal_math import number_theory, symbolic, visualization

    # 1. Number theory: Find perfect numbers
    perfect_nums = number_theory.find_perfect_numbers(30)
    print(f"Perfect numbers up to 30: {perfect_nums}")

    # 2. Symbolic math: Work with polynomials
    sym = symbolic.SymbolicMath()
    x = sym.create_symbol('x')
    poly = x**3 - 6*x**2 + 11*x - 6
    factored = sym.factor(poly)
    roots = sym.solve(poly, x)
    print(f"Polynomial: {poly}")
    print(f"Factored form: {factored}")
    print(f"Roots: {roots}")

    # 3. Visualization: Plot the polynomial
    viz = visualization.MathVisualizer()
    viz.plot_function("x**3 - 6*x**2 + 11*x - 6", x_range=(0, 4))

Next Steps
----------

* Explore the :doc:`examples` for more detailed use cases
* Check the API reference for complete documentation
* Read the user guides for in-depth coverage of each module
* Try the interactive examples in the ``examples/`` directory
