def linear_fit(input):
    """
    :type input: dict
    :rtype: Tuple[float, float]
    """
    # Extract x_values and y_values from input dictionary
    x_values = input["x_values"]
    y_values = input["y_values"]
    
    # Compute means
    x_mean = sum(x_values) / len(x_values)
    y_mean = sum(y_values) / len(y_values)
    
    # Compute numerator and denominator for slope
    numerator = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x_values, y_values))
    denominator = sum((xi - x_mean) ** 2 for xi in x_values)
    
    # Calculate slope and intercept
    slope = numerator / denominator
    intercept = y_mean - slope * x_mean
    
    return slope, intercept