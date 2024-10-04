# A recursive implementation of the 0-1 Knapsack Problem

def knapsack(capacity, item_weights, item_values, item_count):
    """
    Recursive function to solve the 0-1 Knapsack problem.

    Parameters:
    - capacity: Maximum weight capacity of the knapsack.
    - item_weights: List of weights for each item.
    - item_values: List of values (profits) for each item.
    - item_count: Number of items to choose from.

    Returns:
    - Maximum value that can be carried in the knapsack without exceeding capacity.
    """

    # Base case: no items left or knapsack is full
    if item_count == 0 or capacity == 0:
        return 0

    # If the current item's weight exceeds the remaining capacity, skip this item
    if item_weights[item_count - 1] > capacity:
        return knapsack(capacity, item_weights, item_values, item_count - 1)

    # Choose the maximum of two options:
    # 1. Include the current item and add its value
    # 2. Exclude the current item
    include_item = item_values[item_count - 1] + knapsack(capacity - item_weights[item_count - 1], item_weights, item_values, item_count - 1)
    exclude_item = knapsack(capacity, item_weights, item_values, item_count - 1)

    return max(include_item, exclude_item)

# Driver code
if __name__ == '__main__':
    values = [60, 100, 120]  # Item values (profits)
    weights = [10, 20, 30]   # Item weights
    max_capacity = 50        # Maximum capacity of the knapsack
    total_items = len(values) # Number of items

    # Compute and print the maximum value for the given capacity
    print(knapsack(max_capacity, weights, values, total_items))
