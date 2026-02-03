"""
BENCHMARK: UCCC Speedup (v1.0 vs v1.2)
Target: 10MB High-Entropy Data (Simulating Encrypted/Video)
"""
import time
import numpy as np
from uccc import UniversalCompressor
from uccc_thermal import ThermalCompressor

def bench():
    # ENFORCE DETERMINISM (VSA ZERO POINT)
    np.random.seed(0)

    # 1. Generate 10MB Thermal Mass
    print("Generating 10MB High-Entropy Data...")
    data = np.random.bytes(10 * 1024 * 1024)
    
    # 2. Bench v1.0 (Base)
    print("\n--- Benchmarking v1.0 (UniversalCompressor) ---")
    base = UniversalCompressor()
    t0 = time.perf_counter()
    # v1.0 will analyze and try to compress (burning CPU)
    base.compress(data) 
    t_base = time.perf_counter() - t0
    print(f"v1.0 Time: {t_base:.4f}s")
    
    # 3. Bench v1.2 (Thermal Patch)
    print("\n--- Benchmarking v1.2 (ThermalCompressor) ---")
    patch = ThermalCompressor()
    t1 = time.perf_counter()
    # v1.2 will detect heat and skip compression
    patch.compress(data)
    t_patch = time.perf_counter() - t1
    print(f"v1.2 Time: {t_patch:.4f}s")
    
    # 4. Result
    speedup = t_base / t_patch
    print("-" * 40)
    print(f"SPEEDUP FACTOR: {speedup:.2f}x")
    print("-" * 40)

if __name__ == "__main__":
    bench()
