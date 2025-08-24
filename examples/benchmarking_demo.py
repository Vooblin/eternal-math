"""
Example: Performance Benchmarking with Eternal Math

This example demonstrates how to use the benchmarking system to analyze
the performance of mathematical algorithms.
"""

from eternal_math import (
    PerformanceBenchmark,
    fibonacci_sequence,
    gcd,
    is_prime,
    run_performance_analysis,
    sieve_of_eratosthenes,
)


def main():
    """Demonstrate benchmarking capabilities."""
    print("=== Eternal Math: Performance Benchmarking Demo ===\n")

    # Create a benchmark instance
    benchmark = PerformanceBenchmark()

    # Example 1: Benchmark a single function
    print("1. Benchmarking Sieve of Eratosthenes:")
    result = benchmark.time_function(sieve_of_eratosthenes, 10000, iterations=5)
    print(f"   Function: {result.function_name}")
    print(f"   Input size: {result.input_size}")
    print(f"   Mean execution time: {result.mean_time:.4f} seconds")
    print(f"   Standard deviation: {result.std_dev:.4f} seconds")
    print(f"   Iterations: {result.iterations}\n")

    # Example 2: Benchmark Fibonacci sequence generation
    print("2. Benchmarking Fibonacci Sequence Generation:")
    fib_sizes = [50, 100, 200, 500]
    for size in fib_sizes:
        result = benchmark.time_function(fibonacci_sequence, size, iterations=10)
        print(f"   Size {size:3d}: {result.mean_time:.6f}s ± {result.std_dev:.6f}s")
    print()

    # Example 3: Compare GCD performance with different input sizes
    print("3. Benchmarking GCD Algorithm:")
    gcd_tests = [(12, 18), (144, 89), (12345, 67890), (999999, 123456789)]

    for a, b in gcd_tests:
        result = benchmark.time_function(gcd, a, b, iterations=1000)
        print(f"   GCD({a:>9}, {b:>9}): {result.mean_time:.8f}s")
    print()

    # Example 4: Benchmark prime checking
    print("4. Benchmarking Prime Checking:")
    test_primes = [97, 997, 9973, 99991]

    for prime in test_primes:
        result = benchmark.time_function(is_prime, prime, iterations=100)
        print(f"   is_prime({prime:>5}): {result.mean_time:.8f}s")
    print()

    # Example 5: Generate a performance report
    print("5. Performance Report:")
    print("-" * 50)
    report = benchmark.generate_performance_report()
    print(report)

    # Example 6: Run algorithm comparison benchmarks
    print("6. Running Algorithm Comparison Benchmarks:")
    try:
        prime_results = benchmark.benchmark_prime_algorithms([100, 1000, 5000])
        print("   Prime algorithm benchmarks completed!")

        fib_results = benchmark.benchmark_fibonacci_algorithms([10, 50, 100])
        print("   Fibonacci algorithm benchmarks completed!")

    except Exception as e:
        print(f"   Error running comparison benchmarks: {e}")

    # Example 7: Demonstrate comprehensive benchmark suite
    print("\n7. Would you like to run the comprehensive benchmark suite?")
    print("   This includes detailed performance analysis and visualization.")
    print("   (This may take a moment and will create performance plots)")

    response = input("   Run comprehensive benchmarks? (y/N): ").strip().lower()

    if response == "y" or response == "yes":
        print("\n🔄 Running comprehensive benchmark suite...")
        try:
            full_benchmark = run_performance_analysis()
            print("✅ Comprehensive benchmarks completed!")
            print("📊 Check 'performance_report.txt' for detailed results")
            print("📈 Check 'math_plots/' directory for performance visualizations")
        except Exception as e:
            print(f"❌ Comprehensive benchmark failed: {e}")
    else:
        print("   Skipping comprehensive benchmarks.")

    print("\n=== Benchmarking Demo Complete ===")
    print("💡 Tips:")
    print("   - Use benchmarking to identify performance bottlenecks")
    print("   - Compare different algorithms for the same problem")
    print("   - Monitor performance changes as you optimize code")
    print("   - Use iterations parameter to get more accurate timing")


if __name__ == "__main__":
    main()
