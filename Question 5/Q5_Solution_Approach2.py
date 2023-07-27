import numpy as np

def autocorrelation_fft(signal):
    n = len(signal)
    autocovariance = np.correlate(signal - np.mean(signal), signal - np.mean(signal), mode='full')
    result = np.fft.ifft(np.fft.fft(signal, n=2*n) * np.conj(np.fft.fft(autocovariance, n=2*n)))
    return result[:n].real / result[0].real  # Normalize by the first element (corresponding to lag 0)

# Example usage:
signal_data = [3, 8, 4, 6, 7, 5, 4, 3, 6, 7]

result = autocorrelation_fft(signal_data)
print("Autocorrelation using FFT:")
print(result)
