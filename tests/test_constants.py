"""
Test module for mathematical constants.
"""

import math

from eternal_math.core import Constants, constants


class TestConstants:
    """Test mathematical constants."""

    def test_basic_constants(self) -> None:
        """Test basic mathematical constants."""
        # Test π
        assert abs(constants.PI - math.pi) < 1e-15
        assert abs(Constants.PI - math.pi) < 1e-15

        # Test e
        assert abs(constants.E - math.e) < 1e-15
        assert abs(Constants.E - math.e) < 1e-15

        # Test τ (tau) = 2π
        assert abs(constants.TAU - 2 * math.pi) < 1e-15
        assert constants.TAU == 2 * constants.PI

    def test_golden_ratio(self) -> None:
        """Test golden ratio and related constants."""
        # Test φ (golden ratio)
        expected_phi = (1 + math.sqrt(5)) / 2
        assert abs(constants.PHI - expected_phi) < 1e-15

        # Test 1/φ
        expected_phi_inv = 2 / (1 + math.sqrt(5))
        assert abs(constants.PHI_INVERSE - expected_phi_inv) < 1e-15

        # Test mathematical relationship: φ * (1/φ) = 1
        assert abs(constants.PHI * constants.PHI_INVERSE - 1) < 1e-15

        # Test golden ratio property: φ² = φ + 1
        assert abs(constants.PHI**2 - (constants.PHI + 1)) < 1e-15

    def test_euler_mascheroni_constant(self) -> None:
        """Test Euler-Mascheroni constant."""
        # Verify it's approximately 0.5772...
        assert 0.577 < constants.GAMMA < 0.578
        assert abs(constants.GAMMA - 0.5772156649015329) < 1e-15

    def test_square_roots(self) -> None:
        """Test square root constants."""
        assert abs(constants.SQRT_2 - math.sqrt(2)) < 1e-15
        assert abs(constants.SQRT_3 - math.sqrt(3)) < 1e-15
        assert abs(constants.SQRT_5 - math.sqrt(5)) < 1e-15

        # Verify they are indeed square roots
        assert abs(constants.SQRT_2**2 - 2) < 1e-15
        assert abs(constants.SQRT_3**2 - 3) < 1e-15
        assert abs(constants.SQRT_5**2 - 5) < 1e-15

    def test_logarithms(self) -> None:
        """Test natural logarithm constants."""
        assert abs(constants.LN_2 - math.log(2)) < 1e-15
        assert abs(constants.LN_10 - math.log(10)) < 1e-15

        # Verify exponential relationships (use slightly looser tolerance for
        # floating-point precision)
        assert abs(math.exp(constants.LN_2) - 2) < 1e-14
        assert abs(math.exp(constants.LN_10) - 10) < 1e-14

    def test_infinity_constants(self) -> None:
        """Test infinity constants."""
        assert constants.INFINITY == float("inf")
        assert constants.NEG_INFINITY == float("-inf")

        # Test infinity properties
        assert constants.INFINITY > 1e100
        assert constants.NEG_INFINITY < -1e100
        assert constants.INFINITY + 1 == constants.INFINITY
        assert constants.NEG_INFINITY - 1 == constants.NEG_INFINITY

    def test_constants_immutability(self) -> None:
        """Test that constants are properly defined as class attributes."""
        # These should not raise errors
        assert hasattr(Constants, "PI")
        assert hasattr(Constants, "E")
        assert hasattr(Constants, "PHI")
        assert hasattr(Constants, "GAMMA")

        # Test global constants instance
        assert isinstance(constants, Constants)

    def test_mathematical_relationships(self) -> None:
        """Test mathematical relationships between constants."""
        # Euler's identity components: e^(iπ) + 1 = 0
        # We can't test complex numbers directly, but we can test related values

        # Test that π is the ratio of circumference to diameter
        # For a unit circle: circumference = 2π * radius = 2π * 1 = 2π = τ
        assert constants.TAU == 2 * constants.PI

        # Test logarithm base conversions
        # ln(10) / ln(2) should equal log₂(10)
        log2_10 = constants.LN_10 / constants.LN_2
        assert abs(log2_10 - math.log2(10)) < 1e-15

    def test_precision_and_accuracy(self) -> None:
        """Test that constants have appropriate precision."""
        # All constants should have at least 15 decimal places of accuracy
        assert abs(constants.PI - 3.141592653589793) < 1e-15
        assert abs(constants.E - 2.718281828459045) < 1e-15
        assert abs(constants.PHI - 1.618033988749895) < 1e-15

    def test_constants_in_calculations(self) -> None:
        """Test using constants in mathematical calculations."""
        # Area of unit circle: π * r² = π * 1² = π
        unit_circle_area = constants.PI * 1**2
        assert abs(unit_circle_area - constants.PI) < 1e-15

        # Compound interest: A = P * e^(rt) for continuous compounding
        # For P=1, r=1, t=1: A = e
        compound_result = 1 * math.exp(1 * 1)
        assert abs(compound_result - constants.E) < 1e-15

        # Golden rectangle ratio
        golden_rect_ratio = (1 + constants.SQRT_5) / 2
        assert abs(golden_rect_ratio - constants.PHI) < 1e-15


if __name__ == "__main__":
    # Run tests manually if pytest is not available
    test_instance = TestConstants()
    test_instance.test_basic_constants()
    test_instance.test_golden_ratio()
    test_instance.test_euler_mascheroni_constant()
    test_instance.test_square_roots()
    test_instance.test_logarithms()
    test_instance.test_infinity_constants()
    test_instance.test_constants_immutability()
    test_instance.test_mathematical_relationships()
    test_instance.test_precision_and_accuracy()
    test_instance.test_constants_in_calculations()
    print("All constants tests passed!")
