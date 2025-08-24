"""
Tests for the benchmarks module.
"""

import os
import tempfile
import unittest
from typing import Any
from unittest.mock import patch

from eternal_math.benchmarks import (
    BenchmarkResult,
    PerformanceBenchmark,
    run_performance_analysis,
)
from eternal_math.core import gcd
from eternal_math.number_theory import fibonacci_sequence, sieve_of_eratosthenes


class TestBenchmarkResult(unittest.TestCase):
    """Test the BenchmarkResult dataclass."""

    def test_benchmark_result_creation(self) -> None:
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

    def setUp(self) -> None:
        """Set up test fixtures."""
        self.benchmark = PerformanceBenchmark()

    def test_benchmark_initialization(self) -> None:
        """Test benchmark system initializes correctly."""
        self.assertIsInstance(self.benchmark.results, list)
        self.assertEqual(len(self.benchmark.results), 0)

    def test_time_simple_function(self) -> None:
        """Test timing a simple function."""

        def simple_add(a: int, b: int) -> int:
            return a + b

        result = self.benchmark.time_function(simple_add, 5, 10, iterations=5)

        self.assertEqual(result.function_name, "simple_add")
        self.assertEqual(result.iterations, 5)
        self.assertGreater(result.mean_time, 0)
        self.assertGreaterEqual(result.std_dev, 0)
        self.assertGreater(result.max_time, 0)
        self.assertGreater(result.min_time, 0)
        self.assertEqual(len(self.benchmark.results), 1)

    def test_time_gcd_function(self) -> None:
        """Test timing GCD function."""
        result = self.benchmark.time_function(gcd, 48, 18, iterations=10)

        self.assertEqual(result.function_name, "gcd")
        self.assertEqual(result.iterations, 10)
        self.assertGreater(result.mean_time, 0)
        # GCD should be very fast, so mean time should be small
        self.assertLess(result.mean_time, 0.001)  # Less than 1ms

    def test_extract_input_size(self) -> None:
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

    def test_find_perfect_numbers(self) -> None:
        """Test the helper function for finding perfect numbers."""
        perfect_nums = self.benchmark.find_perfect_numbers(30)
        expected = [6, 28]
        self.assertEqual(perfect_nums, expected)

        # Test edge case
        perfect_nums = self.benchmark.find_perfect_numbers(5)
        self.assertEqual(perfect_nums, [])

    def test_benchmark_sieve_of_eratosthenes(self) -> None:
        """Test benchmarking the sieve algorithm."""
        result = self.benchmark.time_function(sieve_of_eratosthenes, 100, iterations=3)

        self.assertEqual(result.function_name, "sieve_of_eratosthenes")
        self.assertEqual(result.input_size, 100)
        self.assertEqual(result.iterations, 3)
        self.assertGreater(result.mean_time, 0)

    def test_benchmark_fibonacci_sequence(self) -> None:
        """Test benchmarking fibonacci sequence generation."""
        result = self.benchmark.time_function(fibonacci_sequence, 20, iterations=5)

        self.assertEqual(result.function_name, "fibonacci_sequence")
        self.assertEqual(result.input_size, 20)
        self.assertEqual(result.iterations, 5)
        self.assertGreater(result.mean_time, 0)

    def test_benchmark_prime_algorithms_small(self) -> None:
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

    def test_benchmark_fibonacci_algorithms_small(self) -> None:
        """Test benchmarking fibonacci algorithms with small sizes."""
        results = self.benchmark.benchmark_fibonacci_algorithms([5, 10])

        self.assertEqual(len(results), 2)

        for result in results:
            self.assertEqual(result.function_name, "fibonacci_sequence")
            self.assertGreater(result.mean_time, 0)

    def test_generate_performance_report_empty(self) -> None:
        """Test generating report with no results."""
        report = self.benchmark.generate_performance_report()
        self.assertEqual(report, "No benchmark results available.")

    def test_generate_performance_report_with_results(self) -> None:
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

    def setUp(self) -> None:
        """Set up test fixtures."""
        self.benchmark = PerformanceBenchmark()

    def test_multiple_function_benchmarks(self) -> None:
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

    def test_benchmark_report_accuracy(self) -> None:
        """Test that benchmark report contains accurate information."""
        # Run a specific benchmark
        result = self.benchmark.time_function(gcd, 144, 89, iterations=10)

        # Generate report
        report = self.benchmark.generate_performance_report()

        # Check report contains specific information
        self.assertIn(f"Mean Time: {result.mean_time:.6f}s", report)
        self.assertIn(f"Iterations: {result.iterations}", report)
        self.assertIn("Function: gcd", report)


