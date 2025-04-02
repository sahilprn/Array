import numpy as np
A = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])

A_inv = np.linalg.inv(A)


product_1 = np.dot(A, A_inv)
product_2 = np.dot(A_inv, A)
print("Matrix A:")
print(A)

print("\nInverse of A (A^-1):")
print(A_inv)

print("\nMatrix Product A * A^-1 (Should be close to Identity):")
print(product_1)

print("\nMatrix Product A^-1 * A (Should be close to Identity):")
print(product_2)