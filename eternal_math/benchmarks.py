"""
Performance benchmarking utilities for eternal-math.

This module provides benchmarking tools to measure and analyze the performance
of mathematical algorithms implemented in eternal-math.
"""

import statistics
import time
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional

import matplotlib.pyplot as plt

from .core import gcd, is_prime
from .number_theory import (
    fibonacci_sequence,
    is_perfect_number,
    sieve_of_eratosthenes,
)


@dataclass
class BenchmarkResult:
    """Container for benchmark results."""

    function_name: str
    input_size: int
    execution_time: float
    iterations: int
    mean_time: float
    std_dev: float
    min_time: float
    max_time: float


class PerformanceBenchmark:
    """Performance benchmarking system for mathematical algorithms."""

    def __init__(self) -> None:
        """Initialize the benchmark system."""
        self.results: List[BenchmarkResult] = []

    def find_perfect_numbers(self, limit: int) -> List[int]:
        """Helper function to find perfect numbers up to a limit."""
        perfect_nums = []
        for i in range(1, limit + 1):
            if is_perfect_number(i):
                perfect_nums.append(i)
        return perfect_nums

    def time_function(
        self, func: Callable[..., Any], *args: Any, iterations: int = 10, **kwargs: Any
    ) -> BenchmarkResult:
        """
        Time a function execution with multiple iterations.

        Args:
            func: Function to benchmark
            *args: Arguments to pass to the function
            iterations: Number of iterations to run
            **kwargs: Keyword arguments to pass to the function

        Returns:
            BenchmarkResult containing timing statistics
        """
        times = []

        for _ in range(iterations):
            start_time = time.perf_counter()
            func(*args, **kwargs)  # Execute function without storing result
            end_time = time.perf_counter()
            times.append(end_time - start_time)

        # Determine input size for common patterns
        input_size = self._extract_input_size(args, kwargs)

        benchmark_result = BenchmarkResult(
            function_name=func.__name__,
            input_size=input_size,
            execution_time=sum(times),
            iterations=iterations,
            mean_time=statistics.mean(times),
            std_dev=statistics.stdev(times) if len(times) > 1 else 0.0,
            min_time=min(times),
            max_time=max(times),
        )

        self.results.append(benchmark_result)
        return benchmark_result

    def _extract_input_size(self, args: tuple, kwargs: dict) -> int:
        """Extract a representative input size from function arguments."""
        # For most number theory functions, the first argument is the size/limit
        if args:
            if isinstance(args[0], int):
                return args[0]
            elif hasattr(args[0], "__len__"):
                return len(args[0])

        # Check for common keyword arguments
        for key in ["n", "limit", "max_value", "size"]:
            if key in kwargs:
                return int(kwargs[key])

        return 0

    def benchmark_prime_algorithms(
        self, sizes: Optional[List[int]] = None
    ) -> Dict[str, List[BenchmarkResult]]:
        """
        Benchmark prime number algorithms across different input sizes.

        Args:
            sizes: List of input sizes to test

        Returns:
            Dictionary mapping algorithm names to their benchmark results
        """
        if sizes is None:
            sizes = [100, 500, 1000, 5000, 10000]

        results: Dict[str, List[BenchmarkResult]] = {
            "sieve_of_eratosthenes": [],
            "is_prime_checks": [],
        }

        # Benchmark Sieve of Eratosthenes
        for size in sizes:
            result = self.time_function(sieve_of_eratosthenes, size, iterations=5)
            results["sieve_of_eratosthenes"].append(result)
            print(
                f"Sieve of Eratosthenes (n={size}): "
                f"{result.mean_time:.4f}s ± {result.std_dev:.4f}s"
            )

        # Benchmark individual prime checks
        test_numbers = [97, 997, 9973, 99991, 999983]  # Known primes
        for num in test_numbers:
            result = self.time_function(is_prime, num, iterations=100)
            results["is_prime_checks"].append(result)
            print(
                f"Prime check (n={num}): "
                f"{result.mean_time:.6f}s ± {result.std_dev:.6f}s"
            )

        return results

    def benchmark_fibonacci_algorithms(
        self, sizes: Optional[List[int]] = None
    ) -> List[BenchmarkResult]:
        """
        Benchmark Fibonacci sequence generation.

        Args:
            sizes: List of sequence lengths to test

        Returns:
            List of benchmark results
        """
        if sizes is None:
            sizes = [10, 50, 100, 500, 1000]

        results = []

        for size in sizes:
            result = self.time_function(fibonacci_sequence, size, iterations=10)
            results.append(result)
            print(
                f"Fibonacci sequence (n={size}): "
                f"{result.mean_time:.4f}s ± {result.std_dev:.4f}s"
            )

        return results

    def benchmark_number_theory_suite(self) -> Dict[str, List[BenchmarkResult]]:
        """
        Run a comprehensive benchmark suite for number theory algorithms.

        Returns:
            Dictionary of benchmark results organized by algorithm type
        """
        print("=== Number Theory Performance Benchmark Suite ===\n")

        results = {}

        # Prime algorithms
        print("1. Prime Number Algorithms:")
        results.update(self.benchmark_prime_algorithms())
        print()

        # Fibonacci
        print("2. Fibonacci Sequence:")
        results["fibonacci"] = self.benchmark_fibonacci_algorithms()
        print()

        # Perfect numbers (smaller sizes due to computational complexity)
        print("3. Perfect Numbers:")
        perfect_sizes = [100, 500, 1000]
        perfect_results = []
        for size in perfect_sizes:
            result = self.time_function(self.find_perfect_numbers, size, iterations=3)
            perfect_results.append(result)
            print(
                f"Perfect numbers (limit={size}): "
                f"{result.mean_time:.4f}s ± {result.std_dev:.4f}s"
            )
        results["perfect_numbers"] = perfect_results
        print()

        # GCD performance
        print("4. GCD Algorithm:")
        gcd_pairs = [(48, 18), (1071, 462), (12345, 54321), (999999, 123456)]
        gcd_results = []
        for a, b in gcd_pairs:
            result = self.time_function(gcd, a, b, iterations=1000)
            gcd_results.append(result)
            print(f"GCD({a}, {b}): {result.mean_time:.6f}s ± {result.std_dev:.6f}s")
        results["gcd"] = gcd_results
        print()

        return results

    def plot_performance_comparison(
        self,
        results: Dict[str, List[BenchmarkResult]],
        title: str = "Performance Comparison",
    ) -> None:
        """
        Create performance comparison plots.

        Args:
            results: Dictionary of benchmark results
            title: Plot title
        """
        plt.figure(figsize=(12, 8))

        for algorithm, benchmark_list in results.items():
            if not benchmark_list:
                continue

            input_sizes = [r.input_size for r in benchmark_list if r.input_size > 0]
            mean_times = [r.mean_time for r in benchmark_list if r.input_size > 0]

            if input_sizes and mean_times:
                plt.loglog(
                    input_sizes,
                    mean_times,
                    "o-",
                    label=algorithm,
                    linewidth=2,
                    markersize=6,
                )

        plt.xlabel("Input Size")
        plt.ylabel("Execution Time (seconds)")
        plt.title(title)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()

        # Save the plot
        plot_filename = f"benchmark_{title.lower().replace(' ', '_')}.png"
        plt.savefig(f"math_plots/{plot_filename}", dpi=300, bbox_inches="tight")
        print(f"Performance plot saved as: math_plots/{plot_filename}")

        plt.show()

    def generate_performance_report(self) -> str:
        """
        Generate a detailed performance report.

        Returns:
            Formatted performance report as string
        """
        if not self.results:
            return "No benchmark results available."

        report = ["=== Eternal Math Performance Report ===\n"]

        # Group results by function
        by_function: Dict[str, List[BenchmarkResult]] = {}
        for result in self.results:
            if result.function_name not in by_function:
                by_function[result.function_name] = []
            by_function[result.function_name].append(result)

        for func_name, func_results in by_function.items():
            report.append(f"Function: {func_name}")
            report.append("-" * 40)

            for result in func_results:
                if result.input_size > 0:
                    report.append(f"  Input Size: {result.input_size}")
                report.append(f"  Mean Time: {result.mean_time:.6f}s")
                report.append(f"  Std Dev: {result.std_dev:.6f}s")
                report.append(
                    f"  Min/Max: {result.min_time:.6f}s / {result.max_time:.6f}s"
                )
                report.append(f"  Iterations: {result.iterations}")
                report.append("")

            report.append("")

        return "\n".join(report)

    def save_results(self, filename: str) -> None:
        """
        Save benchmark results to a file.

        Args:
            filename: Output filename
        """
        report = self.generate_performance_report()

        with open(filename, "w") as f:
            f.write(report)

        print(f"Benchmark results saved to: {filename}")

    def benchmark_algorithm_comparison(self, limit: int = 100_000) -> Dict[str, Any]:
        """
        Benchmark comparison between different implementations of the same algorithm.

        Args:
            limit: Upper limit for algorithm testing

        Returns:
            Dictionary containing performance comparison results
        """
        results: Dict[str, Dict[str, Any]] = {}

        # Compare sieve implementations
        print(f"🔄 Comparing sieve implementations up to {limit:,}...")

        # Standard sieve (force standard implementation)
        from eternal_math.number_theory import _segmented_sieve

        standard_times = []
        for _ in range(3):
            start_time = time.perf_counter()
            # Use standard sieve logic directly
            if limit >= 2:
                sieve = [True] * (limit + 1)
                sieve[0] = sieve[1] = False
                for i in range(2, int(limit**0.5) + 1):
                    if sieve[i]:
                        for j in range(i * i, limit + 1, i):
                            sieve[j] = False
                [i for i in range(2, limit + 1) if sieve[i]]
            end_time = time.perf_counter()
            standard_times.append(end_time - start_time)

        # Optimized implementation
        optimized_times = []
        for _ in range(3):
            start_time = time.perf_counter()
            sieve_of_eratosthenes(limit)
            end_time = time.perf_counter()
            optimized_times.append(end_time - start_time)

        # Segmented sieve (for larger numbers)
        if limit > 1_000_000:
            segmented_times = []
            for _ in range(3):
                start_time = time.perf_counter()
                _segmented_sieve(limit)
                end_time = time.perf_counter()
                segmented_times.append(end_time - start_time)

            results["segmented_sieve"] = {
                "mean_time": statistics.mean(segmented_times),
                "std_dev": (
                    statistics.stdev(segmented_times) if len(segmented_times) > 1 else 0
                ),
                "min_time": min(segmented_times),
                "max_time": max(segmented_times),
                "algorithm": "Segmented Sieve of Eratosthenes",
            }

        results["standard_sieve"] = {
            "mean_time": statistics.mean(standard_times),
            "std_dev": (
                statistics.stdev(standard_times) if len(standard_times) > 1 else 0
            ),
            "min_time": min(standard_times),
            "max_time": max(standard_times),
            "algorithm": "Standard Sieve of Eratosthenes",
        }

        results["optimized_sieve"] = {
            "mean_time": statistics.mean(optimized_times),
            "std_dev": (
                statistics.stdev(optimized_times) if len(optimized_times) > 1 else 0
            ),
            "min_time": min(optimized_times),
            "max_time": max(optimized_times),
            "algorithm": "Optimized Sieve (Auto-selects Implementation)",
        }

        # Calculate performance improvements
        standard_mean = results["standard_sieve"]["mean_time"]
        optimized_mean = results["optimized_sieve"]["mean_time"]

        if standard_mean > 0:
            improvement = ((standard_mean - optimized_mean) / standard_mean) * 100
            results["performance_improvement"] = {
                "percentage": improvement,
                "speedup_factor": (
                    standard_mean / optimized_mean
                    if optimized_mean > 0
                    else float("inf")
                ),
            }

        print(f"✅ Algorithm comparison completed for limit {limit:,}")
        return results


def run_performance_analysis() -> PerformanceBenchmark:
    """Run a complete performance analysis of eternal-math algorithms."""
    benchmark = PerformanceBenchmark()

    # Run comprehensive benchmark suite
    results = benchmark.benchmark_number_theory_suite()

    # Create performance plots
    prime_results = {
        "Sieve of Eratosthenes": results.get("sieve_of_eratosthenes", []),
        "Fibonacci": results.get("fibonacci", []),
        "Perfect Numbers": results.get("perfect_numbers", []),
    }

    benchmark.plot_performance_comparison(
        prime_results, "Algorithm Performance vs Input Size"
    )

    # Generate and save report
    print("\n" + benchmark.generate_performance_report())
    benchmark.save_results("performance_report.txt")

    return benchmark


if __name__ == "__main__":
    # Run performance analysis when executed directly
    run_performance_analysis()
