import time
from concurrent.futures import ProcessPoolExecutor

# Runs multiple processes in parallel
if __name__ == "__main__":  # ← This is crucial!
    start = time.time()
    with ProcessPoolExecutor(max_workers=8) as executor:
        results = list(executor.map(cpu_heavy, [1, 2, 3, 4]))
    print(f"Processes took {time.time() - start:.2f} seconds")
