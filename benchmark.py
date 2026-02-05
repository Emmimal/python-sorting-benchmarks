import time
import statistics
import gc
import csv
from sorts import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, heap_sort
from data_generator import DATA_PATTERNS

ALGORITHMS = {
    "bubble_sort": bubble_sort.bubble_sort,
    "selection_sort": selection_sort.selection_sort,
    "insertion_sort": insertion_sort.insertion_sort,
    "merge_sort": merge_sort.merge_sort,
    "quick_sort": quick_sort.quick_sort,
    "heap_sort": heap_sort.heap_sort,
}

SIZES = [100, 500, 1000, 5000]  # Adjust as needed — larger = longer run

def benchmark(func, data, reps=50):
    # Warmup
    for _ in range(3):
        func(data.copy())
    
    gc.disable()
    times = []
    for _ in range(reps):
        test_data = data.copy()
        start = time.perf_counter()
        func(test_data)
        times.append(time.perf_counter() - start)
    gc.enable()
    return statistics.median(times)

def main():
    results = []
    print("Running benchmarks...\n")
    for size in SIZES:
        for pattern_name, generator in DATA_PATTERNS.items():
            data = generator(size)
            reps = 50 if size <= 1000 else 10
            print(f"Size: {size} | Pattern: {pattern_name}")
            for name, func in ALGORITHMS.items():
                try:
                    t = benchmark(func, data, reps)
                    print(f"  {name}: {t:.6f}s")
                    results.append([size, pattern_name, name, t])
                except Exception as e:
                    print(f"  {name}: ERROR ({e})")
                    results.append([size, pattern_name, name, "ERROR"])
    
    # Save to CSV
    with open("results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Size", "Pattern", "Algorithm", "Median Time (s)"])
        writer.writerows(results)
    
    print("\nBenchmarks complete! Results saved to results.csv")

if __name__ == "__main__":
    main()
