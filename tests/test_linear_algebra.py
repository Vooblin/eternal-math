"""
Tests for linear algebra module.
"""

from typing import List, Union

import pytest
import sympy as sp
from sympy import Matrix

from eternal_math.linear_algebra import LinearAlgebra, MatrixOperations, Vector


class TestVector:
    """Test the Vector class."""

    def test_vector_creation(self) -> None:
        """Test vector creation and basic properties."""
        v = Vector([1, 2, 3])
        assert len(v) == 3
        assert v.dimension == 3
        assert v[0] == 1
        assert v[1] == 2
        assert v[2] == 3

    def test_vector_creation_empty(self) -> None:
        """Test that empty vector raises ValueError."""
        with pytest.raises(ValueError, match="Vector must have at least one component"):
            Vector([])

    def test_vector_addition(self) -> None:
        """Test vector addition."""
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        result = v1 + v2
        assert result.components == [5, 7, 9]

    def test_vector_addition_different_dimensions(self) -> None:
        """Test vector addition with different dimensions."""
        v1 = Vector([1, 2])
        v2 = Vector([3, 4, 5])
        with pytest.raises(
            ValueError, match="Vectors must have same dimension for addition"
        ):
            v1 + v2

    def test_vector_subtraction(self) -> None:
        """Test vector subtraction."""
        v1 = Vector([5, 7, 9])
        v2 = Vector([1, 2, 3])
        result = v1 - v2
        assert result.components == [4, 5, 6]

    def test_vector_scalar_multiplication(self) -> None:
        """Test scalar multiplication."""
        v = Vector([1, 2, 3])
        result = 2 * v
        assert result.components == [2, 4, 6]

        result2 = v * 3
        assert result2.components == [3, 6, 9]

    def test_vector_dot_product(self) -> None:
        """Test dot product."""
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        result = v1.dot(v2)
        assert result == 32  # 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32

    def test_vector_cross_product(self) -> None:
        """Test cross product for 3D vectors."""
        v1 = Vector([1, 0, 0])
        v2 = Vector([0, 1, 0])
        result = v1.cross(v2)
        assert result.components == [0, 0, 1]

    def test_vector_cross_product_invalid_dimension(self) -> None:
        """Test cross product with non-3D vectors."""
        v1 = Vector([1, 2])
        v2 = Vector([3, 4])
        with pytest.raises(
            ValueError, match="Cross product is only defined for 3D vectors"
        ):
            v1.cross(v2)

    def test_vector_magnitude(self) -> None:
        """Test vector magnitude computation."""
        v = Vector([3, 4])
        assert v.magnitude() == 5  # sqrt(3^2 + 4^2) = 5

    def test_vector_normalize(self) -> None:
        """Test vector normalization."""
        v = Vector([3, 4])
        normalized = v.normalize()
        # Unit vector should have magnitude 1
        assert abs(float(normalized.magnitude()) - 1) < 1e-10

    def test_vector_normalize_zero_vector(self) -> None:
        """Test normalizing zero vector raises error."""
        v = Vector([0, 0, 0])
        with pytest.raises(ValueError, match="Cannot normalize zero vector"):
            v.normalize()

    def test_vector_to_sympy_matrix(self) -> None:
        """Test conversion to SymPy Matrix."""
        v = Vector([1, 2, 3])
        matrix = v.to_sympy_matrix()
        expected = Matrix([1, 2, 3])
        assert matrix == expected


