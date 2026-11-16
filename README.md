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