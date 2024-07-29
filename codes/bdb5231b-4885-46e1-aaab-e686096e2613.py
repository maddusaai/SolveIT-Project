def min_travel_cost(N, costs, K, attacks):
    # Compute prefix sums for clockwise direction
    prefix_sum = [0] * N
    prefix_sum[0] = costs[0]
    for i in range(1, N):
        prefix_sum[i] = prefix_sum[i - 1] + costs[i]

    total_cost = prefix_sum[-1]
    
    # Helper function to get cost between two cities in clockwise direction
    def get_clockwise_cost(start, end):
        if start <= end:
            return prefix_sum[end - 1] - (prefix_sum[start - 1] if start > 0 else 0)
        else:
            return total_cost - (prefix_sum[start - 1] if start > 0 else 0) + prefix_sum[end - 1]

    results = []
    current_position = 0

    for direction, distance in attacks:
        if direction == 1:
            target_position = (current_position + distance) % N
        else:
            target_position = (current_position - distance) % N
            if target_position < 0:
                target_position += N
        
        # Calculate costs for both directions
        cost_clockwise = get_clockwise_cost(current_position, target_position)
        cost_anticlockwise = get_clockwise_cost(target_position, current_position)
        
        # Minimum cost to reach target city
        results.append(min(cost_clockwise, cost_anticlockwise))
        
        # Update current position
        current_position = target_position
    
    return results

# Input processing
import sys
input = sys.stdin.read
data = input().strip().split()

N = int(data[0])
costs = list(map(int, data[1:N+1]))
K = int(data[N+1])
attacks = [(int(data[N+2 + 2*i]), int(data[N+3 + 2*i])) for i in range(K)]

# Calculate minimum travel costs
results = min_travel_cost(N, costs, K, attacks)

# Print the results
for result in results:
    print(result)