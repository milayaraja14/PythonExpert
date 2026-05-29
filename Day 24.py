    import statistics
    
    # A list representing the daily temperatures in a city over 10 days
    data = [22, 24, 21, 22, 25, 29, 22, 23, 24, 28]
    
    def analyze_data(dataset):
        print(f"Dataset: {dataset}")
        print("-" * 30)
    
        # 1. Calculating the Mean (Average)
        mean_val = statistics.mean(dataset)
        print(f"Mean (Average): {mean_val}")
    
        # 2. Calculating the Median (Middle value)
        # If the number of data points is even, it averages the two middle numbers
        median_val = statistics.median(dataset)
        print(f"Median: {median_val}")
    
        # 3. Calculating the Mode (Most frequent value)
        try:
            mode_val = statistics.mode(dataset)
            print(f"Mode: {mode_val}")
        except statistics.StatisticsError:
            print("Mode: No unique mode found")
    
        # 4. Calculating Variance
        # High variance means the data is widely spread; low variance means it's close to the mean
        variance_val = statistics.variance(dataset)
        print(f"Variance: {round(variance_val, 2)}")
    
        # 5. Calculating Standard Deviation
        # This is often more intuitive than variance as it's in the same units as the data
        stdev_val = statistics.stdev(dataset)
        print(f"Standard Deviation: {round(stdev_val, 2)}")
    
    if __name__ == "__main__":
        analyze_data(data)
