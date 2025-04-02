import numpy as np

A = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])

A_inv = np.linalg.inv(A)
identity_matrix = np.dot(A, A_inv)
print("Matrix A:")
print(A)

print("\nInverse of Matrix A (A_inv):")
print(A_inv)

print("\nProduct of A * A_inv (should be close to identity matrix):")
print(identity_matrix)

is_identity = np.allclose(identity_matrix, np.eye(3))
print("\nIs A * A_inv close to the identity matrix?")
print(is_identity)