class TestBenchmarkSuite(unittest.TestCase):
    """Test the comprehensive benchmark suite methods."""

    def setUp(self) -> None:
        """Set up test fixtures."""
        self.benchmark = PerformanceBenchmark()

    @patch("builtins.print")  # Suppress output during tests
    def test_benchmark_number_theory_suite(self, mock_print: Any) -> None:
        """Test the complete number theory benchmark suite."""
        with (
            patch.object(self.benchmark, "benchmark_prime_algorithms") as mock_prime,
            patch.object(self.benchmark, "benchmark_fibonacci_algorithms") as mock_fib,
        ):

            # Mock return values
            mock_prime.return_value = {
                "sieve_of_eratosthenes": [
                    BenchmarkResult(
                        "sieve_of_eratosthenes", 100, 0.1, 5, 0.02, 0.001, 0.019, 0.021
                    )
                ],
                "is_prime_checks": [
                    BenchmarkResult(
                        "is_prime", 97, 0.05, 100, 0.0005, 0.0001, 0.0004, 0.0006
                    )
                ],
            }
            mock_fib.return_value = [
                BenchmarkResult(
                    "fibonacci_sequence", 10, 0.01, 10, 0.001, 0.0001, 0.0009, 0.0011
                )
            ]

            results = self.benchmark.benchmark_number_theory_suite()

            # Check that all expected categories are present
            self.assertIn("sieve_of_eratosthenes", results)
            self.assertIn("is_prime_checks", results)
            self.assertIn("fibonacci", results)
            self.assertIn("perfect_numbers", results)
            self.assertIn("gcd", results)

    def test_save_results(self) -> None:
        """Test saving benchmark results to file."""
        # Add some test results
        self.benchmark.time_function(gcd, 48, 18, iterations=3)

        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:
            temp_filename = f.name

        try:
            # Save results
            self.benchmark.save_results(temp_filename)

            # Read back and verify
            with open(temp_filename, "r") as f:
                content = f.read()

            self.assertIn("Eternal Math Performance Report", content)
            self.assertIn("gcd", content)

        finally:
            # Clean up
            if os.path.exists(temp_filename):
                os.remove(temp_filename)

    @patch("matplotlib.pyplot.show")
    @patch("matplotlib.pyplot.savefig")
    @patch("builtins.print")
    def test_plot_performance_comparison(
        self, mock_print: Any, mock_savefig: Any, mock_show: Any
    ) -> None:
        """Test performance comparison plotting."""
        # Create test results
        results = {
            "algorithm1": [
                BenchmarkResult("func1", 100, 0.1, 5, 0.02, 0.001, 0.019, 0.021),
                BenchmarkResult("func1", 200, 0.2, 5, 0.04, 0.002, 0.038, 0.042),
            ],
            "algorithm2": [
                BenchmarkResult("func2", 100, 0.05, 5, 0.01, 0.0005, 0.0095, 0.0105),
                BenchmarkResult("func2", 200, 0.1, 5, 0.02, 0.001, 0.019, 0.021),
            ],
        }

        self.benchmark.plot_performance_comparison(results, "Test Performance")

        # Verify plotting functions were called
        mock_savefig.assert_called_once()
        mock_show.assert_called_once()

        # Check that the saved filename is correct
        args, kwargs = mock_savefig.call_args
        expected_filename = "math_plots/benchmark_test_performance.png"
        self.assertEqual(args[0], expected_filename)

    @patch("matplotlib.pyplot.legend")
    def test_plot_performance_comparison_empty_results(self, mock_legend: Any) -> None:
        """Test plotting with empty results."""
        with (
            patch("matplotlib.pyplot.show") as mock_show,
            patch("matplotlib.pyplot.savefig") as mock_savefig,
        ):

            results: dict[str, list[BenchmarkResult]] = {"empty_algorithm": []}
            self.benchmark.plot_performance_comparison(results, "Empty Test")

            # Should still create plot and call show/savefig
            mock_show.assert_called_once()
            mock_savefig.assert_called_once()

    @patch("matplotlib.pyplot.legend")
    def test_plot_performance_comparison_no_input_sizes(self, mock_legend: Any) -> None:
        """Test plotting with results that have no input sizes."""
        with (
            patch("matplotlib.pyplot.show") as mock_show,
            patch("matplotlib.pyplot.savefig") as mock_savefig,
        ):

            results = {
                "no_input_size": [
                    BenchmarkResult("func", 0, 0.1, 5, 0.02, 0.001, 0.019, 0.021)
                ]
            }
            self.benchmark.plot_performance_comparison(results, "No Input Size Test")

            # Should still create plot even without data points
            mock_show.assert_called_once()
            mock_savefig.assert_called_once()

    def test_benchmark_algorithm_comparison(self) -> None:
        """Test algorithm comparison benchmarking."""
        # Test with a small limit for faster execution
        results = self.benchmark.benchmark_algorithm_comparison(limit=1000)

        # Check expected keys in results
        self.assertIn("standard_sieve", results)
        self.assertIn("optimized_sieve", results)
        self.assertIn("performance_improvement", results)

        # Check structure of individual results
        for key in ["standard_sieve", "optimized_sieve"]:
            self.assertIn("mean_time", results[key])
            self.assertIn("std_dev", results[key])
            self.assertIn("min_time", results[key])
            self.assertIn("max_time", results[key])
            self.assertIn("algorithm", results[key])

        # Check performance improvement calculations
        improvement = results["performance_improvement"]
        self.assertIn("percentage", improvement)
        self.assertIn("speedup_factor", improvement)
        self.assertIsInstance(improvement["percentage"], (int, float))
        self.assertIsInstance(improvement["speedup_factor"], (int, float))

    @patch("builtins.print")
    def test_benchmark_algorithm_comparison_large_limit(self, mock_print: Any) -> None:
        """Test algorithm comparison with large limit to trigger segmented sieve."""
        # Test with large limit that would trigger segmented sieve
        results = self.benchmark.benchmark_algorithm_comparison(limit=2_000_000)

        # Should include segmented sieve results for large inputs
        self.assertIn("segmented_sieve", results)

        # Check segmented sieve result structure
        segmented = results["segmented_sieve"]
        self.assertIn("mean_time", segmented)
        self.assertIn("algorithm", segmented)
        self.assertEqual(segmented["algorithm"], "Segmented Sieve of Eratosthenes")


