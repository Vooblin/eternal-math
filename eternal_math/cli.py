"""
Interactive Command Line Interface for Eternal Math

This module provides an interactive CLI for exploring mathematical concepts,
running calculations, and examining proofs.
"""

from typing import List, Optional, Dict, Any
from eternal_math import (
    sieve_of_eratosthenes, fibonacci_sequence, is_perfect_number,
    twin_primes, verify_goldbach_conjecture, euler_totient,
    collatz_sequence, NumberTheoryUtils, gcd,
    create_fundamental_theorem_of_arithmetic,
    SymbolicMath, CalculusUtils, AlgebraUtils,
    MathVisualizer, create_output_directory,
    PerformanceBenchmark, run_performance_analysis
)


class EternalMathCLI:
    """Interactive CLI for Eternal Math exploration."""
    
    def __init__(self) -> None:
        """Initialize the CLI with available commands."""
        self.commands = {
            'help': self._help,
            'primes': self._primes,
            'fibonacci': self._fibonacci,
            'perfect': self._perfect_numbers,
            'twins': self._twin_primes,
            'goldbach': self._goldbach,
            'euler': self._euler_totient,
            'collatz': self._collatz,
            'crt': self._chinese_remainder,
            'theorem': self._show_theorem,
            'examples': self._show_examples,
            # Symbolic math commands
            'simplify': self._simplify,
            'expand': self._expand,
            'factor': self._factor,
            'solve': self._solve,
            'diff': self._differentiate,
            'integrate': self._integrate,
            'limit': self._limit,
            'taylor': self._taylor_series,
            'substitute': self._substitute,
            # Visualization commands
            'plot': self._plot_function,
            'plotseq': self._plot_sequence,
            'plotprimes': self._plot_primes,
            'plotcollatz': self._plot_collatz,
            'plotcomp': self._plot_comparative,
            'benchmark': self._benchmark,
            'quit': self._quit,
            'exit': self._quit,
        }
        self.running = True
        self.visualizer = MathVisualizer()
        self.output_dir = create_output_directory()
    
    def run(self) -> None:
        """Start the interactive CLI session."""
        print("🧮 Welcome to Eternal Math Interactive CLI")
        print("=" * 50)
        print("Explore mathematical concepts interactively!")
        print("Type 'help' for available commands or 'quit' to exit.\n")
        
        while self.running:
            try:
                user_input = input("eternal-math> ").strip().lower()
                if not user_input:
                    continue
                
                parts = user_input.split()
                command = parts[0]
                args = parts[1:] if len(parts) > 1 else []
                
                if command in self.commands:
                    self.commands[command](args)
                else:
                    print(f"Unknown command: {command}")
                    print("Type 'help' for available commands.\n")
                    
            except KeyboardInterrupt:
                print("\n\nGoodbye! 👋")
                break
            except EOFError:
                print("\n\nGoodbye! 👋")
                break
            except Exception as e:
                print(f"Error: {e}\n")
    
    def _help(self, args: List[str]) -> None:
        """Display help information."""
        print("\n📚 Eternal Math CLI Commands:")
        print("-" * 40)
        print("🔢 Number Theory:")
        print("  primes <n>        - Generate primes up to n")
        print("  fibonacci <n>     - Generate first n Fibonacci numbers")
        print("  perfect <n>       - Find perfect numbers up to n")
        print("  twins <n>         - Find twin prime pairs up to n")
        print("  goldbach <n>      - Verify Goldbach conjecture up to n")
        print("  euler <n>         - Calculate Euler's totient function φ(n)")
        print("  collatz <n>       - Generate Collatz sequence for n")
        print("  crt <a1,n1,a2,n2> - Chinese Remainder Theorem solver")
        print("\n🎓 Proof System:")
        print("  theorem           - Show Fundamental Theorem of Arithmetic")
        print("\n🔣 Symbolic Mathematics:")
        print("  simplify <expr>   - Simplify mathematical expression")
        print("  expand <expr>     - Expand mathematical expression")
        print("  factor <expr>     - Factor mathematical expression")
        print("  solve <eq> [var]  - Solve equation for variable")
        print("  diff <expr> <var> - Differentiate expression")
        print("  integrate <expr> <var> - Integrate expression")
        print("  limit <expr> <var> <point> - Compute limit")
        print("  taylor <expr> <var> [point] [order] - Taylor series")
        print("  substitute <expr> <var=val> - Substitute values")
        print("\n📊 Visualization:")
        print("  plot <expr>       - Plot mathematical function")
        print("  plotseq <type> <n> - Plot sequence (fibonacci/primes)")
        print("  plotprimes <n>    - Plot prime distribution up to n")
        print("  plotcollatz <n1,n2,...> - Plot Collatz trajectories")
        print("  plotcomp <type1> <type2> <n> - Compare sequences")
        print("\n⏱️ Performance:")
        print("  benchmark         - Run quick performance benchmarks")
        print("  benchmark full    - Run comprehensive benchmark suite")
        print("\n❓ General:")
        print("  examples          - Show usage examples")
        print("  help              - Show this help")
        print("  quit/exit         - Exit the CLI\n")
    
    def _primes(self, args: List[str]) -> None:
        """Generate prime numbers."""
        if not args:
            print("Usage: primes <n>")
            print("Example: primes 50")
            return
        
        try:
            n = int(args[0])
            if n < 2:
                print("Please enter a number >= 2")
                return
                
            primes = sieve_of_eratosthenes(n)
            print(f"\n🔍 Prime numbers up to {n}:")
            print(f"   {primes}")
            print(f"   Found {len(primes)} primes\n")
            
        except ValueError:
            print("Please enter a valid integer.\n")
    
    def _fibonacci(self, args: List[str]) -> None:
        """Generate Fibonacci sequence."""
        if not args:
            print("Usage: fibonacci <n>")
            print("Example: fibonacci 10")
            return
        
        try:
            n = int(args[0])
            if n < 1:
                print("Please enter a positive number")
                return
                
            fib_seq = fibonacci_sequence(n)
            print(f"\n🌀 First {n} Fibonacci numbers:")
            print(f"   {fib_seq}")
            if n > 2:
                ratio = fib_seq[-1] / fib_seq[-2] if fib_seq[-2] != 0 else 0
                print(f"   Golden ratio approximation: {ratio:.6f}\n")
            else:
                print()
                
        except ValueError:
            print("Please enter a valid integer.\n")
    
    def _perfect_numbers(self, args: List[str]) -> None:
        """Find perfect numbers."""
        if not args:
            print("Usage: perfect <n>")
            print("Example: perfect 100")
            return
        
        try:
            n = int(args[0])
            if n < 1:
                print("Please enter a positive number")
                return
                
            perfect_nums = []
            for i in range(1, n + 1):
                if is_perfect_number(i):
                    perfect_nums.append(i)
            
            print(f"\n✨ Perfect numbers up to {n}:")
            if perfect_nums:
                print(f"   {perfect_nums}")
            else:
                print("   None found")
            print(f"   Found {len(perfect_nums)} perfect numbers\n")
            
        except ValueError:
            print("Please enter a valid integer.\n")
    
    def _twin_primes(self, args: List[str]) -> None:
        """Find twin prime pairs."""
        if not args:
            print("Usage: twins <n>")
            print("Example: twins 50")
            return
        
        try:
            n = int(args[0])
            if n < 3:
                print("Please enter a number >= 3")
                return
                
            twins = twin_primes(n)
            print(f"\n👯 Twin prime pairs up to {n}:")
            print(f"   {twins}")
            print(f"   Found {len(twins)} twin prime pairs\n")
            
        except ValueError:
            print("Please enter a valid integer.\n")
    
    def _goldbach(self, args: List[str]) -> None:
        """Verify Goldbach conjecture."""
        if not args:
            print("Usage: goldbach <n>")
            print("Example: goldbach 100")
            return
        
        try:
            n = int(args[0])
            if n < 4:
                print("Please enter a number >= 4")
                return
                
            result = verify_goldbach_conjecture(n)
            print(f"\n🔍 Goldbach conjecture verification up to {n}:")
            print(f"   Result: {'✅ Holds' if result else '❌ Fails'}")
            print("   (Every even integer > 2 can be expressed as sum of two primes)\n")
            
        except ValueError:
            print("Please enter a valid integer.\n")
    
    def _euler_totient(self, args: List[str]) -> None:
        """Calculate Euler's totient function."""
        if not args:
            print("Usage: euler <n>")
            print("Example: euler 12")
            return
        
        try:
            n = int(args[0])
            if n < 1:
                print("Please enter a positive number")
                return
                
            result = euler_totient(n)
            print(f"\n🔢 Euler's totient function φ({n}):")
            print(f"   φ({n}) = {result}")
            print(f"   (Count of integers ≤ {n} that are coprime to {n})\n")
            
        except ValueError:
            print("Please enter a valid integer.\n")
    
    def _collatz(self, args: List[str]) -> None:
        """Generate Collatz sequence."""
        if not args:
            print("Usage: collatz <n>")
            print("Example: collatz 7")
            return
        
        try:
            n = int(args[0])
            if n < 1:
                print("Please enter a positive number")
                return
                
            sequence = collatz_sequence(n)
            print(f"\n🎯 Collatz sequence for {n}:")
            print(f"   {sequence}")
            print(f"   Sequence length: {len(sequence)} steps\n")
            
        except ValueError:
            print("Please enter a valid integer.\n")
    
    def _chinese_remainder(self, args: List[str]) -> None:
        """Solve Chinese Remainder Theorem."""
        if not args:
            print("Usage: crt <a1,n1,a2,n2>")
            print("Example: crt 2,3,3,5")
            print("Solves: x ≡ a1 (mod n1) and x ≡ a2 (mod n2)")
            return
        
        try:
            params = args[0].split(',')
            if len(params) != 4:
                print("Please provide exactly 4 comma-separated values")
                return
                
            a1, n1, a2, n2 = map(int, params)
            result = NumberTheoryUtils.chinese_remainder_theorem([a1, a2], [n1, n2])
            
            print(f"\n🧮 Chinese Remainder Theorem:")
            print(f"   x ≡ {a1} (mod {n1})")
            print(f"   x ≡ {a2} (mod {n2})")
            print(f"   Solution: x ≡ {result} (mod {n1 * n2})\n")
            
        except ValueError:
            print("Please enter valid integers separated by commas.\n")
        except Exception as e:
            print(f"Error solving CRT: {e}\n")
    
    def _show_theorem(self, args: List[str]) -> None:
        """Display the Fundamental Theorem of Arithmetic."""
        theorem = create_fundamental_theorem_of_arithmetic()
        
        print(f"\n📜 {theorem.description}")
        print(f"\n🎓 Status: {'Proven ✅' if theorem.proven else 'Not proven ❌'}")
        
        if theorem.proof:
            print(f"\n📋 Proof Structure:")
            print(f"   • Axioms used: {len(theorem.proof.axioms)}")
            print(f"   • Proof steps: {len(theorem.proof.steps)}")
            print(f"   • Verification: {'Valid ✅' if theorem.proof.verify() else 'Invalid ❌'}")
            
            print(f"\n🔍 Axioms:")
            for i, axiom in enumerate(theorem.proof.axioms, 1):
                print(f"   {i}. {axiom.description}")
        print()
    
    def _show_examples(self, args: List[str]) -> None:
        """Show usage examples."""
        examples = [
            ("Find prime numbers", "primes 30"),
            ("Generate Fibonacci sequence", "fibonacci 8"),
            ("Check perfect numbers", "perfect 50"),
            ("Find twin primes", "twins 30"),
            ("Verify Goldbach conjecture", "goldbach 50"),
            ("Calculate Euler's totient", "euler 12"),
            ("Generate Collatz sequence", "collatz 7"),
            ("Solve Chinese Remainder", "crt 2,3,3,5"),
            ("View mathematical theorem", "theorem"),
            ("Simplify expression", "simplify (x+1)^2"),
            ("Expand expression", "expand (x+1)*(x-1)"),
            ("Factor expression", "factor x^2-1"),
            ("Solve equation", "solve x^2-4=0"),
            ("Differentiate function", "diff x^3+2*x^2 x"),
            ("Integrate function", "integrate 2*x+1 x"),
            ("Compute limit", "limit sin(x)/x x 0"),
            ("Taylor series", "taylor exp(x) x 0 5"),
        ]
        
        print("\n💡 Usage Examples:")
        print("-" * 40)
        for desc, cmd in examples:
            print(f"  {desc:.<30} {cmd}")
        print()
    
    def _quit(self, args: List[str]) -> None:
        """Exit the CLI."""
        print("\nGoodbye! Thanks for exploring mathematics! 👋\n")
        self.running = False
    
    # Symbolic Math Commands
    def _simplify(self, args: List[str]) -> None:
        """Simplify a mathematical expression."""
        if not args:
            print("Usage: simplify <expression>")
            print("Example: simplify (x+1)^2 - (x^2 + 2*x + 1)")
            return
        
        try:
            expr = ' '.join(args)
            result = SymbolicMath.simplify_expression(expr)
            print(f"\n🔧 Simplifying: {expr}")
            print(f"   Result: {result}\n")
        except Exception as e:
            print(f"Error simplifying expression: {e}\n")
    
    def _expand(self, args: List[str]) -> None:
        """Expand a mathematical expression."""
        if not args:
            print("Usage: expand <expression>")
            print("Example: expand (x+1)*(x-1)")
            return
        
        try:
            expr = ' '.join(args)
            result = SymbolicMath.expand_expression(expr)
            print(f"\n📈 Expanding: {expr}")
            print(f"   Result: {result}\n")
        except Exception as e:
            print(f"Error expanding expression: {e}\n")
    
    def _factor(self, args: List[str]) -> None:
        """Factor a mathematical expression."""
        if not args:
            print("Usage: factor <expression>")
            print("Example: factor x^2-1")
            return
        
        try:
            expr = ' '.join(args)
            result = SymbolicMath.factor_expression(expr)
            print(f"\n🔍 Factoring: {expr}")
            print(f"   Result: {result}\n")
        except Exception as e:
            print(f"Error factoring expression: {e}\n")
    
    def _solve(self, args: List[str]) -> None:
        """Solve an equation."""
        if not args:
            print("Usage: solve <equation> [variable]")
            print("Example: solve x^2-4=0")
            print("Example: solve x^2+y-4=0 x")
            return
        
        try:
            if len(args) == 1:
                equation = args[0]
                variable = None
            else:
                equation = args[0]
                variable = args[1]
            
            solutions = SymbolicMath.solve_equation(equation, variable)
            print(f"\n🎯 Solving: {equation}")
            if variable:
                print(f"   For variable: {variable}")
            print(f"   Solutions: {solutions}\n")
        except Exception as e:
            print(f"Error solving equation: {e}\n")
    
    def _differentiate(self, args: List[str]) -> None:
        """Differentiate an expression."""
        if len(args) < 2:
            print("Usage: diff <expression> <variable>")
            print("Example: diff x^3+2*x^2 x")
            return
        
        try:
            expr = args[0]
            variable = args[1]
            result = SymbolicMath.differentiate(expr, variable)
            print(f"\n📊 Differentiating: {expr}")
            print(f"   With respect to: {variable}")
            print(f"   Result: {result}\n")
        except Exception as e:
            print(f"Error differentiating expression: {e}\n")
    
    def _integrate(self, args: List[str]) -> None:
        """Integrate an expression."""
        if len(args) < 2:
            print("Usage: integrate <expression> <variable>")
            print("Example: integrate 2*x+1 x")
            return
        
        try:
            expr = args[0]
            variable = args[1]
            result = SymbolicMath.integrate(expr, variable)
            print(f"\n∫ Integrating: {expr}")
            print(f"   With respect to: {variable}")
            print(f"   Result: {result} + C\n")
        except Exception as e:
            print(f"Error integrating expression: {e}\n")
    
    def _limit(self, args: List[str]) -> None:
        """Compute a limit."""
        if len(args) < 3:
            print("Usage: limit <expression> <variable> <point>")
            print("Example: limit sin(x)/x x 0")
            print("Example: limit 1/x x oo")
            return
        
        try:
            expr = args[0]
            variable = args[1] 
            point = args[2]
            result = CalculusUtils.limit(expr, variable, point)
            print(f"\n🎯 Limit of: {expr}")
            print(f"   As {variable} approaches: {point}")
            print(f"   Result: {result}\n")
        except Exception as e:
            print(f"Error computing limit: {e}\n")
    
    def _taylor_series(self, args: List[str]) -> None:
        """Compute Taylor series."""
        if len(args) < 2:
            print("Usage: taylor <expression> <variable> [point] [order]")
            print("Example: taylor exp(x) x 0 5")
            print("Example: taylor sin(x) x")
            return
        
        try:
            expr = args[0]
            variable = args[1]
            point = float(args[2]) if len(args) > 2 else 0
            order = int(args[3]) if len(args) > 3 else 6
            
            result = CalculusUtils.taylor_series(expr, variable, point, order)
            print(f"\n📈 Taylor series of: {expr}")
            print(f"   Variable: {variable}")
            print(f"   Around point: {point}")
            print(f"   Order: {order}")
            print(f"   Result: {result}\n")
        except Exception as e:
            print(f"Error computing Taylor series: {e}\n")
    
    def _substitute(self, args: List[str]) -> None:
        """Substitute values into an expression."""
        if len(args) < 2:
            print("Usage: substitute <expression> <var=value> [var2=value2]")
            print("Example: substitute x^2+y x=2 y=3")
            return
        
        try:
            expr = args[0]
            substitutions: Dict[str, Any] = {}
            
            for sub in args[1:]:
                if '=' not in sub:
                    print(f"Invalid substitution format: {sub}")
                    return
                var, val = sub.split('=', 1)
                try:
                    substitutions[var.strip()] = float(val.strip())
                except ValueError:
                    # If it's not a number, treat as symbolic
                    substitutions[var.strip()] = val.strip()
            
            result = SymbolicMath.substitute(expr, substitutions)
            print(f"\n🔄 Substituting into: {expr}")
            for var, val in substitutions.items():
                print(f"   {var} = {val}")
            print(f"   Result: {result}\n")
        except Exception as e:
            print(f"Error substituting values: {e}\n")

    def _plot_function(self, args: List[str]) -> None:
        """Plot a mathematical function."""
        if not args:
            print("Usage: plot <expression>")
            print("Example: plot x**2")
            print("Example: plot sin(x)")
            return
        
        try:
            expression = ' '.join(args)
            print(f"\n📊 Plotting function: f(x) = {expression}")
            
            # Try to determine a good range based on the function
            x_range = (-10, 10)
            if any(func in expression for func in ['exp', 'log']):
                x_range = (-5, 5)
            elif 'tan' in expression:
                x_range = (-3, 3)
            
            success = self.visualizer.plot_function(
                expression, 
                x_range=x_range,
                title=f"Graph of f(x) = {expression}"
            )
            
            if success:
                print("✅ Plot displayed successfully!")
            else:
                print("❌ Failed to create plot")
                
        except Exception as e:
            print(f"Error plotting function: {e}\n")

    def _plot_sequence(self, args: List[str]) -> None:
        """Plot a mathematical sequence."""
        if len(args) < 2:
            print("Usage: plotseq <type> <n>")
            print("Types: fibonacci, primes")
            print("Example: plotseq fibonacci 10")
            return
        
        try:
            seq_type = args[0].lower()
            n = int(args[1])
            
            if seq_type == 'fibonacci':
                sequence = fibonacci_sequence(n)
                title = f"First {n} Fibonacci Numbers"
            elif seq_type == 'primes':
                primes = sieve_of_eratosthenes(n)
                sequence = primes[:min(20, len(primes))]  # Limit to first 20 for visibility
                title = f"Prime Numbers up to {n}"
            else:
                print(f"Unknown sequence type: {seq_type}")
                return
            
            print(f"\n📊 Plotting {seq_type} sequence...")
            success = self.visualizer.plot_sequence(
                [float(x) for x in sequence],
                title=title
            )
            
            if success:
                print("✅ Sequence plot displayed successfully!")
            else:
                print("❌ Failed to create sequence plot")
                
        except ValueError:
            print("Error: Invalid number format\n")
        except Exception as e:
            print(f"Error plotting sequence: {e}\n")

    def _plot_primes(self, args: List[str]) -> None:
        """Plot prime number distribution."""
        if not args:
            print("Usage: plotprimes <n>")
            print("Example: plotprimes 100")
            return
        
        try:
            n = int(args[0])
            if n < 2:
                print("Number must be at least 2")
                return
            
            print(f"\n📊 Plotting prime distribution up to {n}...")
            primes = sieve_of_eratosthenes(n)
            
            success = self.visualizer.plot_prime_distribution(primes, n)
            
            if success:
                print("✅ Prime distribution plot displayed successfully!")
                print(f"   Found {len(primes)} primes up to {n}")
            else:
                print("❌ Failed to create prime distribution plot")
                
        except ValueError:
            print("Error: Invalid number format\n")
        except Exception as e:
            print(f"Error plotting primes: {e}\n")

    def _plot_collatz(self, args: List[str]) -> None:
        """Plot Collatz sequence trajectories."""
        if not args:
            print("Usage: plotcollatz <n1,n2,n3,...>")
            print("Example: plotcollatz 3,7,15,27")
            return
        
        try:
            # Parse comma-separated numbers
            numbers_str = ' '.join(args)
            numbers = [int(x.strip()) for x in numbers_str.split(',')]
            
            if len(numbers) > 6:
                numbers = numbers[:6]  # Limit to 6 sequences for readability
                print("Note: Limited to first 6 numbers for better visualization")
            
            print(f"\n📊 Plotting Collatz sequences for: {numbers}")
            
            sequences = []
            for num in numbers:
                if num > 0:
                    seq = collatz_sequence(num)
                    sequences.append(seq)
            
            if not sequences:
                print("No valid positive numbers provided")
                return
            
            success = self.visualizer.plot_collatz_trajectory(sequences, numbers)
            
            if success:
                print("✅ Collatz trajectories displayed successfully!")
            else:
                print("❌ Failed to create Collatz plot")
                
        except ValueError:
            print("Error: Invalid number format. Use comma-separated positive integers\n")
        except Exception as e:
            print(f"Error plotting Collatz sequences: {e}\n")

    def _plot_comparative(self, args: List[str]) -> None:
        """Plot comparative sequences."""
        if len(args) < 3:
            print("Usage: plotcomp <type1> <type2> <n>")
            print("Types: fibonacci, primes, collatz, euler")
            print("Example: plotcomp fibonacci primes 10")
            return
        
        try:
            type1, type2 = args[0].lower(), args[1].lower()
            n = int(args[2])
            
            sequences = {}
            
            # Generate sequences based on types
            for seq_type in [type1, type2]:
                if seq_type == 'fibonacci':
                    sequences['Fibonacci'] = [float(x) for x in fibonacci_sequence(min(n, 15))]
                elif seq_type == 'primes':
                    primes = sieve_of_eratosthenes(n * 10)  # Get more primes
                    sequences['Primes'] = [float(x) for x in primes[:min(n, 15)]]
                elif seq_type == 'euler':
                    sequences['Euler φ(n)'] = [float(euler_totient(i)) for i in range(1, min(n, 15) + 1)]
                elif seq_type == 'collatz':
                    # Use length of Collatz sequences
                    sequences['Collatz Steps'] = [float(len(collatz_sequence(i))) for i in range(1, min(n, 15) + 1)]
                else:
                    print(f"Unknown sequence type: {seq_type}")
                    return
            
            if len(sequences) < 2:
                print("Need two different sequence types")
                return
            
            print(f"\n📊 Comparing {type1} vs {type2} sequences...")
            success = self.visualizer.plot_comparative_sequences(
                sequences,
                title=f"Comparison: {type1.title()} vs {type2.title()}"
            )
            
            if success:
                print("✅ Comparative plot displayed successfully!")
            else:
                print("❌ Failed to create comparative plot")
                
        except ValueError:
            print("Error: Invalid number format\n")
        except Exception as e:
            print(f"Error plotting comparative sequences: {e}\n")
    
    def _benchmark(self, args: List[str]) -> None:
        """Run performance benchmarks."""
        if args and args[0] == 'full':
            print("\n⏱️ Running comprehensive performance benchmarks...")
            print("This may take a moment...\n")
            try:
                benchmark = run_performance_analysis()
                print("\n📊 Benchmark completed successfully!")
                print("Report saved to performance_report.txt")
                print("Performance plots saved to math_plots/")
            except Exception as e:
                print(f"❌ Benchmark failed: {e}")
        else:
            print("\n⏱️ Running quick performance benchmarks...")
            try:
                benchmark = PerformanceBenchmark()
                
                # Run a small subset of benchmarks
                print("Testing prime generation...")
                benchmark.time_function(sieve_of_eratosthenes, 1000, iterations=3)
                
                print("Testing Fibonacci sequence...")
                benchmark.time_function(fibonacci_sequence, 100, iterations=3)
                
                print("Testing GCD calculations...")
                benchmark.time_function(lambda: [gcd(i, 100) for i in range(1, 51)], iterations=5)
                
                print("\n📈 Quick Benchmark Results:")
                print(benchmark.generate_performance_report())
                
            except Exception as e:
                print(f"❌ Benchmark failed: {e}")


def main() -> None:
    """Entry point for the CLI."""
    cli = EternalMathCLI()
    cli.run()


if __name__ == "__main__":
    main()
