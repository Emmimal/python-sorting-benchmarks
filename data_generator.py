import random

def generate_random(n):
    return [random.randint(0, 10000) for _ in range(n)]

def generate_nearly_sorted(n, chaos=0.1):
    arr = list(range(n))
    chaos_count = int(n * chaos)
    for _ in range(chaos_count):
        i, j = random.randint(0, n-1), random.randint(0, n-1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def generate_reversed(n):
    return list(range(n-1, -1, -1))

def generate_duplicates(n, unique_ratio=0.5):
    unique = int(n * unique_ratio)
    arr = list(range(unique))
    arr.extend([random.choice(arr) for _ in range(n - unique)])
    random.shuffle(arr)
    return arr

DATA_PATTERNS = {
    "random": generate_random,
    "nearly_sorted": generate_nearly_sorted,
    "reversed": generate_reversed,
    "duplicates": generate_duplicates,
}
