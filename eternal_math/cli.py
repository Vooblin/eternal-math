"""
Interactive Command Line Interface for Eternal Math

This module provides an interactive CLI for exploring mathematical concepts,
running calculations, and examining proofs.
"""

from typing import List
from eternal_math import (
    sieve_of_eratosthenes, fibonacci_sequence, is_perfect_number,
    twin_primes, verify_goldbach_conjecture, euler_totient,
    collatz_sequence, NumberTheoryUtils,
    create_fundamental_theorem_of_arithmetic
)


class EternalMathCLI:
    """Interactive CLI for Eternal Math exploration."""
    
    def __init__(self):
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
            'quit': self._quit,
            'exit': self._quit,
        }
        self.running = True
    
    def run(self):
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
    
    def _help(self, args: List[str]):
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
        print("\n❓ General:")
        print("  examples          - Show usage examples")
        print("  help              - Show this help")
        print("  quit/exit         - Exit the CLI\n")
    
    def _primes(self, args: List[str]):
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
    
    def _fibonacci(self, args: List[str]):
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
    
    def _perfect_numbers(self, args: List[str]):
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
    
    def _twin_primes(self, args: List[str]):
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
    
    def _goldbach(self, args: List[str]):
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
    
    def _euler_totient(self, args: List[str]):
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
    
    def _collatz(self, args: List[str]):
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
    
    def _chinese_remainder(self, args: List[str]):
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
    
    def _show_theorem(self, args: List[str]):
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
    
    def _show_examples(self, args: List[str]):
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
        ]
        
        print("\n💡 Usage Examples:")
        print("-" * 40)
        for desc, cmd in examples:
            print(f"  {desc:.<30} {cmd}")
        print()
    
    def _quit(self, args: List[str]):
        """Exit the CLI."""
        print("\nGoodbye! Thanks for exploring mathematics! 👋\n")
        self.running = False


def main():
    """Entry point for the CLI."""
    cli = EternalMathCLI()
    cli.run()


if __name__ == "__main__":
    main()
