import math  # Provides mathematical functions like square root
from typing import List  # Allows us to specify list types for better readability and type checking
# Define a function to calculate cosine similarity between two vectors
def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    # Step 1: Compute the dot product of the two vectors
    # Multiply corresponding elements and sum them up
    # Example: [1,2,3] • [2,3,4] = (1*2 + 2*3 + 3*4)
    dot_product = sum(a * b for a, b in zip(vec1, vec2))

    # Step 2: Compute the magnitude (length) of vec1
    # Formula: sqrt(x1^2 + x2^2 + x3^2 + ...)
    mag1 = math.sqrt(sum(a * a for a in vec1))

    # Step 3: Compute the magnitude (length) of vec2
    mag2 = math.sqrt(sum(b * b for b in vec2))

    # Step 4: Handle edge case where one of the vectors has zero length
    # Cosine similarity would be undefined (division by zero), so return 0.0 instead
    if mag1 == 0 or mag2 == 0:
        return 0.0

    # Step 5: Compute cosine similarity
    # Formula: dot_product / (|vec1| * |vec2|)
    return dot_product / (mag1 * mag2)
# Example vectors
vec1 = [1, 2, 3]
vec2 = [2, 3, 4]
# Call the function and print the result
print(cosine_similarity(vec1, vec2))