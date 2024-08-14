import numpy as np
from scipy.io import wavfile

def read_audio(file_path):
    sample_rate, data = wavfile.read(file_path)
    return sample_rate, data

def calculate_mse(data1, data2):
    return np.mean((data1 - data2) ** 2)

def percentage_difference(file1, file2):
    sample_rate1, data1 = read_audio(file1)
    sample_rate2, data2 = read_audio(file2)

    if sample_rate1 != sample_rate2:
        raise ValueError("Sample rates of the audio files do not match.")
    
    if data1.shape != data2.shape:
        raise ValueError("Shapes of the audio files do not match.")

    mse = calculate_mse(data1, data2)
    max_possible_error = np.max([np.max(data1), np.max(data2)]) ** 2
    percent_diff = (mse / max_possible_error) * 100

    return percent_diff

# Example usage
file1 = 'outputs/new_separated/1919-142785-0045_6319-275224-0016_s1.wav'
file2 = 'outputs/new_separated/1919-142785-0045_6319-275224-0016_s2.wav'

try:
    difference = percentage_difference(file1, file2)
    print(f"The audio files are {difference:.2f}% unequivalent.")
except ValueError as e:
    print(f"Error: {e}")
