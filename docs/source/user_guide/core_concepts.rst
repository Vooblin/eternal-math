Core Concepts
=============

This section covers the fundamental mathematical objects provided by Eternal Math.

Mathematical Constants
----------------------

Eternal Math provides access to fundamental mathematical constants through the ``constants`` object:

.. code-block:: python

    from eternal_math import constants

    # Basic constants
    print(f"π = {constants.PI}")      # 3.141592653589793
    print(f"e = {constants.E}")       # 2.718281828459045
    print(f"τ = {constants.TAU}")     # 6.283185307179586 (2π)

    # Golden ratio and related constants
    print(f"φ = {constants.PHI}")           # 1.618033988749895
    print(f"1/φ = {constants.PHI_INVERSE}") # 0.618033988749895

    # Square roots and logarithms
    print(f"√2 = {constants.SQRT_2}")   # 1.4142135623730951
    print(f"√3 = {constants.SQRT_3}")   # 1.7320508075688772
    print(f"ln(2) = {constants.LN_2}")  # 0.6931471805599453

    # Special constants
    print(f"γ = {constants.GAMMA}")     # 0.5772156649015329 (Euler-Mascheroni)

Available constants include:

* **PI** - The ratio of circumference to diameter (π)
* **E** - The base of natural logarithm (e)
* **TAU** - Twice pi, the ratio of circumference to radius (τ = 2π)
* **PHI** - The golden ratio ((1 + √5)/2)
* **PHI_INVERSE** - The reciprocal of the golden ratio
* **GAMMA** - The Euler-Mascheroni constant
* **SQRT_2, SQRT_3, SQRT_5** - Common square roots
* **LN_2, LN_10** - Natural logarithms of 2 and 10
* **INFINITY, NEG_INFINITY** - Positive and negative infinity

Mathematical Sets
-----------------

The ``Set`` class provides a mathematical set implementation with standard operations.

.. code-block:: python

    from eternal_math.core import Set

    # Create sets
    set_a = Set([1, 2, 3, 4, 5])
    set_b = Set([4, 5, 6, 7, 8])

    # Set operations
    union = set_a.union(set_b)  # {1, 2, 3, 4, 5, 6, 7, 8}
    intersection = set_a.intersection(set_b)  # {4, 5}
    difference = set_a.difference(set_b)  # {1, 2, 3}

Mathematical Functions
----------------------

The ``Function`` class represents mathematical functions with composition capabilities.

.. code-block:: python

    from eternal_math.core import Function

    # Define functions
    f = Function(lambda x: x**2 + 2*x + 1)
    g = Function(lambda x: 2*x + 3)

    # Function evaluation
    result = f.evaluate(3)  # 16

    # Function composition
    composed = f.compose(g)  # f(g(x))
    composition_result = composed.evaluate(2)  # f(g(2)) = f(7) = 64

Basic Number Theory
-------------------

Core number theory functions for common operations:

.. code-block:: python

    from eternal_math.core import gcd, lcm, is_prime, factorize

    # Greatest common divisor and least common multiple
    print(gcd(48, 18))  # 6
    print(lcm(48, 18))  # 144

    # Prime checking
    print(is_prime(17))  # True
    print(is_prime(15))  # False

    # Prime factorization
    print(factorize(60))  # [2, 2, 3, 5]
