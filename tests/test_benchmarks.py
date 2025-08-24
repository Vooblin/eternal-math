"""
Tests for the benchmarks module.
"""

import unittest

from eternal_math.benchmarks import BenchmarkResult, PerformanceBenchmark
from eternal_math.core import gcd
from eternal_math.number_theory import fibonacci_sequence, sieve_of_eratosthenes


class TestBenchmarkResult(unittest.TestCase):
    """Test the BenchmarkResult dataclass."""

    def test_benchmark_result_creation(self):
        """Test BenchmarkResult initialization."""
        result = BenchmarkResult(
            function_name="test_func",
            input_size=100,
            execution_time=0.5,
            iterations=10,
            mean_time=0.05,
            std_dev=0.01,
            min_time=0.04,
            max_time=0.06,
        )

        self.assertEqual(result.function_name, "test_func")
        self.assertEqual(result.input_size, 100)
        self.assertEqual(result.execution_time, 0.5)
        self.assertEqual(result.iterations, 10)
        self.assertEqual(result.mean_time, 0.05)
        self.assertEqual(result.std_dev, 0.01)
        self.assertEqual(result.min_time, 0.04)
        self.assertEqual(result.max_time, 0.06)


class TestPerformanceBenchmark(unittest.TestCase):
    """Test the PerformanceBenchmark class."""

    def setUp(self):
        """Set up test fixtures."""
        self.benchmark = PerformanceBenchmark()

    def test_benchmark_initialization(self):
        """Test benchmark system initializes correctly."""
        self.assertIsInstance(self.benchmark.results, list)
        self.assertEqual(len(self.benchmark.results), 0)

    def test_time_simple_function(self):
        """Test timing a simple function."""

        def simple_add(a, b):
            return a + b

        result = self.benchmark.time_function(simple_add, 5, 10, iterations=5)

        self.assertEqual(result.function_name, "simple_add")
        self.assertEqual(result.iterations, 5)
        self.assertGreater(result.mean_time, 0)
        self.assertGreaterEqual(result.std_dev, 0)
        self.assertGreater(result.max_time, 0)
        self.assertGreater(result.min_time, 0)
        self.assertEqual(len(self.benchmark.results), 1)

    def test_time_gcd_function(self):
        """Test timing GCD function."""
        result = self.benchmark.time_function(gcd, 48, 18, iterations=10)

        self.assertEqual(result.function_name, "gcd")
        self.assertEqual(result.iterations, 10)
        self.assertGreater(result.mean_time, 0)
        # GCD should be very fast, so mean time should be small
        self.assertLess(result.mean_time, 0.001)  # Less than 1ms

    def test_extract_input_size(self):
        """Test input size extraction from function arguments."""
        # Test with integer argument
        size = self.benchmark._extract_input_size((100,), {})
        self.assertEqual(size, 100)

        # Test with keyword argument
        size = self.benchmark._extract_input_size((), {"n": 50})
        self.assertEqual(size, 50)

        # Test with list argument
        size = self.benchmark._extract_input_size(([1, 2, 3, 4, 5],), {})
        self.assertEqual(size, 5)

        # Test with no recognizable input size (non-sequence)
        size = self.benchmark._extract_input_size((42.5,), {})
        self.assertEqual(size, 0)

    def test_find_perfect_numbers(self):
        """Test the helper function for finding perfect numbers."""
        perfect_nums = self.benchmark.find_perfect_numbers(30)
        expected = [6, 28]
        self.assertEqual(perfect_nums, expected)

        # Test edge case
        perfect_nums = self.benchmark.find_perfect_numbers(5)
        self.assertEqual(perfect_nums, [])

    def test_benchmark_sieve_of_eratosthenes(self):
        """Test benchmarking the sieve algorithm."""
        result = self.benchmark.time_function(sieve_of_eratosthenes, 100, iterations=3)

        self.assertEqual(result.function_name, "sieve_of_eratosthenes")
        self.assertEqual(result.input_size, 100)
        self.assertEqual(result.iterations, 3)
        self.assertGreater(result.mean_time, 0)

    def test_benchmark_fibonacci_sequence(self):
        """Test benchmarking fibonacci sequence generation."""
        result = self.benchmark.time_function(fibonacci_sequence, 20, iterations=5)

        self.assertEqual(result.function_name, "fibonacci_sequence")
        self.assertEqual(result.input_size, 20)
        self.assertEqual(result.iterations, 5)
        self.assertGreater(result.mean_time, 0)

    def test_benchmark_prime_algorithms_small(self):
        """Test benchmarking prime algorithms with small sizes."""
        # Use small sizes for faster testing
        results = self.benchmark.benchmark_prime_algorithms([10, 50])

        self.assertIn("sieve_of_eratosthenes", results)
        self.assertIn("is_prime_checks", results)

        sieve_results = results["sieve_of_eratosthenes"]
        self.assertEqual(len(sieve_results), 2)

        for result in sieve_results:
            self.assertEqual(result.function_name, "sieve_of_eratosthenes")
            self.assertGreater(result.mean_time, 0)

    def test_benchmark_fibonacci_algorithms_small(self):
        """Test benchmarking fibonacci algorithms with small sizes."""
        results = self.benchmark.benchmark_fibonacci_algorithms([5, 10])

        self.assertEqual(len(results), 2)

        for result in results:
            self.assertEqual(result.function_name, "fibonacci_sequence")
            self.assertGreater(result.mean_time, 0)

    def test_generate_performance_report_empty(self):
        """Test generating report with no results."""
        report = self.benchmark.generate_performance_report()
        self.assertEqual(report, "No benchmark results available.")

    def test_generate_performance_report_with_results(self):
        """Test generating report with results."""
        # Add some benchmark results
        self.benchmark.time_function(gcd, 48, 18, iterations=3)
        self.benchmark.time_function(fibonacci_sequence, 10, iterations=2)

        report = self.benchmark.generate_performance_report()

        self.assertIn("Eternal Math Performance Report", report)
        self.assertIn("gcd", report)
        self.assertIn("fibonacci_sequence", report)
        self.assertIn("Mean Time:", report)
        self.assertIn("Std Dev:", report)