class TestRunPerformanceAnalysis(unittest.TestCase):
    """Test the main performance analysis runner."""

    @patch("matplotlib.pyplot.show")
    @patch("matplotlib.pyplot.savefig")
    @patch("builtins.print")
    def test_run_performance_analysis(
        self, mock_print: Any, mock_savefig: Any, mock_show: Any
    ) -> None:
        """Test the complete performance analysis workflow."""
        # Mock the benchmark methods to run faster
        with patch.object(
            PerformanceBenchmark, "benchmark_number_theory_suite"
        ) as mock_suite:
            mock_suite.return_value = {
                "sieve_of_eratosthenes": [
                    BenchmarkResult(
                        "sieve_of_eratosthenes", 100, 0.1, 5, 0.02, 0.001, 0.019, 0.021
                    )
                ],
                "fibonacci": [
                    BenchmarkResult(
                        "fibonacci_sequence",
                        10,
                        0.01,
                        10,
                        0.001,
                        0.0001,
                        0.0009,
                        0.0011,
                    )
                ],
                "perfect_numbers": [
                    BenchmarkResult(
                        "find_perfect_numbers", 100, 0.5, 3, 0.167, 0.01, 0.16, 0.17
                    )
                ],
            }

            with patch.object(PerformanceBenchmark, "save_results") as mock_save:
                benchmark = run_performance_analysis()

                # Check that benchmark object is returned
                self.assertIsInstance(benchmark, PerformanceBenchmark)

                # Verify that the suite was run
                mock_suite.assert_called_once()

                # Verify plotting and saving were called
                mock_savefig.assert_called()
                mock_save.assert_called_with("performance_report.txt")


if __name__ == "__main__":
    unittest.main()
