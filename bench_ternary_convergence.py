"""
BENCHMARK: Ternary vs Binary Convergence
Hypothesis: Ternary Logic (States -1, 0, 1) converges faster than Binary (-1, 1) 
due to the 'Neutral' (0) state acting as a natural momentum Pivot/Dropout.

Task: Learn the function f(x, y, z) = x + y - z (Symbolic Mapping)
Dataset: 1000 random samples.
"""
import random
import time

def activation_binary(val):
    return 1 if val >= 0 else -1

def activation_ternary(val):
    if val > 0.5: return 1
    if val < -0.5: return -1
    return 0

def target_function(x, y, z):
    # A simple linear combination requiring inhibition (negative) and excitation (positive)
    res = x + y - z
    if res > 0: return 1
    if res < 0: return -1
    return 0

def train_perceptron(mode='binary', epochs=100):
    weights = [0.0, 0.0, 0.0]
    bias = 0.0
    learning_rate = 0.1
    dataset = []
    
    # Generate Data
    for _ in range(200):
        # Inputs restricted to relevant domain
        x = random.choice([-1, 0, 1]) if mode == 'ternary' else random.choice([-1, 1])
        y = random.choice([-1, 0, 1]) if mode == 'ternary' else random.choice([-1, 1])
        z = random.choice([-1, 0, 1]) if mode == 'ternary' else random.choice([-1, 1])
        target = target_function(x, y, z)
        dataset.append(([x, y, z], target))
        
    start_time = time.perf_counter()
    converged = False
    final_epoch = epochs
    
    for epoch in range(epochs):
        errors = 0
        for inputs, target in dataset:
            # Forward
            linear = sum(w*i for w, i in zip(weights, inputs)) + bias
            
            if mode == 'ternary':
                pred = activation_ternary(linear)
            else:
                pred = activation_binary(linear)
                
            # Backward (Update)
            error = target - pred
            if error != 0:
                errors += 1
                for i in range(3):
                    weights[i] += learning_rate * error * inputs[i]
                bias += learning_rate * error
        
        if errors == 0:
            converged = True
            final_epoch = epoch
            break
            
    dt = time.perf_counter() - start_time
    return converged, final_epoch, dt

def run_bench():
    # ENFORCE DETERMINISM (VSA ZERO POINT)
    random.seed(0)

    print("--- LEARNING PIPELINE ACCELERATION BENCHMARK ---")
    
    # Run Binary
    b_conv, b_ep, b_time = train_perceptron('binary')
    print(f"BINARY (2-State): Converged? {b_conv} | Epochs: {b_ep} | Time: {b_time:.4f}s")
    
    # Run Ternary
    t_conv, t_ep, t_time = train_perceptron('ternary')
    print(f"TERNARY (3-State): Converged? {t_conv} | Epochs: {t_ep} | Time: {t_time:.4f}s")
    
    if b_ep > 0:
        improvement = ((b_ep - t_ep) / b_ep) * 100
        print(f"ACCELERATION: Ternary converged {improvement:.1f}% faster (Epochs).")

if __name__ == "__main__":
    run_bench()