class TestMatrixOperations:
    """Test the MatrixOperations class."""

    def test_create_matrix(self) -> None:
        """Test matrix creation."""
        data: List[List[Union[int, float, sp.Expr]]] = [[1, 2], [3, 4]]
        matrix = MatrixOperations.create_matrix(data)
        expected = Matrix([[1, 2], [3, 4]])
        assert matrix == expected

    def test_create_matrix_empty(self) -> None:
        """Test creating empty matrix raises error."""
        with pytest.raises(ValueError, match="Matrix data cannot be empty"):
            MatrixOperations.create_matrix([])

    def test_create_matrix_uneven_rows(self) -> None:
        """Test creating matrix with uneven rows."""
        data: List[List[Union[int, float, sp.Expr]]] = [[1, 2], [3, 4, 5]]
        with pytest.raises(ValueError, match="All rows must have the same length"):
            MatrixOperations.create_matrix(data)

    def test_identity_matrix(self) -> None:
        """Test identity matrix creation."""
        identity = MatrixOperations.identity_matrix(3)
        expected = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        assert identity == expected

    def test_zero_matrix(self) -> None:
        """Test zero matrix creation."""
        zero_mat = MatrixOperations.zero_matrix(2, 3)
        expected = Matrix([[0, 0, 0], [0, 0, 0]])
        assert zero_mat == expected

    def test_transpose(self) -> None:
        """Test matrix transpose."""
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        transposed = MatrixOperations.transpose(matrix)
        expected = Matrix([[1, 4], [2, 5], [3, 6]])
        assert transposed == expected

    def test_determinant(self) -> None:
        """Test matrix determinant."""
        matrix = Matrix([[1, 2], [3, 4]])
        det = MatrixOperations.determinant(matrix)
        assert det == -2  # 1*4 - 2*3 = -2

    def test_determinant_non_square(self) -> None:
        """Test determinant of non-square matrix raises error."""
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        with pytest.raises(
            ValueError, match="Determinant is only defined for square matrices"
        ):
            MatrixOperations.determinant(matrix)

    def test_inverse(self) -> None:
        """Test matrix inverse."""
        matrix = Matrix([[1, 2], [3, 4]])
        inverse = MatrixOperations.inverse(matrix)
        # Check that A * A^-1 = I
        identity = matrix * inverse
        expected_identity = Matrix([[1, 0], [0, 1]])
        # Use simplify to handle floating point precision
        simplified_identity = sp.simplify(identity)
        assert simplified_identity == expected_identity

    def test_inverse_singular_matrix(self) -> None:
        """Test inverse of singular matrix raises error."""
        matrix = Matrix([[1, 2], [2, 4]])  # Determinant is 0
        with pytest.raises(ValueError, match="Matrix is singular"):
            MatrixOperations.inverse(matrix)

    def test_rank(self) -> None:
        """Test matrix rank computation."""
        matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        rank = MatrixOperations.rank(matrix)
        assert rank == 2  # This matrix has rank 2

    def test_trace(self) -> None:
        """Test matrix trace computation."""
        matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        trace = MatrixOperations.trace(matrix)
        assert trace == 15  # 1 + 5 + 9 = 15

    def test_eigenvalues(self) -> None:
        """Test eigenvalue computation."""
        matrix = Matrix([[1, 0], [0, 2]])  # Diagonal matrix
        eigenvals = MatrixOperations.eigenvalues(matrix)
        # Should be [1, 2] (diagonal elements)
        assert set(eigenvals) == {1, 2}

    def test_solve_system(self) -> None:
        """Test solving linear system Ax = b."""
        A = Matrix([[2, 1], [1, 1]])
        b = Matrix([3, 2])
        solution = MatrixOperations.solve_system(A, b)

        # Verify solution by checking A * x = b
        result = A * solution
        assert result == b

    def test_row_echelon_form(self) -> None:
        """Test row echelon form computation."""
        matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        rref = MatrixOperations.row_echelon_form(matrix)

        # The result should be in reduced row echelon form
        # Check that it's upper triangular with leading 1s
        assert rref[0, 0] == 1
        assert rref[1, 0] == 0
        assert rref[2, 0] == 0


