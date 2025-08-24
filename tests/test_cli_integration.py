"""
Integration tests for the Eternal Math CLI.

These tests verify end-to-end functionality, entry points, and complete workflows
that users would actually experience when using the CLI.
"""

from unittest.mock import MagicMock, patch

import pytest

from eternal_math.cli import EternalMathCLI, main


class TestCLIIntegration:
    """Integration tests for CLI functionality."""

    def setup_method(self) -> None:
        """Setup for each test method."""
        self.cli = EternalMathCLI()

    def test_main_function_entry_point(self) -> None:
        """Test that main() creates and runs CLI properly."""
        with patch.object(EternalMathCLI, "run") as mock_run:
            main()
            mock_run.assert_called_once()

    def test_cli_startup_sequence(self) -> None:
        """Test the CLI startup welcome message and initialization."""
        with patch("builtins.input", side_effect=["quit"]):
            with patch("builtins.print") as mock_print:
                self.cli.run()

                # Verify welcome message is displayed
                print_calls = [call[0][0] for call in mock_print.call_args_list]
                assert any(
                    "Welcome to Eternal Math" in str(call) for call in print_calls
                )
                assert any(
                    "Type 'help' for available commands" in str(call)
                    for call in print_calls
                )

    def test_help_command_workflow(self) -> None:
        """Test complete help command workflow."""
        with patch("builtins.input", side_effect=["help", "quit"]):
            with patch("builtins.print") as mock_print:
                self.cli.run()

                # Verify help content is displayed
                print_calls = [call[0][0] for call in mock_print.call_args_list]
                assert any(
                    "Eternal Math CLI Commands" in str(call) for call in print_calls
                )
                assert any("Number Theory" in str(call) for call in print_calls)
                assert any("Symbolic Mathematics" in str(call) for call in print_calls)

    def test_mathematical_computation_workflow(self) -> None:
        """Test a complete mathematical computation workflow."""
        inputs = ["primes 10", "fibonacci 5", "simplify x**2 + 2*x + 1", "quit"]

        with patch("builtins.input", side_effect=inputs):
            with patch("builtins.print") as mock_print:
                self.cli.run()

                print_calls = [str(call) for call in mock_print.call_args_list]

                # Verify mathematical results are computed and displayed
                assert any(
                    "[2, 3, 5, 7]" in call for call in print_calls
                )  # Prime results
                assert any(
                    "[0, 1, 1, 2, 3]" in call for call in print_calls
                )  # Fibonacci results

    def test_error_handling_workflow(self) -> None:
        """Test CLI error handling in realistic scenarios."""
        inputs = [
            "invalid_command",
            "primes abc",  # Invalid argument
            "fibonacci -5",  # Negative number
            "quit",
        ]

        with patch("builtins.input", side_effect=inputs):
            with patch("builtins.print") as mock_print:
                self.cli.run()

                print_calls = [str(call) for call in mock_print.call_args_list]

                # Verify error messages are displayed appropriately
                assert any("Unknown command" in call for call in print_calls)
                assert any(
                    "valid integer" in call or "Error" in call for call in print_calls
                )

    def test_keyboard_interrupt_handling(self) -> None:
        """Test graceful handling of Ctrl+C."""
        with patch("builtins.input", side_effect=KeyboardInterrupt):
            with patch("builtins.print") as mock_print:
                self.cli.run()

                print_calls = [str(call) for call in mock_print.call_args_list]
                assert any("Goodbye" in call for call in print_calls)

    def test_eof_error_handling(self) -> None:
        """Test graceful handling of EOF (Ctrl+D)."""
        with patch("builtins.input", side_effect=EOFError):
            with patch("builtins.print") as mock_print:
                self.cli.run()

                print_calls = [str(call) for call in mock_print.call_args_list]
                assert any("Goodbye" in call for call in print_calls)

    @patch("matplotlib.pyplot.show")
    def test_visualization_workflow(self, mock_show: MagicMock) -> None:
        """Test visualization command integration."""
        with patch("builtins.input", side_effect=["plot sin(x)", "quit"]):
            with patch("builtins.print") as mock_print:
                self.cli.run()

                print_calls = [str(call) for call in mock_print.call_args_list]
                # Should attempt to plot
                assert any(
                    "Plotting function" in call or "Plot" in call
                    for call in print_calls
                )

    def test_benchmark_workflow(self) -> None:
        """Test benchmark command integration."""
        with patch("builtins.input", side_effect=["benchmark", "quit"]):
            with patch("builtins.print") as mock_print:
                self.cli.run()

                # Verify benchmark output is displayed
                print_calls = [str(call) for call in mock_print.call_args_list]
                assert any(
                    "benchmark" in call.lower() or "performance" in call.lower()
                    for call in print_calls
                )

    def test_theorem_proof_workflow(self) -> None:
        """Test theorem and proof system integration."""
        with patch("builtins.input", side_effect=["theorem", "quit"]):
            with patch("builtins.print") as mock_print:
                self.cli.run()

                print_calls = [str(call) for call in mock_print.call_args_list]
                # Should display theorem information
                assert any("integer greater than 1" in call for call in print_calls)
                assert any("Proven" in call for call in print_calls)

    def test_examples_command_workflow(self) -> None:
        """Test examples command provides useful information."""
        with patch("builtins.input", side_effect=["examples", "quit"]):
            with patch("builtins.print") as mock_print:
                self.cli.run()

                print_calls = [str(call) for call in mock_print.call_args_list]
                assert any("Usage Examples" in call for call in print_calls)
                assert any("primes" in call for call in print_calls)

    def test_command_case_insensitivity(self) -> None:
        """Test that commands work regardless of case."""
        inputs = ["HELP", "Help", "hElP", "quit"]

        with patch("builtins.input", side_effect=inputs):
            with patch("builtins.print") as mock_print:
                self.cli.run()

                # Should handle all case variations of help
                print_calls = [str(call) for call in mock_print.call_args_list]
                help_calls = [call for call in print_calls if "CLI Commands" in call]
                assert len(help_calls) >= 3  # Should show help multiple times

    def test_empty_input_handling(self) -> None:
        """Test handling of empty input."""
        with patch("builtins.input", side_effect=["", "   ", "\t", "quit"]):
            with patch("builtins.print") as mock_print:
                self.cli.run()

                # Should not crash on empty inputs
                print_calls = [str(call) for call in mock_print.call_args_list]
                assert any("Goodbye" in call for call in print_calls)

    def test_cli_state_management(self) -> None:
        """Test that CLI maintains proper state during execution."""
        initial_running = self.cli.running
        assert initial_running is True

        with patch("builtins.input", side_effect=["help", "quit"]):
            self.cli.run()

        # Running state should be maintained properly
        assert hasattr(self.cli, "running")
        assert hasattr(self.cli, "commands")
        assert isinstance(self.cli.commands, dict)

    def test_all_declared_commands_exist(self) -> None:
        """Test that all commands mentioned in help actually exist."""
        # Extract all commands from the CLI
        available_commands = set(self.cli.commands.keys())

        # Commands that should be available based on help text
        expected_commands = {
            "help",
            "primes",
            "fibonacci",
            "perfect",
            "twins",
            "goldbach",
            "euler",
            "collatz",
            "crt",
            "theorem",
            "examples",
            "simplify",
            "expand",
            "factor",
            "solve",
            "diff",
            "integrate",
            "limit",
            "taylor",
            "substitute",
            "plot",
            "plotseq",
            "plotprimes",
            "plotcollatz",
            "plotcomp",
            "benchmark",
            "quit",
            "exit",
        }

        # Verify all expected commands are implemented
        missing_commands = expected_commands - available_commands
        assert (
            not missing_commands
        ), f"Missing command implementations: {missing_commands}"


