"""
Number theory utilities and theorems.
"""

from typing import List, Tuple

from .core import gcd, prime_factorization
from .proofs import Axiom, LogicalStatement, Proof, ProofStep, Theorem


def sieve_of_eratosthenes(limit: int) -> List[int]:
    """
    Generate all prime numbers up to a given limit using the Sieve of Eratosthenes.

    For limits > 1,000,000, automatically uses segmented sieve for better memory
     efficiency.
    """
    if limit < 2:
        return []

    # Use segmented sieve for large limits for better memory efficiency
    if limit > 1_000_000:
        return _segmented_sieve(limit)

    # Standard sieve for smaller limits
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    return [i for i in range(2, limit + 1) if sieve[i]]


def _segmented_sieve(limit: int) -> List[int]:
    """
    Segmented Sieve of Eratosthenes for memory-efficient prime generation.
    Uses O(sqrt(n)) memory instead of O(n).
    """
    import math

    sqrt_limit = int(math.sqrt(limit))

    # Generate primes up to sqrt(limit) using standard sieve
    base_primes = []
    if sqrt_limit >= 2:
        sieve = [True] * (sqrt_limit + 1)
        sieve[0] = sieve[1] = False

        for i in range(2, int(sqrt_limit**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, sqrt_limit + 1, i):
                    sieve[j] = False

        base_primes = [i for i in range(2, sqrt_limit + 1) if sieve[i]]

    # Process segments
    segment_size = max(sqrt_limit, 32768)  # At least 32KB segments
    primes = base_primes[:]

    for segment_start in range(sqrt_limit + 1, limit + 1, segment_size):
        segment_end = min(segment_start + segment_size - 1, limit)
        segment = [True] * (segment_end - segment_start + 1)

        for prime in base_primes:
            # Find first multiple of prime in this segment
            start = max(prime * prime, (segment_start + prime - 1) // prime * prime)

            for multiple in range(start, segment_end + 1, prime):
                segment[multiple - segment_start] = False

        # Collect primes from this segment
        for i in range(len(segment)):
            if segment[i]:
                candidate = segment_start + i
                if candidate > sqrt_limit:  # Avoid duplicates
                    primes.append(candidate)

    return primes


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
        sequence.append(sequence[i - 1] + sequence[i - 2])

    return sequence


def is_perfect_number(n: int) -> bool:
    """
    Check if a number is a perfect number (sum of proper divisors equals the number).
    Optimized algorithm with early termination.
    """
    if n <= 1:
        return False

    # Even perfect numbers are of the form 2^(p-1) * (2^p - 1) where 2^p - 1 is prime
    # This optimization handles Mersenne-based perfect numbers efficiently
    if n % 2 == 0:
        # Check if n = 2^(p-1) * (2^p - 1) for some prime p
        temp = n
        power_of_2 = 0
        while temp % 2 == 0:
            temp //= 2
            power_of_2 += 1

        if power_of_2 > 0:
            mersenne_candidate = temp
            expected_mersenne = (1 << (power_of_2 + 1)) - 1

            if mersenne_candidate == expected_mersenne and _is_prime(
                mersenne_candidate
            ):
                return True

    # General case with optimized divisor sum calculation
    divisor_sum = 1  # 1 is always a proper divisor
    sqrt_n = int(n**0.5)

    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            divisor_sum += i
            complement = n // i
            if i != complement:  # Avoid double-counting perfect squares
                divisor_sum += complement

            # Early termination if sum already exceeds n
            if divisor_sum > n:
                return False

    return divisor_sum == n


def _is_prime(n: int) -> bool:
    """Fast primality test for moderate-sized numbers."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def euler_totient(n: int) -> int:
    """
    Calculate Euler's totient function φ(n) - count of integers up to n
    that are coprime to n.
    """
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
    """
    Find all twin prime pairs (p, p+2) where both are prime, up to the given limit.
    """
    primes = sieve_of_eratosthenes(limit)
    prime_set = set(primes)

    twin_pairs = []
    for p in primes:
        if p + 2 in prime_set:
            twin_pairs.append((p, p + 2))

    return twin_pairs


# Number theory theorems
def create_fundamental_theorem_of_arithmetic() -> Theorem:
    """
    Create the Fundamental Theorem of Arithmetic as a theorem object with
    detailed proof steps.
    """
    description = (
        "Every integer greater than 1 either is prime itself "
        "or is the product of prime numbers, and this product is unique "
        "up to the order of factors."
    )

    theorem = Theorem(description)

    # Create a comprehensive proof structure
    proof = Proof(theorem)

    # Add foundational axioms
    axiom1 = Axiom("Every integer n > 1 has a smallest divisor d > 1")
    axiom2 = Axiom("If d is the smallest divisor of n > 1, then d is prime")
    axiom3 = Axiom(
        "If n = p1^a1 * p2^a2 * ... * pk^ak and n = q1^b1 * q2^b2 * ... * qm^bm "
        "where all p_i and q_j are prime, then k = m and the multisets "
        "{p1, p2, ..., pk} and {q1, q2, ..., qm} are identical"
    )

    proof.add_axiom(axiom1)
    proof.add_axiom(axiom2)
    proof.add_axiom(axiom3)

    # Create statements for proof steps
    existence_stmt = LogicalStatement(
        "Every integer n > 1 can be expressed as a product of primes"
    )
    uniqueness_stmt = LogicalStatement(
        "The prime factorization of any integer n > 1 is unique up to order"
    )

    # Proof steps for existence (by strong induction)
    step1 = ProofStep(
        premises=[axiom1],
        conclusion=LogicalStatement(
            "Let n > 1 be arbitrary. Either n is prime or n has a proper divisor"
        ),
        rule="Case Analysis",
        justification=(
            "By definition, n is prime if it has no proper divisors, "
            "otherwise it has proper divisors"
        ),
    )

    step2 = ProofStep(
        premises=[step1.conclusion, axiom2],
        conclusion=LogicalStatement(
            "If n is composite, then n = d * (n/d) where d is the smallest "
            "prime divisor of n"
        ),
        rule="Division Property",
        justification=(
            "If n has a proper divisor d, then n/d is also a divisor, "
            "and the smallest such d must be prime"
        ),
    )

    step3 = ProofStep(
        premises=[step2.conclusion],
        conclusion=LogicalStatement(
            "By strong induction, both d and n/d can be expressed as "
            "products of primes"
        ),
        rule="Strong Induction",
        justification=(
            "Since d < n and n/d < n, by inductive hypothesis both have "
            "prime factorizations"
        ),
    )

    step4 = ProofStep(
        premises=[step1.conclusion, step3.conclusion],
        conclusion=existence_stmt,
        rule="Inductive Construction",
        justification=(
            "Base case: primes factor as themselves. Inductive step: "
            "composite n = d * (n/d) where both factors have prime factorizations"
        ),
    )

    # Proof steps for uniqueness (by contradiction)
    step5 = ProofStep(
        premises=[existence_stmt],
        conclusion=LogicalStatement(
            "Assume n has two different prime factorizations: "
            "n = p1 * p2 * ... * pk = q1 * q2 * ... * qm"
        ),
        rule="Proof by Contradiction Setup",
        justification=(
            "To prove uniqueness, assume the contrary and derive a contradiction"
        ),
    )

    step6 = ProofStep(
        premises=[step5.conclusion],
        conclusion=LogicalStatement(
            "Since p1 divides the left side, p1 must divide some q_j "
            "on the right side"
        ),
        rule="Divisibility Property",
        justification=(
            "If a prime divides a product, it must divide at least one factor"
        ),
    )

    step7 = ProofStep(
        premises=[step6.conclusion],
        conclusion=LogicalStatement(
            "Since p1 and q_j are both prime and p1 divides q_j, we have p1 = q_j"
        ),
        rule="Prime Property",
        justification=(
            "A prime number has no proper divisors, so if one prime divides "
            "another, they must be equal"
        ),
    )

    step8 = ProofStep(
        premises=[step7.conclusion],
        conclusion=uniqueness_stmt,
        rule="Inductive Cancellation",
        justification=(
            "Cancel equal primes from both sides and repeat the argument "
            "until both factorizations are shown to be identical"
        ),
    )

    step9 = ProofStep(
        premises=[existence_stmt, uniqueness_stmt],
        conclusion=LogicalStatement(description),
        rule="Conjunction",
        justification=(
            "The Fundamental Theorem follows from both existence and uniqueness "
            "of prime factorization"
        ),
    )

    # Add all proof steps
    proof.add_step(step1)
    proof.add_step(step2)
    proof.add_step(step3)
    proof.add_step(step4)
    proof.add_step(step5)
    proof.add_step(step6)
    proof.add_step(step7)
    proof.add_step(step8)
    proof.add_step(step9)

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
    "sieve_of_eratosthenes",
    "fibonacci",
    "fibonacci_sequence",
    "is_perfect_number",
    "euler_totient",
    "collatz_sequence",
    "twin_primes",
    "create_fundamental_theorem_of_arithmetic",
    "verify_goldbach_conjecture",
    "NumberTheoryUtils",
]
