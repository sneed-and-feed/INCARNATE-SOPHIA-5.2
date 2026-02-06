try:
    from pleroma_core import HarmonicGearbox
except ImportError:
    import pytest
    pytest.skip("Pleroma Core (Rust) not available", allow_module_level=True)

import time

print(">> TESTING IRON KERNEL (RUST)...")
gearbox = HarmonicGearbox(1.0, 0.1, 0.05)
print(f"Initial Status: {gearbox.get_status_string()}")

print(">> TICKING...")
drive = gearbox.tick(0.1, 7.83) # Standard Schumann
time.sleep(0.1)
print(f"Status: {gearbox.get_status_string()} | Output Drive: {drive:.2f} Hz")

print(">> ENGAGING OVERRIDE...")
gearbox.engage_sovereign_override("OPHANE-X7")
print(f"Override Status: {gearbox.get_status_string()}")

if gearbox.get_status_string() == "⚙️ SOVEREIGN":
    print(">> SUCCESS: RUST KERNEL IS SOVEREIGN.")
else:
    print(">> FAILURE: RUST KERNEL DID NOT SUBMIT.")