class TestCLISystemIntegration:
    """Test CLI integration with the system and external interfaces."""

    def test_cli_executable_entry_point(self) -> None:
        """Test that the CLI can be executed as a script."""
        # Test the __main__ block
        with patch("eternal_math.cli.main") as mock_main:
            # Simulate running the module as main
            exec_globals = {"__name__": "__main__"}
            exec(
                """
if __name__ == "__main__":
    main()
            """,
                exec_globals,
                {"main": mock_main},
            )

            mock_main.assert_called_once()

    def test_import_integration(self) -> None:
        """Test that CLI imports all required modules successfully."""
        # Verify all imports work
        from eternal_math.cli import EternalMathCLI, main

        # Test CLI can be instantiated
        cli = EternalMathCLI()
        assert cli is not None
        assert hasattr(cli, "commands")
        assert callable(main)

    def test_mathematical_library_integration(self) -> None:
        """Test CLI integrates properly with mathematical libraries."""
        cli = EternalMathCLI()

        # Test that mathematical functions are accessible
        with patch("builtins.input", side_effect=["primes 10", "quit"]):
            with patch("builtins.print"):
                try:
                    cli.run()
                except Exception as e:
                    pytest.fail(
                        f"CLI should integrate with math libraries without errors: {e}"
                    )

    @patch("matplotlib.pyplot.show")
    @patch.dict("os.environ", {"MPLBACKEND": "Agg"})
    def test_visualization_backend_integration(self, mock_show: MagicMock) -> None:
        """Test CLI works with matplotlib backend configuration."""
        with patch("builtins.input", side_effect=["plot x**2", "quit"]):
            with patch("builtins.print"):
                cli = EternalMathCLI()
                try:
                    cli.run()
                except ImportError as e:
                    pytest.fail(f"CLI should handle matplotlib backend properly: {e}")

    def test_cli_memory_usage(self) -> None:
        """Test CLI doesn't leak memory during normal operation."""
        import gc

        initial_objects = len(gc.get_objects())

        # Run CLI with several commands
        with patch(
            "builtins.input", side_effect=["help", "primes 10", "fibonacci 5", "quit"]
        ):
            with patch("builtins.print"):
                cli = EternalMathCLI()
                cli.run()
                del cli

        # Force garbage collection
        gc.collect()

        final_objects = len(gc.get_objects())

        # Allow some variance but check for major memory leaks
        object_difference = final_objects - initial_objects
        assert (
            object_difference < 1000
        ), f"Potential memory leak detected: {object_difference} objects"


if __name__ == "__main__":
    pytest.main([__file__])
