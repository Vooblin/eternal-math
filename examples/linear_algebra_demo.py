#!/usr/bin/env python3
"""
Linear Algebra Demo

This example demonstrates the linear algebra capabilities of Eternal Math,
including vector operations, matrix computations, and advanced linear algebra concepts.
"""

import math

from eternal_math import LinearAlgebra, MatrixOperations, Vector


def vector_operations_demo() -> None:
    """Demonstrate basic vector operations."""
    print("1. Vector Operations:")
    print("=" * 30)

    # Create vectors
    v1 = Vector([3, 4])
    v2 = Vector([1, 2])
    v3 = Vector([1, 0, 0])
    v4 = Vector([0, 1, 0])

    print(f"   Vector v1: {v1}")
    print(f"   Vector v2: {v2}")
    print(f"   Magnitude of v1: {float(v1.magnitude()):.3f}")
    print(f"   Magnitude of v2: {float(v2.magnitude()):.3f}")

    # Basic operations
    print(f"\n   v1 + v2 = {v1 + v2}")
    print(f"   v1 - v2 = {v1 - v2}")
    print(f"   2 * v1 = {2 * v1}")

    # Dot product
    dot_product = v1.dot(v2)
    print(f"   v1 · v2 = {dot_product}")

    # Cross product (3D vectors)
    print(f"\n   3D vectors: v3 = {v3}, v4 = {v4}")
    cross_product = v3.cross(v4)
    print(f"   v3 × v4 = {cross_product}")

    # Normalization
    normalized_v1 = v1.normalize()
    print(f"\n   Normalized v1: {normalized_v1}")
    print(f"   Magnitude of normalized v1: {float(normalized_v1.magnitude()):.6f}")

    print()


def matrix_operations_demo() -> None:
    """Demonstrate matrix operations."""
    print("2. Matrix Operations:")
    print("=" * 30)

    # Create matrices
    matrix_a = MatrixOperations.create_matrix([[1, 2], [3, 4]])
    matrix_b = MatrixOperations.create_matrix([[5, 6], [7, 8]])

    print("   Matrix A:")
    print(matrix_a)
    print("\n   Matrix B:")
    print(matrix_b)

    # Basic properties
    print(f"\n   Determinant of A: {MatrixOperations.determinant(matrix_a)}")
    print(f"   Rank of A: {MatrixOperations.rank(matrix_a)}")
    print(f"   Trace of A: {MatrixOperations.trace(matrix_a)}")

    # Transpose
    transpose_a = MatrixOperations.transpose(matrix_a)
    print("\n   Transpose of A:")
    print(transpose_a)

    # Matrix multiplication
    product = matrix_a * matrix_b
    print("\n   A × B:")
    print(product)

    # Identity and zero matrices
    identity = MatrixOperations.identity_matrix(3)
    zero_mat = MatrixOperations.zero_matrix(2, 3)

    print("\n   3×3 Identity matrix:")
    print(identity)
    print("\n   2×3 Zero matrix:")
    print(zero_mat)

    print()


def eigenvalue_demo() -> None:
    """Demonstrate eigenvalue and eigenvector computations."""
    print("3. Eigenvalues and Eigenvectors:")
    print("=" * 35)

    # Create a symmetric matrix (has real eigenvalues)
    matrix = MatrixOperations.create_matrix([[4, 1], [1, 3]])

    print("   Matrix M:")
    print(matrix)

    # Compute eigenvalues
    eigenvals = MatrixOperations.eigenvalues(matrix)
    print(f"\n   Eigenvalues: {eigenvals}")

    # Compute eigenvectors
    eigenvects = MatrixOperations.eigenvectors(matrix)
    print("\n   Eigenvectors (eigenvalue, multiplicity, vectors):")
    for eigenval, mult, vects in eigenvects:
        print(f"   λ = {eigenval}, multiplicity = {mult}")
        for i, vect in enumerate(vects):
            print(f"     v{i+1} = {vect.T}")

    print()


def linear_system_demo() -> None:
    """Demonstrate solving linear systems."""
    print("4. Linear System Solving:")
    print("=" * 30)

    # System: 2x + y = 5, x + y = 3
    # Solution: x = 2, y = 1
    coefficient_matrix = MatrixOperations.create_matrix([[2, 1], [1, 1]])
    constants = MatrixOperations.create_matrix([[5], [3]])

    print("   System: Ax = b")
    print("   Coefficient matrix A:")
    print(coefficient_matrix)
    print("\n   Constants vector b:")
    print(constants)

    # Solve the system
    solution = MatrixOperations.solve_system(coefficient_matrix, constants)
    print("\n   Solution x:")
    print(solution)

    # Verify the solution
    verification = coefficient_matrix * solution
    print("\n   Verification (Ax):")
    print(verification)
    print(f"   Should equal b: {verification == constants}")

    print()


