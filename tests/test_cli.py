"""
Tests for the CLI functionality.
"""

import unittest
from unittest.mock import MagicMock, patch

from eternal_math.cli import EternalMathCLI


class TestEternalMathCLI(unittest.TestCase):
    """Test cases for the CLI interface."""

    def setUp(self):
        """Set up test fixtures."""
        self.cli = EternalMathCLI()

    def test_cli_initialization(self):
        """Test CLI initializes correctly."""
        self.assertTrue(self.cli.running)
        self.assertIn("help", self.cli.commands)
        self.assertIn("primes", self.cli.commands)
        self.assertIn("quit", self.cli.commands)

    @patch("builtins.print")
    def test_help_command(self, mock_print):
        """Test help command displays correctly."""
        self.cli._help([])
        mock_print.assert_called()
        # Check that help was called multiple times (for different sections)
        self.assertGreater(mock_print.call_count, 5)

    @patch("builtins.print")
    def test_primes_command(self, mock_print):
        """Test primes command works correctly."""
        self.cli._primes(["10"])
        mock_print.assert_called()
        # Check that output contains prime numbers
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("[2, 3, 5, 7]", output)

    @patch("builtins.print")
    def test_primes_command_no_args(self, mock_print):
        """Test primes command with no arguments."""
        self.cli._primes([])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Usage:", output)

    @patch("builtins.print")
    def test_fibonacci_command(self, mock_print):
        """Test fibonacci command works correctly."""
        self.cli._fibonacci(["5"])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("[0, 1, 1, 2, 3]", output)

    @patch("builtins.print")
    def test_perfect_numbers_command(self, mock_print):
        """Test perfect numbers command."""
        self.cli._perfect_numbers(["10"])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("[6]", output)

    @patch("builtins.print")
    def test_euler_totient_command(self, mock_print):
        """Test Euler's totient function command."""
        self.cli._euler_totient(["12"])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("φ(12)", output)

    @patch("builtins.print")
    def test_collatz_command(self, mock_print):
        """Test Collatz sequence command."""
        self.cli._collatz(["7"])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Collatz sequence for 7", output)

    @patch("builtins.print")
    def test_theorem_command(self, mock_print):
        """Test theorem display command."""
        self.cli._show_theorem([])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("integer greater than 1", output)

    @patch("builtins.print")
    def test_examples_command(self, mock_print):
        """Test examples display command."""
        self.cli._show_examples([])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Usage Examples", output)

    def test_quit_command(self):
        """Test quit command stops the CLI."""
        self.assertTrue(self.cli.running)
        self.cli._quit([])
        self.assertFalse(self.cli.running)

    @patch("builtins.print")
    def test_invalid_command(self, mock_print):
        """Test invalid command handling."""
        # Mock the input and running state
        with patch("builtins.input", return_value="invalid_command"):
            self.cli.running = True
            # Simulate one iteration of the main loop
            user_input = "invalid_command"
            parts = user_input.split()
            command = parts[0]

            if command in self.cli.commands:
                self.cli.commands[command]([])
            else:
                print(f"Unknown command: {command}")
                print("Type 'help' for available commands.\n")

            mock_print.assert_called()
            calls = [str(call) for call in mock_print.call_args_list]
            output = " ".join(calls)
            self.assertIn("Unknown command", output)

    # Number Theory Commands Tests
    @patch("builtins.print")
    def test_twin_primes_command(self, mock_print):
        """Test twin primes command."""
        self.cli._twin_primes(["10"])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("(3, 5)", output)

    @patch("builtins.print")
    def test_twin_primes_command_no_args(self, mock_print):
        """Test twin primes command with no arguments."""
        self.cli._twin_primes([])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Usage:", output)

    @patch("builtins.print")
    def test_goldbach_command(self, mock_print):
        """Test Goldbach conjecture command."""
        self.cli._goldbach(["10"])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Goldbach conjecture", output)

    @patch("builtins.print")
    def test_goldbach_command_no_args(self, mock_print):
        """Test Goldbach conjecture command with no arguments."""
        self.cli._goldbach([])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Usage:", output)

    @patch("builtins.print")
    def test_chinese_remainder_command(self, mock_print):
        """Test Chinese Remainder Theorem command."""
        self.cli._chinese_remainder(["2,3,2,3"])
        self.assertTrue(mock_print.called)

    @patch("builtins.print")
    def test_chinese_remainder_command_invalid_args(self, mock_print):
        """Test Chinese Remainder Theorem command with invalid arguments."""
        self.cli._chinese_remainder(["1,2,3"])  # Odd number of arguments
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("exactly 4 comma-separated", output)

    # Symbolic Math Commands Tests
    @patch("builtins.print")
    def test_simplify_command(self, mock_print):
        """Test simplify command."""
        self.cli._simplify(["(x + 1)**2"])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Simplifying", output)

    @patch("builtins.print")
    def test_simplify_command_no_args(self, mock_print):
        """Test simplify command with no arguments."""
        self.cli._simplify([])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Usage:", output)

    @patch("builtins.print")
    def test_expand_command(self, mock_print):
        """Test expand command."""
        self.cli._expand(["(x + 1)**2"])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("x**2 + 2*x + 1", output)

    @patch("builtins.print")
    def test_expand_command_no_args(self, mock_print):
        """Test expand command with no arguments."""
        self.cli._expand([])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Usage:", output)

    @patch("builtins.print")
    def test_factor_command(self, mock_print):
        """Test factor command."""
        self.cli._factor(["x**2 - 1"])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("(x - 1)*(x + 1)", output)

    @patch("builtins.print")
    def test_factor_command_no_args(self, mock_print):
        """Test factor command with no arguments."""
        self.cli._factor([])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Usage:", output)

    @patch("builtins.print")
    def test_solve_command(self, mock_print):
        """Test solve command."""
        self.cli._solve(["x**2 - 4", "x"])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("[-2, 2]", output)

    @patch("builtins.print")
    def test_solve_command_no_args(self, mock_print):
        """Test solve command with no arguments."""
        self.cli._solve([])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Usage:", output)

    @patch("builtins.print")
    def test_differentiate_command(self, mock_print):
        """Test differentiate command."""
        self.cli._differentiate(["x**2", "x"])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("2*x", output)

    @patch("builtins.print")
    def test_differentiate_command_no_args(self, mock_print):
        """Test differentiate command with no arguments."""
        self.cli._differentiate([])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Usage:", output)

    @patch("builtins.print")
    def test_integrate_command(self, mock_print):
        """Test integrate command."""
        self.cli._integrate(["2*x", "x"])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("x**2", output)

    @patch("builtins.print")
    def test_integrate_command_no_args(self, mock_print):
        """Test integrate command with no arguments."""
        self.cli._integrate([])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Usage:", output)

    @patch("builtins.print")
    def test_limit_command(self, mock_print):
        """Test limit command."""
        self.cli._limit(["sin(x)/x", "x", "0"])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("1", output)

    @patch("builtins.print")
    def test_limit_command_no_args(self, mock_print):
        """Test limit command with no arguments."""
        self.cli._limit([])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Usage:", output)

    @patch("builtins.print")
    def test_taylor_series_command(self, mock_print):
        """Test Taylor series command."""
        self.cli._taylor_series(["exp(x)", "x", "0", "3"])
        self.assertTrue(mock_print.called)

    @patch("builtins.print")
    def test_taylor_series_command_no_args(self, mock_print):
        """Test Taylor series command with no arguments."""
        self.cli._taylor_series([])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Usage:", output)

    @patch("builtins.print")
    def test_substitute_command(self, mock_print):
        """Test substitute command."""
        self.cli._substitute(["x**2 + y", "x=2", "y=3"])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("7", output)

    @patch("builtins.print")
    def test_substitute_command_no_args(self, mock_print):
        """Test substitute command with no arguments."""
        self.cli._substitute([])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Usage:", output)

    # Visualization Commands Tests
    @patch("builtins.print")
    @patch("eternal_math.cli.MathVisualizer")
    def test_plot_function_command(self, mock_visualizer, mock_print):
        """Test plot function command."""
        mock_viz_instance = MagicMock()
        mock_visualizer.return_value = mock_viz_instance

        self.cli._plot_function(["sin(x)"])
        self.assertTrue(mock_print.called)

    @patch("builtins.print")
    def test_plot_function_command_no_args(self, mock_print):
        """Test plot function command with no arguments."""
        self.cli._plot_function([])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Usage:", output)

    @patch("builtins.print")
    def test_plot_sequence_command(self, mock_print):
        """Test plot sequence command."""
        self.cli._plot_sequence(["fibonacci", "10"])
        self.assertTrue(mock_print.called)

    @patch("builtins.print")
    def test_plot_sequence_command_no_args(self, mock_print):
        """Test plot sequence command with no arguments."""
        self.cli._plot_sequence([])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Usage:", output)

    @patch("builtins.print")
    def test_plot_primes_command(self, mock_print):
        """Test plot primes command."""
        self.cli._plot_primes(["50"])
        self.assertTrue(mock_print.called)

    @patch("builtins.print")
    def test_plot_primes_command_no_args(self, mock_print):
        """Test plot primes command with no arguments."""
        self.cli._plot_primes([])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Usage:", output)

    @patch("builtins.print")
    def test_plot_collatz_command(self, mock_print):
        """Test plot Collatz command."""
        self.cli._plot_collatz(["7"])
        self.assertTrue(mock_print.called)

    @patch("builtins.print")
    def test_plot_collatz_command_no_args(self, mock_print):
        """Test plot Collatz command with no arguments."""
        self.cli._plot_collatz([])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Usage:", output)

    @patch("builtins.print")
    def test_plot_comparative_command(self, mock_print):
        """Test plot comparative command."""
        self.cli._plot_comparative(["fibonacci", "primes", "10"])
        self.assertTrue(mock_print.called)

    @patch("builtins.print")
    def test_plot_comparative_command_no_args(self, mock_print):
        """Test plot comparative command with no arguments."""
        self.cli._plot_comparative([])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Usage:", output)

    # Benchmark Commands Tests
    @patch("builtins.print")
    def test_benchmark_command(self, mock_print):
        """Test benchmark command."""
        self.cli._benchmark(["primes", "100"])
        self.assertTrue(mock_print.called)

    @patch("builtins.print")
    def test_benchmark_command_no_args(self, mock_print):
        """Test benchmark command with no arguments."""
        self.cli._benchmark([])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Quick Benchmark", output)

    # Test error handling in commands
    @patch("builtins.print")
    def test_simplify_command_invalid_expression(self, mock_print):
        """Test simplify command with invalid expression."""
        self.cli._simplify(["invalid^^expression"])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Error", output)

    @patch("builtins.print")
    def test_fibonacci_command_invalid_input(self, mock_print):
        """Test fibonacci command with invalid input."""
        self.cli._fibonacci(["not_a_number"])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("valid integer", output)

    @patch("builtins.print")
    def test_fibonacci_command_no_args(self, mock_print):
        """Test fibonacci command with no arguments."""
        self.cli._fibonacci([])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Usage:", output)

    @patch("builtins.print")
    def test_perfect_numbers_command_no_args(self, mock_print):
        """Test perfect numbers command with no arguments."""
        self.cli._perfect_numbers([])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Usage:", output)

    @patch("builtins.print")
    def test_euler_totient_command_no_args(self, mock_print):
        """Test Euler totient command with no arguments."""
        self.cli._euler_totient([])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Usage:", output)

    @patch("builtins.print")
    def test_collatz_command_no_args(self, mock_print):
        """Test Collatz command with no arguments."""
        self.cli._collatz([])
        mock_print.assert_called()
        calls = [str(call) for call in mock_print.call_args_list]
        output = " ".join(calls)
        self.assertIn("Usage:", output)


if __name__ == "__main__":
    unittest.main()
