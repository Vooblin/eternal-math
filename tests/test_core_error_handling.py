"""
Tests for error handling in the core module.
"""

import pytest

from eternal_math.core import Function, Set, gcd, is_prime, lcm, prime_factorization


class TestGcdErrorHandling:
    """Test error handling for GCD function."""

    def test_gcd_type_error_first_arg(self) -> None:
        """Test that GCD raises TypeError for non-integer first argument."""
        with pytest.raises(TypeError, match="Both arguments must be integers"):
            gcd("a", 5)  # type: ignore

    def test_gcd_type_error_second_arg(self) -> None:
        """Test that GCD raises TypeError for non-integer second argument."""
        with pytest.raises(TypeError, match="Both arguments must be integers"):
            gcd(5, "b")  # type: ignore

    def test_gcd_type_error_both_args(self) -> None:
        """Test that GCD raises TypeError for non-integer arguments."""
        with pytest.raises(TypeError, match="Both arguments must be integers"):
            gcd("a", "b")  # type: ignore

    def test_gcd_value_error_both_zero(self) -> None:
        """Test that GCD raises ValueError when both arguments are zero."""
        with pytest.raises(
            ValueError, match="GCD is undefined when both arguments are zero"
        ):
            gcd(0, 0)

    def test_gcd_valid_with_one_zero(self) -> None:
        """Test that GCD works correctly with one zero argument."""
        assert gcd(0, 5) == 5
        assert gcd(7, 0) == 7


class TestLcmErrorHandling:
    """Test error handling for LCM function."""

    def test_lcm_type_error_first_arg(self) -> None:
        """Test that LCM raises TypeError for non-integer first argument."""
        with pytest.raises(TypeError, match="Both arguments must be integers"):
            lcm("a", 5)  # type: ignore

    def test_lcm_type_error_second_arg(self) -> None:
        """Test that LCM raises TypeError for non-integer second argument."""
        with pytest.raises(TypeError, match="Both arguments must be integers"):
            lcm(5, "b")  # type: ignore


class TestIsPrimeErrorHandling:
    """Test error handling for is_prime function."""

    def test_is_prime_type_error(self) -> None:
        """Test that is_prime raises TypeError for non-integer argument."""
        with pytest.raises(TypeError, match="Argument must be an integer"):
            is_prime("5")  # type: ignore

    def test_is_prime_type_error_float(self) -> None:
        """Test that is_prime raises TypeError for float argument."""
        with pytest.raises(TypeError, match="Argument must be an integer"):
            is_prime(5.0)  # type: ignore


class TestPrimeFactorizationErrorHandling:
    """Test error handling for prime_factorization function."""

    def test_prime_factorization_type_error(self) -> None:
        """Test that prime_factorization raises TypeError for non-integer argument."""
        with pytest.raises(TypeError, match="Argument must be an integer"):
            prime_factorization("10")  # type: ignore

    def test_prime_factorization_value_error_negative(self) -> None:
        """Test that prime_factorization raises ValueError for negative numbers."""
        with pytest.raises(
            ValueError, match="Prime factorization is only defined for integers >= 2"
        ):
            prime_factorization(-5)

    def test_prime_factorization_value_error_zero(self) -> None:
        """Test that prime_factorization raises ValueError for zero."""
        with pytest.raises(
            ValueError, match="Prime factorization is only defined for integers >= 2"
        ):
            prime_factorization(0)

    def test_prime_factorization_value_error_one(self) -> None:
        """Test that prime_factorization raises ValueError for one."""
        with pytest.raises(
            ValueError, match="Prime factorization is only defined for integers >= 2"
        ):
            prime_factorization(1)


class TestSetErrorHandling:
    """Test error handling for Set class."""

    def test_set_init_invalid_elements_type(self) -> None:
        """Test that Set raises TypeError for invalid elements type."""
        with pytest.raises(TypeError, match="Elements must be a list"):
            Set("invalid")  # type: ignore

    def test_set_init_valid_types(self) -> None:
        """Test that Set accepts valid element types."""
        # Should not raise any exceptions
        Set([1, 2, 3])  # list
        Set()  # empty/None

    def test_set_union_type_error(self) -> None:
        """Test that Set.union raises TypeError for non-Set argument."""
        s = Set([1, 2, 3])
        with pytest.raises(TypeError, match="Argument must be a Set instance"):
            s.union([4, 5, 6])  # type: ignore

    def test_set_intersection_type_error(self) -> None:
        """Test that Set.intersection raises TypeError for non-Set argument."""
        s = Set([1, 2, 3])
        with pytest.raises(TypeError, match="Argument must be a Set instance"):
            s.intersection([2, 3, 4])  # type: ignore

    def test_set_difference_type_error(self) -> None:
        """Test that Set.difference raises TypeError for non-Set argument."""
        s = Set([1, 2, 3])
        with pytest.raises(TypeError, match="Argument must be a Set instance"):
            s.difference([2, 3])  # type: ignore


class TestFunctionErrorHandling:
    """Test error handling for Function class."""

    def test_function_init_non_callable(self) -> None:
        """Test that Function raises TypeError for non-callable func argument."""
        with pytest.raises(TypeError, match="func must be callable"):
            Function("not_callable")  # type: ignore

    def test_function_compose_type_error(self) -> None:
        """Test that Function.compose raises TypeError for non-Function argument."""
        f = Function(lambda x: x * 2)
        with pytest.raises(TypeError, match="Argument must be a Function instance"):
            f.compose("not_a_function")  # type: ignore

    def test_function_valid_initialization(self) -> None:
        """Test that Function can be initialized with valid callable."""
        # Should not raise any exceptions
        Function(lambda x: x * 2)
        Function(abs)  # built-in function

        def custom_func(x: int) -> int:
            return x + 1

        Function(custom_func)  # custom function
