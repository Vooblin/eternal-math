# Eternal Math

An open-source software platform designed as a comprehensive, ever-evolving toolkit for exploring, proving, and generating mathematical concepts.

## Overview

Eternal Math provides a Python-based framework for mathematical computation, theorem proving, and concept exploration. The platform combines computational tools with formal proof systems to create an integrated environment for mathematical research and education.

## Features

### Core Mathematical Objects
- **Set Theory**: Mathematical sets with standard operations (union, intersection, difference)
- **Function Theory**: Mathematical functions with composition and evaluation
- **Number Theory**: Prime numbers, GCD/LCM, factorization algorithms

### Proof System
- **Formal Proofs**: Structured proof representation with axioms, theorems, and proof steps
- **Theorem Management**: Create, verify, and organize mathematical theorems
- **Logical Framework**: Support for direct proofs, proof by contradiction, and more

### Number Theory Toolkit
- **Prime Generation**: Sieve of Eratosthenes for efficient prime computation
- **Sequences**: Fibonacci numbers, perfect numbers, Collatz sequences
- **Conjectures**: Goldbach conjecture verification, twin prime detection
- **Advanced Tools**: Euler's totient function, Chinese Remainder Theorem

## Installation

```bash
# Clone the repository
git clone https://github.com/Vooblin/eternal-math.git
cd eternal-math

# Install dependencies
pip install -e .
```

## Quick Start

```python
from eternal_math import sieve_of_eratosthenes, fibonacci_sequence, twin_primes

# Generate prime numbers up to 50
primes = sieve_of_eratosthenes(50)
print(f"Primes: {primes}")

# Generate Fibonacci sequence
fib = fibonacci_sequence(10)
print(f"Fibonacci: {fib}")

# Find twin prime pairs
twins = twin_primes(30)
print(f"Twin primes: {twins}")
```

## Examples

Run the number theory exploration example:

```bash
python examples/number_theory_exploration.py
```

## Testing

Run the test suite:

```bash
python -m tests.test_core
python -m tests.test_number_theory
```

## Project Structure

```
eternal-math/
├── eternal_math/          # Main package
│   ├── core.py           # Core mathematical objects
│   ├── proofs.py         # Proof system and logic
│   └── number_theory.py  # Number theory utilities
├── tests/                # Test suite
├── examples/             # Usage examples
└── pyproject.toml       # Project configuration
```

## Contributing

This is an open-source project. Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## License

MIT License - see LICENSE file for details.
