import numpy as np

# Four corners of a square: each row is [x, y]
points = np.array([
    [0.0, 0.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [0.0, 1.0]
])

# We will scale the shape by 2 in X, 3 in Y, and rotate it 45 degrees
scale_x, scale_y = 2.0, 3.0
theta = np.radians(45)
c, s = np.cos(theta), np.sin(theta)

# Scaling matrix
S = np.array([[scale_x, 0], [0, scale_y]])
# Rotation matrix
R = np.array([[c, -s], [s, c]])

# Combined transformation
transformation = R @ S

# Row-vector form requires multiplication by transpose
transformed_points = points @ transformation.T 

print("Original points:\n", points)
print("Transformation matrix:\n", transformation)
print("Transformed points:\n", transformed_points)
print("Determinant:", np.linalg.det(transformation))