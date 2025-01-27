def minimax_alpha_beta(depth, node_index, is_maximizer, scores, alpha, beta, current_depth):
    actions = []  # List to store actions for output

    # Base case: Leaf node reached
    if depth == current_depth:
        return scores[node_index], actions

    if is_maximizer:
        max_eval = float('-inf')
        for i in range(2):  # Two children per node
            eval, sub_actions = minimax_alpha_beta(depth, node_index * 2 + i, False, scores, alpha, beta, current_depth + 1)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            actions.extend(sub_actions)
            actions.append(f"Maximizer updated best value to {max_eval} at depth {current_depth}")
            if beta <= alpha:
                actions.append(f"Pruning at depth {current_depth} by Maximizer")
                break  # Beta cut-off
        return max_eval, actions
    else:
        min_eval = float('inf')
        for i in range(2):  # Two children per node
            eval, sub_actions = minimax_alpha_beta(depth, node_index * 2 + i, True, scores, alpha, beta, current_depth + 1)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            actions.extend(sub_actions)
            actions.append(f"Minimizer updated best value to {min_eval} at depth {current_depth}")
            if beta <= alpha:
                actions.append(f"Pruning at depth {current_depth} by Minimizer")
                break  # Alpha cut-off
        return min_eval, actions


# Input Parsing
depth = int(input().strip())
scores = list(map(int, input().strip().split()))

# Calculate the optimal value using Minimax with alpha-beta pruning
optimal_value, actions = minimax_alpha_beta(depth, 0, True, scores, float('-inf'), float('inf'), 0)

# Output Results
for action in actions:
    print(action)
print(f"Optimal Value: {optimal_value}")
