"""
Linear algebra operations and matrix computations for Eternal Math.
"""

from typing import List, Tuple, Union

import sympy as sp
from sympy import Matrix, eye, zeros


class Vector:
    """Represents a mathematical vector with operations."""

    def __init__(self, components: List[Union[int, float, sp.Expr]]):
        """Initialize a vector with components."""
        if not components:
            raise ValueError("Vector must have at least one component")
        self.components = [sp.sympify(c) for c in components]
        self.dimension = len(components)

    def __repr__(self) -> str:
        return f"Vector({self.components})"

    def __str__(self) -> str:
        return f"[{', '.join(str(c) for c in self.components)}]"

    def __getitem__(self, index: int) -> sp.Expr:
        return self.components[index]

    def __len__(self) -> int:
        return self.dimension

    def __add__(self, other: "Vector") -> "Vector":
        """Add two vectors."""
        if not isinstance(other, Vector):
            raise TypeError("Can only add Vector to Vector")
        if self.dimension != other.dimension:
            raise ValueError("Vectors must have same dimension for addition")

        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(result)

    def __sub__(self, other: "Vector") -> "Vector":
        """Subtract two vectors."""
        if not isinstance(other, Vector):
            raise TypeError("Can only subtract Vector from Vector")
        if self.dimension != other.dimension:
            raise ValueError("Vectors must have same dimension for subtraction")

        result = [a - b for a, b in zip(self.components, other.components)]
        return Vector(result)

    def __mul__(self, scalar: Union[int, float, sp.Expr]) -> "Vector":
        """Multiply vector by a scalar."""
        scalar = sp.sympify(scalar)
        result = [scalar * c for c in self.components]
        return Vector(result)

    def __rmul__(self, scalar: Union[int, float, sp.Expr]) -> "Vector":
        """Right multiplication by scalar."""
        return self.__mul__(scalar)

    def dot(self, other: "Vector") -> sp.Expr:
        """Compute dot product with another vector."""
        if not isinstance(other, Vector):
            raise TypeError("Dot product requires another Vector")
        if self.dimension != other.dimension:
            raise ValueError("Vectors must have same dimension for dot product")

        return sum(a * b for a, b in zip(self.components, other.components))

    def cross(self, other: "Vector") -> "Vector":
        """Compute cross product (only for 3D vectors)."""
        if not isinstance(other, Vector):
            raise TypeError("Cross product requires another Vector")
        if self.dimension != 3 or other.dimension != 3:
            raise ValueError("Cross product is only defined for 3D vectors")

        a, b, c = self.components
        d, e, f = other.components

        result = [b * f - c * e, c * d - a * f, a * e - b * d]
        return Vector(result)

    def magnitude(self) -> sp.Expr:
        """Compute the magnitude (norm) of the vector."""
        return sp.sqrt(sum(c**2 for c in self.components))

    def normalize(self) -> "Vector":
        """Return a unit vector in the same direction."""
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize zero vector")
        return Vector([c / mag for c in self.components])

    def to_sympy_matrix(self) -> Matrix:
        """Convert to SymPy Matrix (column vector)."""
        return Matrix(self.components)


