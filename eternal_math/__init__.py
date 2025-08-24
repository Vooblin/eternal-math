"""
Eternal Math - A comprehensive mathematical toolkit.

This package provides tools for exploring, proving, and generating mathematical concepts.
"""

__version__ = "0.1.0"
__author__ = "Dmitrii Murygin"

# Benchmarking utilities
from .benchmarks import BenchmarkResult, PerformanceBenchmark, run_performance_analysis
from .core import *
from .number_theory import *
from .proofs import *
from .symbolic import *
from .visualization import *

# CLI is available but not imported by default to avoid unnecessary dependencies
# Import with: from eternal_math.cli import main
