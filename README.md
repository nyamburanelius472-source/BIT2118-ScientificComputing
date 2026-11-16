# BIT2118-ScientificComputing

## Task 2: NumPy Arrays and Numerical Computation

*   **Input values:** 24 hourly temperature readings in degrees Celsius.
*   **Mathematical operation:** Arithmetic mean, minimum, maximum, and vectorized linear transformation (F = 1.8C + 32).
*   **Parameter Change:** I changed the first temperature reading from 18.5 to 30.0. As a result, the daily mean temperature increased, and the first Fahrenheit reading increased from 65.3 to 86.0.
*   **Output Interpretation:** The script calculates the daily average, lowest, and highest temperatures, and converts them to Fahrenheit. It demonstrates how NumPy allows us to apply a mathematical operation to an entire array at once without writing loops.

## Task 3: Mathematical Functions and Vectorization

*   **Input values:** 1,000,000 simulated network latency readings in milliseconds.
*   **Mathematical operation:** Division by 1000 and squaring (converting to seconds and calculating squared values).
*   **Parameter Change:** I changed the number of simulated readings. If I reduce the dataset to 10 values, the time difference between the loop and vectorized version becomes negligible because the overhead of starting the loop is small.
*   **Output Interpretation:** The output shows that the vectorized NumPy approach is approximately 76 times faster (0.5708s for the loop vs 0.0075s for vectorization). This is because NumPy performs the operations in optimized C code without the overhead of looping in Python.

## Task 4: Floating-Point Arithmetic and Numerical Errors

*   **Input values:** The values 0.1, 0.2, 0.3, the square root of 2 approximated as 1.414, and small test values (1e-4, 1e-8, 1e-12).
*   **Mathematical operation:** Floating-point addition, absolute error, relative error, and evaluating a formula using both an unstable and a stable algebraic arrangement.
*   **Parameter Change:** If I change the approximation of the square root of 2 to 1.4142 (instead of 1.414), the absolute error decreases because the approximation is closer to the true value.
*   **Output Interpretation:** The script proves that `0.1 + 0.2 == 0.3` is `False` due to binary representation limits. It also shows that for very small values (like 1e-12), the "direct" formula loses precision (yielding 0.500044...), while the mathematically rearranged "stable" formula gives the correct answer of 0.500000000000.

## Task 5: Matrix Algebra and Matrix Operations

*   **Input values:** A 4x2 matrix representing the corners of a 1x1 square, scaling factors (2 and 3), and a rotation angle (45 degrees).
*   **Mathematical operation:** Matrix multiplication (combining rotation and scaling matrices), and calculating the determinant of the transformation matrix.
*   **Parameter Change:** If I change the rotation angle from 45 degrees to 90 degrees, the output "Transformed points" will change to reflect a quarter-turn rotation, moving the corners to different quadrants.
*   **Output Interpretation:** The script successfully applies a combined scaling and rotation to the square. The "Transformed points" show the new coordinates in 2D space. The determinant represents how much the area of the shape scaled (in this case, 6.0, which is the product of the x and y scaling factors).