class TestLinearAlgebra:
    """Test the main LinearAlgebra class."""

    def test_create_vector(self) -> None:
        """Test vector creation through LinearAlgebra."""
        v = LinearAlgebra.create_vector([1, 2, 3])
        assert isinstance(v, Vector)
        assert v.components == [1, 2, 3]

    def test_create_matrix(self) -> None:
        """Test matrix creation through LinearAlgebra."""
        matrix = LinearAlgebra.create_matrix([[1, 2], [3, 4]])
        expected = Matrix([[1, 2], [3, 4]])
        assert matrix == expected

    def test_vector_angle(self) -> None:
        """Test angle computation between vectors."""
        v1 = Vector([1, 0])
        v2 = Vector([0, 1])
        angle = LinearAlgebra.vector_angle(v1, v2)
        # Angle should be π/2 (90 degrees)
        expected = sp.pi / 2
        assert sp.simplify(angle - expected) == 0

    def test_are_orthogonal(self) -> None:
        """Test orthogonality check."""
        v1 = Vector([1, 0])
        v2 = Vector([0, 1])
        assert LinearAlgebra.are_orthogonal(v1, v2) is True

        v3 = Vector([1, 1])
        assert LinearAlgebra.are_orthogonal(v1, v3) is False

    def test_are_parallel(self) -> None:
        """Test parallelism check."""
        v1 = Vector([1, 2])
        v2 = Vector([2, 4])  # 2 * v1
        assert LinearAlgebra.are_parallel(v1, v2) is True

        v3 = Vector([1, 3])
        assert LinearAlgebra.are_parallel(v1, v3) is False

    def test_gram_schmidt(self) -> None:
        """Test Gram-Schmidt orthogonalization."""
        v1 = Vector([1, 1, 0])
        v2 = Vector([1, 0, 1])
        vectors = [v1, v2]

        orthogonal = LinearAlgebra.gram_schmidt(vectors)

        # Check that result has orthogonal vectors
        assert len(orthogonal) == 2
        # Orthogonal vectors should have zero dot product
        dot_product = orthogonal[0].dot(orthogonal[1])
        assert sp.simplify(dot_product) == 0

    def test_project_vector(self) -> None:
        """Test vector projection."""
        v = Vector([1, 1])
        onto = Vector([1, 0])

        projection = LinearAlgebra.project_vector(v, onto)

        # Projection of [1,1] onto [1,0] should be [1,0]
        assert projection.components == [1, 0]

    def test_project_vector_zero_target(self) -> None:
        """Test projecting onto zero vector raises error."""
        v = Vector([1, 1])
        onto = Vector([0, 0])

        with pytest.raises(ValueError, match="Cannot project onto zero vector"):
            LinearAlgebra.project_vector(v, onto)


class TestIntegration:
    """Test integration between Vector and Matrix operations."""

    def test_vector_matrix_multiplication(self) -> None:
        """Test multiplying a matrix by a vector."""
        matrix = Matrix([[1, 2], [3, 4]])
        vector = Vector([1, 2])
        vector_matrix = vector.to_sympy_matrix()

        result = matrix * vector_matrix
        expected = Matrix([5, 11])  # [1*1 + 2*2, 3*1 + 4*2] = [5, 11]
        assert result == expected

    def test_eigenvalue_eigenvector_consistency(self) -> None:
        """Test that eigenvalues and eigenvectors are consistent."""
        matrix = Matrix([[3, 1], [0, 2]])

        eigenvals = MatrixOperations.eigenvalues(matrix)
        eigenvects = MatrixOperations.eigenvectors(matrix)

        # Check that each eigenvalue has corresponding eigenvector
        eigenval_set = set(eigenvals)
        eigenvect_eigenvals = {eigenval for eigenval, _, _ in eigenvects}
        assert eigenval_set == eigenvect_eigenvals

    def test_symbolic_computation(self) -> None:
        """Test linear algebra with symbolic expressions."""
        x = sp.Symbol("x")
        matrix = LinearAlgebra.create_matrix([[x, 1], [0, 2]])

        det = MatrixOperations.determinant(matrix)
        assert det == 2 * x  # Determinant should be 2x
