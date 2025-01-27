def minimax_alpha_beta(depth, node_index, is_maximizing_player, scores, alpha, beta):
    # Base case: Leaf node reached
    if depth == 3:  # Depth 3 for 8 leaf nodes
        return scores[node_index]

    if is_maximizing_player:
        max_eval = float('-inf')
        for i in range(2):  # Two children per node
            eval = minimax_alpha_beta(depth + 1, node_index * 2 + i, False, scores, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(2):  # Two children per node
            eval = minimax_alpha_beta(depth + 1, node_index * 2 + i, True, scores, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval

# Input Parsing
scores = list(map(int, input().split()))

# Calculate the base optimal value using Minimax with alpha-beta pruning
base_optimal_value = minimax_alpha_beta(0, 0, True, scores, float('-inf'), float('inf'))

# Apply 10% increase due to synergistic effects
optimal_value_with_increase = int(base_optimal_value * 1.1)

# Output the results
print(f"Base optimal value: {base_optimal_value}")
print(f"After 10% increase: {optimal_value_with_increase}")
