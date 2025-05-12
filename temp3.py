import numpy as np

# 1. Create two (3×3) arrays of random integers between 0 and 20
a = np.random.randint(0, 21, size=(3, 3))
b = np.random.randint(0, 21, size=(3, 3))

print("Array a:\n", a)
print("Array b:\n", b)

# 1. Element-wise addition
sum_ab = a + b
print("\n1. Element-wise addition (a + b):\n", sum_ab)

# 2. Mean and standard deviation of first array
mean_a = a.mean()
std_a  = a.std()
print(f"\n2. For array a → mean: {mean_a:.2f}, std dev: {std_a:.2f}")

# 3. Multiply each element of first array by a scalar (e.g. 5)
scalar = 5
scaled_a = a * scalar
print(f"\n3. Array a multiplied by {scalar}:\n", scaled_a)

# 4. Dot product of the two matrices
dot_ab = np.dot(a, b)
print("\n4. Dot product (a · b):\n", dot_ab)
