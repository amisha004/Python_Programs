from collections import Counter
import statistics

def calculate_statistics(numbers):
    # Calculate the mean
    mean = sum(numbers) / len(numbers)
    
    # Calculate the median
    median = statistics.median(numbers)
    
    # Calculate the mode
    mode = Counter(numbers).most_common(1)[0][0]
    
    # Return the mean, median, and mode as a tuple
    return mean, median, mode


numbers = [1, 2, 3, 4, 4, 5, 5, 5, 6]
mean, median, mode = calculate_statistics(numbers)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
