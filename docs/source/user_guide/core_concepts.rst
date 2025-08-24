Core Concepts
=============

This section covers the fundamental mathematical objects provided by Eternal Math.

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
