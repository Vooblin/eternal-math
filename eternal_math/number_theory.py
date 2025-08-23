"""
Number theory utilities and theorems.
"""

from typing import List, Iterator, Tuple
from .core import is_prime, prime_factorization, gcd
from .proofs import Theorem, Axiom, Proof, EqualityStatement


def sieve_of_eratosthenes(limit: int) -> List[int]:
    """Generate all prime numbers up to a given limit using the Sieve of Eratosthenes."""
    if limit < 2:
        return []
    
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    
    return [i for i in range(2, limit + 1) if sieve[i]]


def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number (0-indexed)."""
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_sequence(count: int) -> List[int]:
    """Generate the first 'count' Fibonacci numbers."""
    if count <= 0:
        return []
    elif count == 1:
        return [0]
    elif count == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, count):
        sequence.append(sequence[i-1] + sequence[i-2])
    
    return sequence


def is_perfect_number(n: int) -> bool:
    """Check if a number is a perfect number (sum of proper divisors equals the number)."""
    if n <= 1:
        return False
    
    divisor_sum = 1  # 1 is always a proper divisor
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:  # Avoid double-counting square roots
                divisor_sum += n // i
    
    return divisor_sum == n


def euler_totient(n: int) -> int:
    """Calculate Euler's totient function φ(n) - count of integers up to n that are coprime to n."""
    if n == 1:
        return 1
    
    result = n
    factors = set(prime_factorization(n))
    
    for p in factors:
        result = result * (p - 1) // p
    
    return result


def collatz_sequence(n: int) -> List[int]:
    """Generate the Collatz sequence starting from n until reaching 1."""
    if n <= 0:
        return []
    
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    
    return sequence


def twin_primes(limit: int) -> List[Tuple[int, int]]:
    """Find all twin prime pairs (p, p+2) where both are prime, up to the given limit."""
    primes = sieve_of_eratosthenes(limit)
    prime_set = set(primes)
    
    twin_pairs = []
    for p in primes:
        if p + 2 in prime_set:
            twin_pairs.append((p, p + 2))
    
    return twin_pairs


# Number theory theorems
def create_fundamental_theorem_of_arithmetic() -> Theorem:
    """Create the Fundamental Theorem of Arithmetic as a theorem object."""
    description = ("Every integer greater than 1 either is prime itself "
                  "or is the product of prime numbers, and this product is unique "
                  "up to the order of factors.")
    
    theorem = Theorem(description)
    
    # Create a simple proof structure (conceptual)
    proof = Proof(theorem)
    
    # Add axioms (simplified)
    proof.add_axiom(Axiom("Every integer n > 1 has a smallest divisor d > 1"))
    proof.add_axiom(Axiom("If d is the smallest divisor of n > 1, then d is prime"))
    proof.add_axiom(Axiom("Prime factorization can be computed recursively"))
    
    theorem.proof = proof
    theorem.proven = True
    
    return theorem


def verify_goldbach_conjecture(limit: int) -> bool:
    """Verify Goldbach's conjecture for all even numbers up to the given limit."""
    primes = set(sieve_of_eratosthenes(limit))
    
    for n in range(4, limit + 1, 2):  # Check all even numbers >= 4
        found_pair = False
        for p in primes:
            if p > n // 2:
                break
            if (n - p) in primes:
                found_pair = True
                break
        
        if not found_pair:
            return False
    
    return True


class NumberTheoryUtils:
    """Utility class for number theory operations."""
    
    @staticmethod
    def chinese_remainder_theorem(remainders: List[int], moduli: List[int]) -> int:
        """
        Solve system of congruences using Chinese Remainder Theorem.
        Returns x such that x ≡ remainders[i] (mod moduli[i]) for all i.
        """
        if len(remainders) != len(moduli):
            raise ValueError("Remainders and moduli must have the same length")
        
        # Check that moduli are pairwise coprime
        for i in range(len(moduli)):
            for j in range(i + 1, len(moduli)):
                if gcd(moduli[i], moduli[j]) != 1:
                    raise ValueError("Moduli must be pairwise coprime")
        
        total = 0
        prod = 1
        for m in moduli:
            prod *= m
        
        for r, m in zip(remainders, moduli):
            p = prod // m
            total += r * p * pow(p, -1, m)
        
        return total % prod


__all__ = [
    'sieve_of_eratosthenes', 'fibonacci', 'fibonacci_sequence',
    'is_perfect_number', 'euler_totient', 'collatz_sequence', 'twin_primes',
    'create_fundamental_theorem_of_arithmetic', 'verify_goldbach_conjecture',
    'NumberTheoryUtils'
]
