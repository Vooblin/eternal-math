# Development Guide

This guide provides information for developers working on the Eternal Math project.

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/Vooblin/eternal-math.git
cd eternal-math
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install development dependencies:
```bash
pip install -e '.[dev]'
```

## Code Quality Standards

### Type Checking
This project uses comprehensive type hints throughout the codebase. We use mypy for static type checking.

Run type checking:
```bash
mypy eternal_math/ tests/ examples/
```

### Code Formatting
We use Black for code formatting and isort for import sorting:

```bash
# Format code
black eternal_math/ tests/ examples/

# Sort imports
isort eternal_math/ tests/ examples/

# Check formatting (without modifying files)
black --check eternal_math/ tests/ examples/
```

### Linting
We use flake8 for linting:
```bash
flake8 eternal_math/ tests/ examples/
```

### Running All Quality Checks
```bash
# Run all quality checks
make lint  # if Makefile exists, or run commands individually:
black --check eternal_math/ tests/ examples/
isort --check-only eternal_math/ tests/ examples/
flake8 eternal_math/ tests/ examples/
mypy eternal_math/ tests/ examples/
pytest tests/
```

## Type Hints Guidelines

### Function Annotations
All functions must have complete type annotations:

```python
from typing import List, Optional, Dict, Any, Union

def process_data(items: List[int], threshold: Optional[float] = None) -> Dict[str, Any]:
    """Process a list of items with optional threshold."""
    pass
```

### Class Methods
Class methods should include type annotations for parameters and return values:

```python
class MathProcessor:
    def __init__(self, config: Dict[str, Any]) -> None:
        self.config = config
    
    def compute(self, value: float) -> Optional[float]:
        """Compute processed value."""
        pass
```

### Generic Types
Use appropriate generic types for containers:

```python
from typing import List, Dict, Tuple, Optional, Union

# Good
def process_pairs(pairs: List[Tuple[int, str]]) -> Dict[int, List[str]]:
    pass

# Avoid untyped containers
def process_pairs(pairs):  # Missing type hints
    pass
```

## Testing

Run tests with coverage:
```bash
pytest tests/ -v --cov=eternal_math --cov-report=html
```

## Documentation

### Docstring Format
Use Google-style docstrings with type information:

```python
def calculate_prime_density(limit: int, primes: List[int]) -> float:
    """Calculate the density of prime numbers up to a given limit.
    
    Args:
        limit: The upper bound for calculation
        primes: List of prime numbers up to the limit
        
    Returns:
        The density as a float between 0 and 1
        
    Raises:
        ValueError: If limit is less than 2
        
    Example:
        >>> primes = sieve_of_eratosthenes(100)
        >>> density = calculate_prime_density(100, primes)
        >>> print(f"Prime density: {density:.3f}")
    """
    if limit < 2:
        raise ValueError("Limit must be at least 2")
    return len(primes) / limit
```

## Project Structure

The project follows a modular structure:

```
eternal_math/
├── __init__.py          # Package initialization and exports
├── core.py             # Core mathematical objects and utilities
├── number_theory.py    # Number theory algorithms and theorems
├── symbolic.py         # Symbolic mathematics with SymPy
├── proofs.py          # Formal proof system
├── visualization.py   # Mathematical plotting and graphics
├── benchmarks.py      # Performance benchmarking system
├── cli.py             # Interactive command-line interface
└── py.typed           # Marks package as typed for mypy
```

## Contributing Workflow

1. Create a feature branch from `main`
2. Make your changes with proper type hints and documentation
3. Run all quality checks locally
4. Write tests for new functionality
5. Update documentation as needed
6. Create a pull request

## CI/CD Pipeline

The project uses GitHub Actions for:
- Running tests on Python 3.12
- Type checking with mypy
- Code coverage reporting
- Building and publishing packages

## Performance Considerations

When adding new features:
1. Consider algorithmic complexity
2. Use appropriate data structures
3. Add benchmarks for performance-critical code
4. Profile code if performance issues are suspected

## Adding New Mathematical Concepts

When adding new mathematical functionality:

1. **Core Module**: Add basic mathematical objects and utilities
2. **Specialized Modules**: Add domain-specific algorithms
3. **Proofs**: Include formal representations when applicable
4. **Visualization**: Add plotting capabilities for new concepts
5. **CLI Integration**: Add interactive commands
6. **Examples**: Create demonstration scripts
7. **Tests**: Write comprehensive test coverage
8. **Documentation**: Update README and add docstrings

## Dependencies

### Runtime Dependencies
- `numpy`: Numerical computing
- `sympy`: Symbolic mathematics
- `matplotlib`: Plotting and visualization

### Development Dependencies
- `pytest`: Testing framework
- `pytest-cov`: Coverage reporting
- `black`: Code formatting
- `isort`: Import sorting
- `flake8`: Linting
- `mypy`: Static type checking

## Release Process

1. Update version in `pyproject.toml` and `__init__.py`
2. Update `CHANGELOG.md` with new features and changes
3. Create a git tag with the version number
4. GitHub Actions will automatically build and publish to PyPI
