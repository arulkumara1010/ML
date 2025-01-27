def minimax(depth, node_index, is_maximizing_player, scores, height):
    # Base case: leaf node is reached
    if depth == height:
        return scores[node_index]

    if is_maximizing_player:
        return max(
            minimax(depth + 1, node_index * 2, False, scores, height),
            minimax(depth + 1, node_index * 2 + 1, False, scores, height)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, scores, height),
            minimax(depth + 1, node_index * 2 + 1, True, scores, height)
        )

# Input Parsing
import math

n = int(input())
scores = list(map(int, input().split()))
height = int(math.log2(n))

optimal_value = minimax(0, 0, True, scores, height)
print(f"The optimal value is: {optimal_value}")
