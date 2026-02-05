# python-sorting-benchmarks
Benchmarks of 6 classic sorting algorithms in pure Python — showing why constant factors and CPython overhead make Timsort (built-in sorted()) untouchable.
# python-sorting-benchmarks

A companion repository for the blog post:  
**"I Implemented Every Sorting Algorithm in Python — The Results Nobody Talks About (Benchmarked on CPython)"**  
https://emitechlogic.com/sorting-algorithm-in-python/]

This repo contains clean, from-scratch implementations of six classic sorting algorithms in pure Python, plus a robust benchmarking suite that measures their real-world performance on CPython.

The goal is to show why textbook Big-O analysis doesn't tell the full story in Python — constant factors, interpreter overhead, recursion costs, memory allocations, and garbage collection dominate practical performance.

## Key Findings (from the blog post)

- Bubble/Selection sort become unusable around 1,000–5,000 elements.
- Insertion sort surprisingly wins on small (<100 elements) or nearly-sorted data.
- Merge/Quick/Heap sort are decent but still 5–150× slower than Python's built-in `sorted()` (Timsort).
- Python's built-in sort is untouchable — use it always in production.

## Repository Structure
python-sorting-benchmarks/
├── sorts/
│   ├── init.py
│   ├── bubble_sort.py
│   ├── selection_sort.py
│   ├── insertion_sort.py
│   ├── merge_sort.py
│   ├── quick_sort.py
│   └── heap_sort.py
├── data_generator.py      # Functions to generate test datasets
├── benchmark.py           # Main benchmarking script
├── results_example.csv    # Sample output from my machine
├── README.md              # This file
└── requirements.txt       # Empty — uses only stdlib

## How to Run the Benchmarks

1. Clone the repo:
   ```bash
   git clone https://github.com/Emmimal/python-sorting-benchmarks.git
   cd python-sorting-benchmarks
2. Run the benchmarks:
   python benchmark.py

## What This Benchmark Does

- Tests all sorting algorithms on **multiple dataset sizes and patterns**
- Results are:
  - Printed to the console
  - Saved to `results.csv`
- Runtime: **~10–30 minutes** on a standard laptop  
  *(Bubble sort on large datasets is intentionally slow)*

You can adjust dataset sizes and input patterns in `benchmark.py`.

---

## Environment (Used for Blog Post Results)

- **Python:** CPython 3.11.4
- **OS:** Ubuntu 22.04 LTS
- **CPU:** Intel i5-1135G7
- **RAM:** 16 GB

> Your results may vary slightly due to hardware differences and garbage collection timing,  
> but **relative performance trends should remain consistent**.

---

## Notes on Implementations

- All sorting functions **return a new sorted list**
- Input data is **copied before sorting** for fair benchmarking
- In-place techniques are used internally where possible
- Code is **simple and readable**
  - No micro-optimizations
  - Designed to expose real Python overhead

---

## License

**MIT License** — feel free to use, modify, or share.

---

## Questions or Feedback?

Open an issue or leave a comment on the blog post.

— **Emmimal Alexander**  
[@Emmimal on GitHub]

### File: `sorts/__init__.py`
```python
# Empty file to make 'sorts' a package
