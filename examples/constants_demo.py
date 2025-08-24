#!/usr/bin/env python3
"""
Mathematical Constants Demo

This example demonstrates the use of mathematical constants provided
by the Eternal Math library in practical calculations.
"""

import math

from eternal_math import constants


def circle_calculations(radius: float) -> None:
    """Demonstrate circle calculations using π and τ."""
    print(f"\n=== Circle with radius {radius} ===")

    # Area using π
    area = constants.PI * radius**2
    print(f"Area (π·r²): {area:.6f}")

    # Circumference using τ (tau = 2π)
    circumference = constants.TAU * radius
    print(f"Circumference (τ·r): {circumference:.6f}")

    # Verify τ = 2π relationship
    print(f"Verification: 2π·r = {2 * constants.PI * radius:.6f}")


def compound_interest_demo() -> None:
    """Demonstrate compound interest using Euler's number."""
    print(f"\n=== Compound Interest (using e = {constants.E:.6f}) ===")

    principal = 1000.0
    rate = 0.05  # 5% annual interest
    time = 10  # 10 years

    # Continuous compounding: A = P * e^(rt)
    amount_continuous = principal * math.exp(rate * time)
    print(f"Principal: ${principal:.2f}")
    print(f"Rate: {rate*100}% annually")
    print(f"Time: {time} years")
    print(f"Continuous compounding: ${amount_continuous:.2f}")

    # Compare with manual calculation using constants.E
    manual_calc = principal * (constants.E ** (rate * time))
    print(f"Using constants.E: ${manual_calc:.2f}")


def golden_ratio_applications() -> None:
    """Demonstrate golden ratio applications."""
    print(f"\n=== Golden Ratio (φ = {constants.PHI:.6f}) ===")

    # Golden rectangle dimensions
    width = 10.0
    height = width * constants.PHI
    print(f"Golden rectangle: {width:.1f} × {height:.6f}")

    # Fibonacci ratio approximation
    fib_sequence = [1, 1]
    for i in range(2, 15):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    print("\nFibonacci sequence ratios approaching φ:")
    for i in range(10, 14):
        ratio = fib_sequence[i] / fib_sequence[i - 1]
        difference = abs(ratio - constants.PHI)
        print(f"F({i})/F({i-1}) = {ratio:.8f}, diff from φ: {difference:.8f}")

    # Golden ratio properties
    print("\nGolden ratio properties:")
    print(f"φ² = φ + 1: {constants.PHI**2:.6f} = {constants.PHI + 1:.6f}")
    print(f"φ × (1/φ) = 1: {constants.PHI * constants.PHI_INVERSE:.10f}")


def logarithm_demonstrations() -> None:
    """Demonstrate logarithmic calculations."""
    print("\n=== Logarithms ===")

    print(f"ln(2) = {constants.LN_2:.6f}")
    print(f"ln(10) = {constants.LN_10:.6f}")

    # Verify exponential relationships
    print("\nExponential verification:")
    print(f"e^(ln(2)) = {math.exp(constants.LN_2):.6f} (should be 2)")
    print(f"e^(ln(10)) = {math.exp(constants.LN_10):.6f} (should be 10)")

    # Change of base formula: log_a(x) = ln(x) / ln(a)
    x = 1024
    log_result = math.log(x) / constants.LN_2
    print(f"\nChange of base: log₂({x}) = ln({x})/ln(2) = {log_result:.1f}")
    print(f"Verification: 2^{log_result:.1f} = {2**log_result:.1f}")


def trigonometric_examples() -> None:
    """Demonstrate trigonometric calculations with π and τ."""
    print("\n=== Trigonometry with π and τ ===")

    # Unit circle: full rotation = τ radians = 2π radians
    print(f"Full circle: τ = 2π = {constants.TAU:.6f} radians")
    print(f"Half circle: π = {constants.PI:.6f} radians")
    print(f"Quarter circle: π/2 = {constants.PI/2:.6f} radians")

    # Common angles
    angles_in_pi: list[float] = [0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]
    print("\nTrigonometric values (using multiples of π):")
    print(f"{'Angle (π)':>10} {'Radians':>10} {'sin':>8} {'cos':>8}")
    print("-" * 40)

    for mult in angles_in_pi:
        angle_rad = mult * constants.PI
        sin_val = math.sin(angle_rad)
        cos_val = math.cos(angle_rad)
        print(f"{mult:>8.2f}π {angle_rad:>10.4f} {sin_val:>8.4f} {cos_val:>8.4f}")


def precision_comparisons() -> None:
    """Compare constant precision with math module."""
    print("\n=== Precision Comparisons ===")

    constants_vs_math = [
        ("π", constants.PI, math.pi),
        ("e", constants.E, math.e),
        ("√2", constants.SQRT_2, math.sqrt(2)),
        ("√3", constants.SQRT_3, math.sqrt(3)),
        ("ln(2)", constants.LN_2, math.log(2)),
        ("ln(10)", constants.LN_10, math.log(10)),
    ]

    print(
        f"{'Constant':>8} {'eternal_math':>20} {'math module':>20} {'Difference':>15}"
    )
    print("-" * 70)

    for name, eternal_val, math_val in constants_vs_math:
        diff = abs(eternal_val - math_val)
        print(f"{name:>8} {eternal_val:>20.15f} {math_val:>20.15f} {diff:>15e}")


def main() -> None:
    """Run all mathematical constants demonstrations."""
    print("Mathematical Constants Demonstration")
    print("=" * 50)

    # Run all demonstrations
    circle_calculations(5.0)
    compound_interest_demo()
    golden_ratio_applications()
    logarithm_demonstrations()
    trigonometric_examples()
    precision_comparisons()

    print(f"\n{'='*50}")
    print("All constants available in eternal_math.constants:")
    print("PI, E, TAU, PHI, PHI_INVERSE, GAMMA, SQRT_2, SQRT_3, SQRT_5")
    print("LN_2, LN_10, INFINITY, NEG_INFINITY")


if __name__ == "__main__":
    main()
