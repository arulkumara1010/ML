import math

# Define the function Y = sin(X) - 0.1 * X^2
def function(x):
    return math.sin(x) - 0.1 * x**2

# Hill-climbing algorithm
def hill_climb(x, step):
    y = function(x)
    while True:
        x1 = x + step  # Move to the right
        y1 = function(x1)
        if y1 > y:
            x, y = x1, y1  # Update to the new point
        else:
            return x, y  # Stop when no higher value is found

# Find the local maximum starting at X = 0 with step 0.05
def find_local_maximum():
    start_x = 0
    step = 0.05
    max_x, max_y = hill_climb(start_x, step)
    print(f"Maximum found at X = {max_x:.2f} with value Y = {max_y:.2f}")

# Execute the function
find_local_maximum()
