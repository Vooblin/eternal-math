"""
Eternal Math - A comprehensive mathematical toolkit.

This package provides tools for exploring, proving, and generating
mathematical concepts.
"""

__version__ = "0.1.0"
__author__ = "Dmitrii Murygin"

# Import core functionality with explicit __all__ to avoid F403/F401 issues
from .benchmarks import *  # noqa: F403, F401
from .core import *  # noqa: F403, F401
from .linear_algebra import *  # noqa: F403, F401
from .number_theory import *  # noqa: F403, F401
from .proofs import *  # noqa: F403, F401
from .symbolic import *  # noqa: F403, F401
from .visualization import *  # noqa: F403, F401

# CLI is available but not imported by default to avoid unnecessary dependencies
# Import with: from eternal_math.cli import main

# Define what gets imported with "from eternal_math import *"
__all__ = [
    # Core objects and utilities
    "Constants",
    "constants",
    "MathematicalObject",
    "Set",
    "Function",
    "gcd",
    "lcm",
    "is_prime",
    "prime_factorization",
    # Number theory
    "sieve_of_eratosthenes",
    "fibonacci",
    "fibonacci_sequence",
    "is_perfect_number",
    "euler_totient",
    "collatz_sequence",
    "twin_primes",
    "verify_goldbach_conjecture",
    "NumberTheoryUtils",
    # Proof system
    "Statement",
    "Axiom",
    "Theorem",
    "Proof",
    "ProofStep",
    "DirectProof",
    "ProofByContradiction",
    "EqualityStatement",
    "InequalityStatement",
    "LogicalStatement",
    # Symbolic math
    "SymbolicMath",
    "CalculusUtils",
    "AlgebraUtils",
    "CONSTANTS",
    "FUNCTIONS",
    # Linear algebra
    "Vector",
    "MatrixOperations",
    "LinearAlgebra",
    # Visualization
    "MathVisualizer",
    # Benchmarking
    "BenchmarkResult",
    "PerformanceBenchmark",
    "run_performance_analysis",
]