class TestBenchmarkIntegration(unittest.TestCase):
    """Integration tests for the benchmark system."""

    def setUp(self):
        """Set up test fixtures."""
        self.benchmark = PerformanceBenchmark()

    def test_multiple_function_benchmarks(self):
        """Test benchmarking multiple different functions."""
        # Benchmark several functions
        self.benchmark.time_function(gcd, 100, 25, iterations=5)
        self.benchmark.time_function(fibonacci_sequence, 15, iterations=3)
        self.benchmark.time_function(sieve_of_eratosthenes, 50, iterations=2)

        # Check that all results were recorded
        self.assertEqual(len(self.benchmark.results), 3)

        # Check function names
        function_names = [r.function_name for r in self.benchmark.results]
        self.assertIn("gcd", function_names)
        self.assertIn("fibonacci_sequence", function_names)
        self.assertIn("sieve_of_eratosthenes", function_names)

        # Verify all have positive execution times
        for result in self.benchmark.results:
            self.assertGreater(result.mean_time, 0)
            self.assertGreaterEqual(result.std_dev, 0)

    def test_benchmark_report_accuracy(self):
        """Test that benchmark report contains accurate information."""
        # Run a specific benchmark
        result = self.benchmark.time_function(gcd, 144, 89, iterations=10)

        # Generate report
        report = self.benchmark.generate_performance_report()

        # Check report contains specific information
        self.assertIn(f"Mean Time: {result.mean_time:.6f}s", report)
        self.assertIn(f"Iterations: {result.iterations}", report)
        self.assertIn("Function: gcd", report)


if __name__ == "__main__":
    unittest.main()
