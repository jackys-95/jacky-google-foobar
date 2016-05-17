def answer(heights):
    """
    See the documentation for the rationale.
    """
    
    solution = 0
    left_peak = -1
    right_peak = -1
    left_index = 0
    right_index = len(heights) - 1
    while left_index < right_index:
        if heights[left_index] > left_peak:
            left_peak = heights[left_index]
        if heights[right_index] > right_peak:
            right_peak = heights[right_index]
        if (left_peak <= right_peak):
            solution += left_peak - heights[left_index]
            left_index += 1
        else:
            solution += right_peak - heights[right_index]
            right_index -= 1
    return solution     
