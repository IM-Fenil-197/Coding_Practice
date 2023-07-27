import numpy as np

def autocorrelation(signal, lag):
    n = len(signal)
    mean = np.mean(signal)
    numerator = sum((signal[i] - mean) * (signal[i + lag] - mean) for i in range(n - lag))
    denominator = sum((signal[i] - mean) ** 2 for i in range(n))
    return numerator / denominator

# Example usage:
signal_data = [3, 8, 4, 6, 7, 5, 4, 3, 6, 7]
lag_value = 2

result = autocorrelation(signal_data, lag_value)
print(f"The autocorrelation at lag {lag_value} is: {result}")
