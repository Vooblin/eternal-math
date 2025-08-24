"""
Core mathematical utilities and data structures for Eternal Math.
"""

import math
from typing import Any, Callable, List, Optional


# Mathematical Constants
class Constants:
    """Container for fundamental mathematical constants."""

    # Basic constants
    PI = math.pi
    E = math.e
    TAU = 2 * math.pi  # τ = 2π

    # Golden ratio and related constants
    PHI = (1 + math.sqrt(5)) / 2  # Golden ratio φ = (1 + √5)/2
    PHI_INVERSE = 2 / (1 + math.sqrt(5))  # 1/φ = (√5 - 1)/2

    # Euler-Mascheroni constant (approximation)
    GAMMA = 0.5772156649015329

    # Mathematical ratios
    SQRT_2 = math.sqrt(2)
    SQRT_3 = math.sqrt(3)
    SQRT_5 = math.sqrt(5)

    # Natural logarithms of common values
    LN_2 = math.log(2)
    LN_10 = math.log(10)

    # Common mathematical limits
    INFINITY = float("inf")
    NEG_INFINITY = float("-inf")


# Create global constants instance for easy access
constants = Constants()


class MathematicalObject:
    """Base class for all mathematical objects in the system."""

    def __init__(self, name: Optional[str] = None):
        self.name = name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name or 'unnamed'})"


class Set(MathematicalObject):
    """Mathematical set implementation."""

    def __init__(
        self, elements: Optional[List[Any]] = None, name: Optional[str] = None
    ):
        super().__init__(name)
        if elements is not None and not isinstance(elements, list):
            raise TypeError("Elements must be a list")
        self.elements = list(set(elements or []))

    def __contains__(self, item: Any) -> bool:
        return item in self.elements

    def __len__(self) -> int:
        return len(self.elements)

    def __iter__(self) -> Any:
        return iter(self.elements)

    def union(self, other: "Set") -> "Set":
        """
        Return the union of this set with another.

        Args:
            other: Another Set object

        Returns:
            New Set containing elements from both sets

        Raises:
            TypeError: If other is not a Set instance
        """
        if not isinstance(other, Set):
            raise TypeError("Argument must be a Set instance")
        return Set(self.elements + other.elements)

    def intersection(self, other: "Set") -> "Set":
        """
        Return the intersection of this set with another.

        Args:
            other: Another Set object

        Returns:
            New Set containing elements common to both sets

        Raises:
            TypeError: If other is not a Set instance
        """
        if not isinstance(other, Set):
            raise TypeError("Argument must be a Set instance")
        return Set([x for x in self.elements if x in other])

    def difference(self, other: "Set") -> "Set":
        """
        Return the difference of this set with another.

        Args:
            other: Another Set object

        Returns:
            New Set containing elements in this set but not in other

        Raises:
            TypeError: If other is not a Set instance
        """
        if not isinstance(other, Set):
            raise TypeError("Argument must be a Set instance")
        return Set([x for x in self.elements if x not in other])


class Function(MathematicalObject):
    """Mathematical function representation."""

    def __init__(
        self,
        func: Callable[..., Any],
        domain: Optional[Set] = None,
        codomain: Optional[Set] = None,
        name: Optional[str] = None,
    ):
        super().__init__(name)
        if not callable(func):
            raise TypeError("func must be callable")
        self.func = func
        self.domain = domain
        self.codomain = codomain

    def __call__(self, x: Any) -> Any:
        if self.domain and x not in self.domain:
            raise ValueError(f"{x} is not in the domain {self.domain}")
        return self.func(x)

    def compose(self, other: "Function") -> "Function":
        """
        Compose this function with another function.

        Args:
            other: Another Function object

        Returns:
            New Function representing the composition

        Raises:
            TypeError: If other is not a Function instance
        """
        if not isinstance(other, Function):
            raise TypeError("Argument must be a Function instance")

        return Function(
            lambda x: self(other(x)),
            other.domain,
            self.codomain,
            f"({self.name} ∘ {other.name})" if self.name and other.name else None,
        )


def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor of two integers using Euclidean algorithm.

    Args:
        a: First integer
        b: Second integer

    Returns:
        The greatest common divisor of a and b

    Raises:
        TypeError: If either argument is not an integer
        ValueError: If both arguments are zero
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers")

    if a == 0 and b == 0:
        raise ValueError("GCD is undefined when both arguments are zero")

    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a: int, b: int) -> int:
    """
    Calculate the least common multiple of two integers.

    Args:
        a: First integer
        b: Second integer

    Returns:
        The least common multiple of a and b

    Raises:
        TypeError: If either argument is not an integer
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers")

    return abs(a * b) // gcd(a, b) if a and b else 0


def is_prime(n: int) -> bool:
    """
    Check if a number is prime using trial division.

    Args:
        n: The number to check for primality

    Returns:
        True if n is prime, False otherwise

    Raises:
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Argument must be an integer")

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def prime_factorization(n: int) -> List[int]:
    """
    Return the prime factorization of a positive integer.

    Args:
        n: The positive integer to factorize

    Returns:
        List of prime factors in ascending order

    Raises:
        TypeError: If n is not an integer
        ValueError: If n is less than 2
    """
    if not isinstance(n, int):
        raise TypeError("Argument must be an integer")

    if n < 2:
        raise ValueError("Prime factorization is only defined for integers >= 2")

    factors: List[int] = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


__all__ = [
    "Constants",
    "constants",
    "MathematicalObject",
    "Set",
    "Function",
    "gcd",
    "lcm",
    "is_prime",
    "prime_factorization",
]