class MatrixOperations:
    """Class for matrix operations and linear algebra computations."""

    @staticmethod
    def create_matrix(data: List[List[Union[int, float, sp.Expr]]]) -> Matrix:
        """Create a matrix from nested lists."""
        if not data or not data[0]:
            raise ValueError("Matrix data cannot be empty")

        # Ensure all rows have the same length
        row_length = len(data[0])
        if not all(len(row) == row_length for row in data):
            raise ValueError("All rows must have the same length")

        return Matrix([[sp.sympify(elem) for elem in row] for row in data])

    @staticmethod
    def identity_matrix(size: int) -> Matrix:
        """Create an identity matrix of given size."""
        if size <= 0:
            raise ValueError("Matrix size must be positive")
        return eye(size)

    @staticmethod
    def zero_matrix(rows: int, cols: int) -> Matrix:
        """Create a zero matrix of given dimensions."""
        if rows <= 0 or cols <= 0:
            raise ValueError("Matrix dimensions must be positive")
        return zeros(rows, cols)

    @staticmethod
    def transpose(matrix: Matrix) -> Matrix:
        """Compute the transpose of a matrix."""
        return matrix.T

    @staticmethod
    def determinant(matrix: Matrix) -> sp.Expr:
        """Compute the determinant of a square matrix."""
        if matrix.rows != matrix.cols:
            raise ValueError("Determinant is only defined for square matrices")
        return matrix.det()

    @staticmethod
    def inverse(matrix: Matrix) -> Matrix:
        """Compute the inverse of a matrix."""
        if matrix.rows != matrix.cols:
            raise ValueError("Inverse is only defined for square matrices")

        det = matrix.det()
        if det == 0:
            raise ValueError("Matrix is singular (determinant is zero)")

        return matrix.inv()

    @staticmethod
    def rank(matrix: Matrix) -> int:
        """Compute the rank of a matrix."""
        return int(matrix.rank())

    @staticmethod
    def trace(matrix: Matrix) -> sp.Expr:
        """Compute the trace (sum of diagonal elements) of a square matrix."""
        if matrix.rows != matrix.cols:
            raise ValueError("Trace is only defined for square matrices")
        return matrix.trace()

    @staticmethod
    def eigenvalues(matrix: Matrix) -> List[sp.Expr]:
        """Compute eigenvalues of a square matrix."""
        if matrix.rows != matrix.cols:
            raise ValueError("Eigenvalues are only defined for square matrices")

        eigenvals = matrix.eigenvals()
        # Convert to list, accounting for multiplicities
        result = []
        for eigenval, multiplicity in eigenvals.items():
            result.extend([eigenval] * multiplicity)
        return result

    @staticmethod
    def eigenvectors(matrix: Matrix) -> List[Tuple[sp.Expr, int, List[Matrix]]]:
        """
        Compute eigenvectors of a square matrix.

        Returns:
            List of tuples (eigenvalue, multiplicity, eigenvectors)
        """
        if matrix.rows != matrix.cols:
            raise ValueError("Eigenvectors are only defined for square matrices")

        return list(matrix.eigenvects())

    @staticmethod
    def solve_system(matrix: Matrix, vector: Matrix) -> Matrix:
        """
        Solve the linear system Ax = b.

        Args:
            matrix: Coefficient matrix A
            vector: Right-hand side vector b

        Returns:
            Solution vector x
        """
        if matrix.rows != vector.rows:
            raise ValueError("Matrix and vector dimensions are incompatible")

        return matrix.LUsolve(vector)

    @staticmethod
    def row_echelon_form(matrix: Matrix) -> Matrix:
        """Compute row echelon form of a matrix."""
        return matrix.rref()[0]

    @staticmethod
    def null_space(matrix: Matrix) -> List[Matrix]:
        """Compute the null space (kernel) of a matrix."""
        return list(matrix.nullspace())

    @staticmethod
    def column_space(matrix: Matrix) -> List[Matrix]:
        """Compute the column space of a matrix."""
        return list(matrix.columnspace())


class LinearAlgebra:
    """Main class for linear algebra operations."""

    @staticmethod
    def create_vector(components: List[Union[int, float, sp.Expr]]) -> Vector:
        """Create a vector from components."""
        return Vector(components)

    @staticmethod
    def create_matrix(data: List[List[Union[int, float, sp.Expr]]]) -> Matrix:
        """Create a matrix from nested lists."""
        return MatrixOperations.create_matrix(data)

    @staticmethod
    def vector_angle(v1: Vector, v2: Vector) -> sp.Expr:
        """Compute angle between two vectors in radians."""
        if v1.dimension != v2.dimension:
            raise ValueError("Vectors must have same dimension")

        dot_product = v1.dot(v2)
        magnitude_product = v1.magnitude() * v2.magnitude()

        if magnitude_product == 0:
            raise ValueError("Cannot compute angle with zero vector")

        cos_angle = dot_product / magnitude_product
        return sp.acos(cos_angle)

    @staticmethod
    def are_orthogonal(v1: Vector, v2: Vector) -> bool:
        """Check if two vectors are orthogonal."""
        return bool(v1.dot(v2) == 0)

    @staticmethod
    def are_parallel(v1: Vector, v2: Vector) -> bool:
        """Check if two vectors are parallel."""
        if v1.dimension != v2.dimension:
            return False

        # Vectors are parallel if one is a scalar multiple of the other
        # Find first non-zero component to get the ratio
        ratio = None
        for a, b in zip(v1.components, v2.components):
            if b != 0:
                if ratio is None:
                    ratio = a / b
                elif sp.simplify(a / b - ratio) != 0:
                    return False
            elif a != 0:
                return False

        return True

    @staticmethod
    def gram_schmidt(vectors: List[Vector]) -> List[Vector]:
        """Apply Gram-Schmidt orthogonalization to a list of vectors."""
        if not vectors:
            return []

        orthogonal_vectors: List[Vector] = []

        for v in vectors:
            # Start with the current vector
            u = Vector(v.components[:])

            # Subtract projections onto all previous orthogonal vectors
            for prev_u in orthogonal_vectors:
                projection_coeff = v.dot(prev_u) / prev_u.dot(prev_u)
                projection = projection_coeff * prev_u
                u = u - projection

            # Add to orthogonal set if not zero
            if u.magnitude() != 0:
                orthogonal_vectors.append(u)

        return orthogonal_vectors

    @staticmethod
    def project_vector(v: Vector, onto: Vector) -> Vector:
        """Project vector v onto vector 'onto'."""
        if onto.magnitude() == 0:
            raise ValueError("Cannot project onto zero vector")

        projection_coeff = v.dot(onto) / onto.dot(onto)
        return Vector(projection_coeff * onto)


# Export main classes and functions
__all__ = ["Vector", "MatrixOperations", "LinearAlgebra"]