def vector_geometry_demo() -> None:
    """Demonstrate geometric vector operations."""
    print("5. Vector Geometry:")
    print("=" * 25)

    # Create vectors
    v1 = Vector([1, 0])
    v2 = Vector([0, 1])
    v3 = Vector([1, 1])

    print(f"   Vector v1: {v1}")
    print(f"   Vector v2: {v2}")
    print(f"   Vector v3: {v3}")

    # Angle calculations
    angle_v1_v2 = LinearAlgebra.vector_angle(v1, v2)
    angle_v1_v3 = LinearAlgebra.vector_angle(v1, v3)

    print(
        f"\n   Angle between v1 and v2: {float(angle_v1_v2):.4f} radians"
        f" ({float(angle_v1_v2) * 180/math.pi:.1f}°)"
    )
    print(
        f"   Angle between v1 and v3: {float(angle_v1_v3):.4f} radians"
        f" ({float(angle_v1_v3) * 180/math.pi:.1f}°)"
    )

    # Orthogonality and parallelism
    print(f"\n   v1 and v2 are orthogonal: {LinearAlgebra.are_orthogonal(v1, v2)}")
    print(f"   v1 and v3 are orthogonal: {LinearAlgebra.are_orthogonal(v1, v3)}")

    parallel_v = Vector([2, 0])  # Parallel to v1
    print(f"   v1 and [2,0] are parallel: {LinearAlgebra.are_parallel(v1, parallel_v)}")

    # Vector projection
    projection = LinearAlgebra.project_vector(v3, v1)
    print(f"\n   Projection of v3 onto v1: {projection}")

    print()


def gram_schmidt_demo() -> None:
    """Demonstrate Gram-Schmidt orthogonalization."""
    print("6. Gram-Schmidt Orthogonalization:")
    print("=" * 40)

    # Create linearly independent vectors
    vectors = [Vector([1, 1, 0]), Vector([1, 0, 1]), Vector([0, 1, 1])]

    print("   Original vectors:")
    for i, v in enumerate(vectors):
        print(f"   v{i+1} = {v}")

    # Apply Gram-Schmidt
    orthogonal_vectors = LinearAlgebra.gram_schmidt(vectors)

    print("\n   Orthogonalized vectors:")
    for i, v in enumerate(orthogonal_vectors):
        print(f"   u{i+1} = {v}")
        print(f"       Magnitude: {float(v.magnitude()):.6f}")

    # Verify orthogonality
    print("\n   Verification (dot products should be zero):")
    for i in range(len(orthogonal_vectors)):
        for j in range(i + 1, len(orthogonal_vectors)):
            dot_prod = orthogonal_vectors[i].dot(orthogonal_vectors[j])
            print(f"   u{i+1} · u{j+1} = {float(dot_prod):.10f}")

    print()


def advanced_matrix_demo() -> None:
    """Demonstrate advanced matrix operations."""
    print("7. Advanced Matrix Operations:")
    print("=" * 35)

    # Create a matrix
    matrix = MatrixOperations.create_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    print("   Matrix M:")
    print(matrix)

    # Row echelon form
    rref_matrix = MatrixOperations.row_echelon_form(matrix)
    print("\n   Row echelon form:")
    print(rref_matrix)

    # Null space
    null_space = MatrixOperations.null_space(matrix)
    print("\n   Null space basis vectors:")
    for i, vec in enumerate(null_space):
        print(f"   n{i+1} = {vec.T}")

    # Column space
    col_space = MatrixOperations.column_space(matrix)
    print("\n   Column space basis vectors:")
    for i, vec in enumerate(col_space):
        print(f"   c{i+1} = {vec.T}")

    print()


def integration_demo() -> None:
    """Demonstrate integration with symbolic math."""
    print("8. Integration with Symbolic Math:")
    print("=" * 40)

    # Create matrix with symbolic elements
    import sympy as sp

    x = sp.Symbol("x")

    symbolic_matrix = LinearAlgebra.create_matrix([[x, 1], [0, 2]])

    print("   Symbolic matrix:")
    print(symbolic_matrix)

    det = MatrixOperations.determinant(symbolic_matrix)
    print(f"\n   Determinant: {det}")

    # Eigenvalues with parameter
    eigenvals = MatrixOperations.eigenvalues(symbolic_matrix)
    print(f"   Eigenvalues: {eigenvals}")

    print()


def main() -> None:
    """Run all linear algebra demonstrations."""
    print("🔢 Eternal Math - Linear Algebra Demo")
    print("=" * 50)
    print("Comprehensive demonstration of linear algebra capabilities")
    print("including vectors, matrices, eigenvalues, and geometric operations.")
    print("=" * 50)

    vector_operations_demo()
    matrix_operations_demo()
    eigenvalue_demo()
    linear_system_demo()
    vector_geometry_demo()
    gram_schmidt_demo()
    advanced_matrix_demo()
    integration_demo()

    print("🎯 Demo completed! The linear algebra module provides:")
    print("• Vector operations (dot product, cross product, normalization)")
    print("• Matrix computations (determinant, inverse, eigenvalues)")
    print("• Linear system solving")
    print("• Geometric operations (angles, projections, orthogonalization)")
    print("• Advanced algorithms (Gram-Schmidt, null space, column space)")
    print("• Seamless integration with symbolic mathematics")
    print("=" * 50)


if __name__ == "__main__":
    main()
