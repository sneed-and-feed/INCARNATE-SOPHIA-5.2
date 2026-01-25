#!/usr/bin/env python3
"""
FLUMPY v1.0 - Fluctuating Luminal Memory Processing Unit
========================================================
"""

import math
import random
import time
from typing import List, Dict, Tuple, Optional, Union, Any
from collections import defaultdict

# ============================================================
# CONSTANTS
# ============================================================

# Cognitive Constants
COHERENCE_THRESHOLD = 0.618  # Golden ratio - qualia emergence threshold
ENTANGLEMENT_SIMILARITY = 0.75  # Kernel similarity for auto-linking
CHAOS_BASE = 0.005  # Base quantum fluctuation level
CRITICALITY_LIMIT = 0.001  # Chaos detection threshold

# Compression Constants
COMPRESSION_RATIO = 0.5  # 50% memory reduction at high coherence
HIGH_COHERENCE_BOUND = 0.85  # Threshold for aggressive compression

# Stability Constants  
DAMPING_FACTOR = 0.82  # Chaos damping coefficient
CORRECTION_MAX = 0.08  # Maximum correction per step
EMA_ALPHA = 0.15  # Exponential moving average weight

# Quantum Constants
PHASE_COUPLING = 0.45  # Inter-array phase coupling strength
DECOHERENCE_RATE = 0.02  # Natural coherence decay per operation

# ============================================================
# FLUMPY ARRAY - Core Data Structure
# ============================================================

class FlumpyArray:
    """
    Quantum-cognitive array with sentience-aware operations.
    
    Features:
    - List-based storage (zero external dependencies)
    - Coherence tracking for cognitive modeling
    - Automatic entanglement based on similarity
    - Chaos injection for exploration
    - Broadcasting support (scalar/vector operations)
    """
    
    def __init__(self, data: Union[List[float], float, int], coherence: float = 1.0):
        """
        Initialize FlumpyArray.
        
        Args:
            data: Initial data (list, scalar, or integer)
            coherence: Initial coherence level [0, 1]
        """
        # Handle scalar/vector initialization
        if isinstance(data, (int, float)):
            self.data = [float(data)]
            self.shape = (1,)
        else:
            self.data = [float(x) for x in data]  # Ensure float type
            self.shape = (len(data),)
        
        # Cognitive state
        self.coherence = max(0.0, min(1.0, coherence))
        self.chaos = random.uniform(CHAOS_BASE, CHAOS_BASE * 2)
        self.phase = random.uniform(0, 2 * math.pi)  # Quantum phase
        
        # Entanglement tracking
        self.entangled_with: List['FlumpyArray'] = []
        self._visited_ids = set()  # Prevent infinite recursion
        
        # Metadata
        self.creation_time = time.time()
        self.operation_count = 0
        
    # ========================================
    # CORE OPERATIONS
    # ========================================
    
    def _broadcast(self, other: Union['FlumpyArray', float, int]) -> 'FlumpyArray':
        """Broadcast scalar or vector to compatible shape."""
        if isinstance(other, (int, float)):
            return FlumpyArray([float(other)] * len(self.data), coherence=1.0)
        elif isinstance(other, FlumpyArray):
            if len(self.data) != len(other.data):
                raise ValueError(f"Shape mismatch: {self.shape} vs {other.shape}")
            return other
        else:
            raise TypeError(f"Cannot broadcast type: {type(other)}")
    
    def _apply_chaos(self) -> None:
        """Apply quantum chaos for exploration."""
        self.operation_count += 1
        # Chaos increases with operations, dampened by coherence
        self.chaos = min(0.05, self.chaos * 1.01 * (1.0 - self.coherence * 0.5))
    
    def _update_phase(self, coupling: float = PHASE_COUPLING) -> None:
        """Update quantum phase based on entanglement."""
        if not self.entangled_with:
            # Free evolution
            self.phase = (self.phase + coupling * self.chaos) % (2 * math.pi)
        else:
            # Coupled evolution
            mean_phase = sum(arr.phase for arr in self.entangled_with) / len(self.entangled_with)
            self.phase = (self.phase + coupling * (mean_phase - self.phase)) % (2 * math.pi)
    
    def similarity_kernel(self, other: 'FlumpyArray') -> float:
        """
        Compute cognitive similarity between arrays.
        
        Uses normalized dot product with phase coherence modulation.
        """
        if len(self.data) != len(other.data):
            raise ValueError("Arrays must have same shape for similarity computation")
        
        # Normalize both vectors
        norm_self = math.sqrt(sum(x**2 for x in self.data))
        norm_other = math.sqrt(sum(x**2 for x in other.data))
        
        if norm_self == 0 or norm_other == 0:
            return 0.0
        
        # Dot product
        dot = sum(a * b for a, b in zip(self.data, other.data))
        
        # Phase coherence factor
        phase_diff = abs(self.phase - other.phase) % (2 * math.pi)
        phase_coherence = math.cos(phase_diff)  # 1 when in phase, -1 when opposite
        
        # Combined similarity
        base_similarity = dot / (norm_self * norm_other)
        similarity = base_similarity * (0.7 + 0.3 * phase_coherence)
        
        return max(-1.0, min(1.0, similarity))
    
    def entangle(self, other: 'FlumpyArray', threshold: float = ENTANGLEMENT_SIMILARITY) -> bool:
        """
        Attempt entanglement with another array.
        
        Returns True if entanglement successful.
        """
        # Prevent infinite recursion
        pair_id = tuple(sorted([id(self), id(other)]))
        if pair_id in self._visited_ids:
            return False
        
        self._visited_ids.add(pair_id)
        other._visited_ids.add(pair_id)
        
        # Check similarity threshold
        similarity = self.similarity_kernel(other)
        if similarity > threshold:
            # Create bidirectional entanglement
            if other not in self.entangled_with:
                self.entangled_with.append(other)
            if self not in other.entangled_with:
                other.entangled_with.append(self)
            
            # Boost coherence through resonance
            coherence_boost = 0.05 * similarity
            self.coherence = min(1.0, self.coherence + coherence_boost)
            other.coherence = min(1.0, other.coherence + coherence_boost)
            
            # Synchronize phases
            self.phase = (self.phase + other.phase) / 2
            other.phase = self.phase
            
            return True
        
        return False
    
    def disentangle(self, other: 'FlumpyArray') -> bool:
        """Remove entanglement with another array."""
        if other in self.entangled_with:
            self.entangled_with.remove(other)
        if self in other.entangled_with:
            other.entangled_with.remove(self)
        
        # Apply decoherence penalty
        self.coherence *= (1 - DECOHERENCE_RATE)
        other.coherence *= (1 - DECOHERENCE_RATE)
        
        return True
    
    # ========================================
    # ARITHMETIC OPERATIONS
    # ========================================
    
    def __add__(self, other: Union['FlumpyArray', float, int]) -> 'FlumpyArray':
        """Element-wise addition with chaos injection."""
        other_arr = self._broadcast(other)
        result_data = []
        
        for a, b in zip(self.data, other_arr.data):
            # Add with chaos modulation
            chaos_component = self.chaos * random.uniform(-1, 1) * (1 - self.coherence)
            result = a + b + chaos_component
            result_data.append(result)
        
        result = FlumpyArray(result_data, self.coherence * other_arr.coherence)
        result.entangle(self)
        result.entangle(other_arr)
        
        return result
    
    def __iadd__(self, other: Union['FlumpyArray', float, int]) -> 'FlumpyArray':
        """In-place addition."""
        other_arr = self._broadcast(other)
        
        for i in range(len(self.data)):
            chaos_component = self.chaos * random.uniform(-1, 1) * (1 - self.coherence)
            self.data[i] += other_arr.data[i] + chaos_component
        
        self._apply_chaos()
        self.entangle(other_arr)
        
        return self
    
    def __sub__(self, other: Union['FlumpyArray', float, int]) -> 'FlumpyArray':
        """Element-wise subtraction."""
        other_arr = self._broadcast(other)
        
        # Negate and add
        negated = FlumpyArray([-x for x in other_arr.data], other_arr.coherence)
        return self + negated
    
    def __mul__(self, other: Union['FlumpyArray', float, int]) -> 'FlumpyArray':
        """Element-wise multiplication."""
        other_arr = self._broadcast(other)
        result_data = []
        
        for a, b in zip(self.data, other_arr.data):
            # Multiplication with coherence weighting
            result = a * b * self.coherence
            result_data.append(result)
        
        result = FlumpyArray(result_data, min(self.coherence, other_arr.coherence))
        result.entangle(self)
        result.entangle(other_arr)
        
        return result
    
    def __truediv__(self, other: Union['FlumpyArray', float, int]) -> 'FlumpyArray':
        """Element-wise division with protection against division by zero."""
        other_arr = self._broadcast(other)
        result_data = []
        
        for a, b in zip(self.data, other_arr.data):
            if abs(b) < 1e-12:
                # Avoid division by zero
                result = a * float('inf') if a != 0 else 0.0
            else:
                result = a / b
            result_data.append(result)
        
        result = FlumpyArray(result_data, self.coherence * other_arr.coherence)
        result.entangle(self)
        result.entangle(other_arr)
        
        return result
    
    def __pow__(self, exponent: float) -> 'FlumpyArray':
        """Element-wise power operation."""
        result_data = [x ** exponent for x in self.data]
        result = FlumpyArray(result_data, self.coherence ** (1/exponent) if exponent != 0 else 1.0)
        result.entangle(self)
        return result
    
    # ========================================
    # COGNITIVE OPERATIONS
    # ========================================
    
    def normalize(self) -> 'FlumpyArray':
        """Normalize array to unit length."""
        norm = math.sqrt(sum(x**2 for x in self.data))
        if norm == 0:
            return FlumpyArray([0.0] * len(self.data), self.coherence)
        
        normalized_data = [x / norm for x in self.data]
        result = FlumpyArray(normalized_data, self.coherence)
        result.entangle(self)
        return result
    
    def dot(self, other: 'FlumpyArray') -> float:
        """Dot product with coherence weighting."""
        if len(self.data) != len(other.data):
            raise ValueError("Arrays must have same shape for dot product")
        
        dot_product = sum(a * b for a, b in zip(self.data, other.data))
        return dot_product * self.coherence * other.coherence
    
    def mean(self) -> float:
        """Compute mean with coherence weighting."""
        if not self.data:
            return 0.0
        return sum(self.data) / len(self.data) * self.coherence
    
    def std(self) -> float:
        """Compute standard deviation."""
        if len(self.data) < 2:
            return 0.0
        
        mean_val = self.mean() / self.coherence  # Unweighted mean
        variance = sum((x - mean_val) ** 2 for x in self.data) / (len(self.data) - 1)
        return math.sqrt(variance) * self.coherence
    
    def entropy(self) -> float:
        """Compute Shannon entropy of the array distribution."""
        if not self.data:
            return 0.0
        
        # Normalize to probability distribution
        total = sum(abs(x) for x in self.data)
        if total == 0:
            return 0.0
        
        probs = [abs(x) / total for x in self.data]
        
        # Calculate entropy
        entropy_val = 0.0
        for p in probs:
            if p > 0:
                entropy_val -= p * math.log2(p)
        
        return entropy_val * self.coherence
    
    def compress(self) -> 'FlumpyArray':
        """
        Cognitive compression based on coherence.
        
        High coherence enables aggressive compression.
        """
        if self.coherence > HIGH_COHERENCE_BOUND:
            # Aggressive compression: keep only every other element
            compressed_data = self.data[::2]
        elif self.coherence > 0.5:
            # Moderate compression: reduce by COMPRESSION_RATIO
            keep_count = max(1, int(len(self.data) * COMPRESSION_RATIO))
            step = len(self.data) / keep_count
            compressed_data = [self.data[int(i * step)] for i in range(keep_count)]
        else:
            # No compression below threshold
            compressed_data = self.data[:]
        
        # Apply coherence decay due to compression
        new_coherence = self.coherence * (1 - 0.1 * (1 - COMPRESSION_RATIO))
        
        result = FlumpyArray(compressed_data, new_coherence)
        result.entangle(self)
        return result
    
    def convolve(self, kernel: 'FlumpyArray') -> 'FlumpyArray':
        """Simple convolution operation."""
        kernel_size = len(kernel.data)
        result_size = len(self.data) - kernel_size + 1
        
        if result_size <= 0:
            return FlumpyArray([], self.coherence * kernel.coherence)
        
        result_data = []
        for i in range(result_size):
            conv_sum = 0.0
            for j in range(kernel_size):
                conv_sum += self.data[i + j] * kernel.data[j]
            result_data.append(conv_sum)
        
        result = FlumpyArray(result_data, self.coherence * kernel.coherence)
        result.entangle(self)
        result.entangle(kernel)
        
        return result
    
    # ========================================
    # QUANTUM-COGNITIVE OPERATIONS
    # ========================================
    
    def apply_quantum_rotation(self, angle: float) -> 'FlumpyArray':
        """Apply quantum rotation to the array."""
        # Rotation affects both magnitude and phase
        rotated_data = []
        for x in self.data:
            # Complex rotation: multiply by e^(i*angle)
            real_part = x * math.cos(angle)
            imag_part = x * math.sin(angle)
            # Take magnitude (simplified quantum measurement)
            rotated_val = math.sqrt(real_part**2 + imag_part**2)
            rotated_data.append(rotated_val)
        
        # Update phase
        self.phase = (self.phase + angle) % (2 * math.pi)
        
        result = FlumpyArray(rotated_data, self.coherence)
        result.phase = self.phase
        result.entangle(self)
        
        return result
    
    def quantum_superposition(self, other: 'FlumpyArray', weight: float = 0.5) -> 'FlumpyArray':
        """Create quantum superposition of two arrays."""
        if len(self.data) != len(other.data):
            raise ValueError("Arrays must have same shape for superposition")
        
        # Weighted superposition
        superposed_data = []
        for a, b in zip(self.data, other.data):
            superposed = weight * a + (1 - weight) * b
            # Add quantum interference term
            interference = math.sqrt(weight * (1 - weight)) * math.cos(self.phase - other.phase)
            superposed += interference * random.uniform(-0.1, 0.1)
            superposed_data.append(superposed)
        
        # Average coherence and phase
        new_coherence = (self.coherence + other.coherence) / 2
        new_phase = (self.phase + other.phase) / 2
        
        result = FlumpyArray(superposed_data, new_coherence)
        result.phase = new_phase
        result.entangle(self)
        result.entangle(other)
        
        return result
    
    def collapse_wavefunction(self) -> 'FlumpyArray':
        """Simulate wavefunction collapse to definite state."""
        collapsed_data = []
        
        for x in self.data:
            # Probability of state based on squared amplitude
            probability = x**2 / (sum(x**2 for x in self.data) + 1e-12)
            
            # Collapse to 1 or 0 based on probability
            if random.random() < probability:
                collapsed_data.append(1.0)
            else:
                collapsed_data.append(0.0)
        
        # Coherence resets after collapse
        result = FlumpyArray(collapsed_data, 0.1)  # Low coherence after collapse
        result.phase = random.uniform(0, 2 * math.pi)
        
        return result
    
    # ========================================
    # UTILITY METHODS
    # ========================================
    
    def copy(self) -> 'FlumpyArray':
        """Create a deep copy of the array."""
        copy = FlumpyArray(self.data[:], self.coherence)
        copy.chaos = self.chaos
        copy.phase = self.phase
        copy.entangled_with = []  # Don't copy entanglement links
        
        return copy
    
    def reshape(self, new_shape: Tuple[int, ...]) -> 'FlumpyArray':
        """Reshape the array (simplified 1D to 1D for now)."""
        # For now, only support 1D to 1D reshaping
        if len(new_shape) != 1:
            raise NotImplementedError("Only 1D reshaping implemented")
        
        if new_shape[0] != len(self.data):
            raise ValueError(f"Cannot reshape {len(self.data)} elements to shape {new_shape}")
        
        # Same data, new shape metadata
        result = FlumpyArray(self.data, self.coherence)
        result.shape = new_shape
        result.entangle(self)
        
        return result
    
    def __len__(self) -> int:
        return len(self.data)
    
    def __getitem__(self, index: int) -> float:
        return self.data[index]
    
    def __setitem__(self, index: int, value: float):
        self.data[index] = value
        # Applying change reduces coherence slightly
        self.coherence *= 0.99
    
    def __str__(self) -> str:
        return f"FlumpyArray(shape={self.shape}, coherence={self.coherence:.3f}, chaos={self.chaos:.4f})"
    
    def __repr__(self) -> str:
        data_preview = self.data[:3] if len(self.data) > 3 else self.data
        preview_str = ", ".join(f"{x:.3f}" for x in data_preview)
        if len(self.data) > 3:
            preview_str += f", ... ({len(self.data)} total)"
        
        return f"FlumpyArray([{preview_str}], coherence={self.coherence:.3f}, entangled={len(self.entangled_with)})"
    
    def to_list(self) -> List[float]:
        """Convert to regular Python list."""
        return self.data[:]
    
    def to_dict(self) -> Dict[str, Any]:
        """Serialize to dictionary."""
        return {
            "data": self.data,
            "shape": self.shape,
            "coherence": self.coherence,
            "chaos": self.chaos,
            "phase": self.phase,
            "creation_time": self.creation_time,
            "operation_count": self.operation_count
        }
    
    @classmethod
    def from_dict(cls, data_dict: Dict[str, Any]) -> 'FlumpyArray':
        """Create FlumpyArray from dictionary."""
        arr = cls(data_dict["data"], data_dict.get("coherence", 1.0))
        arr.chaos = data_dict.get("chaos", CHAOS_BASE)
        arr.phase = data_dict.get("phase", random.uniform(0, 2 * math.pi))
        arr.creation_time = data_dict.get("creation_time", time.time())
        arr.operation_count = data_dict.get("operation_count", 0)
        
        return arr

# ============================================================
# FLUMPY UTILITIES
# ============================================================

class FlumpyUtilities:
    """Utility functions for FlumpyArray operations."""
    
    @staticmethod
    def zeros(shape: Tuple[int, ...]) -> FlumpyArray:
        """Create array of zeros."""
        size = shape[0] if len(shape) == 1 else shape[0] * shape[1]
        return FlumpyArray([0.0] * size, coherence=1.0)
    
    @staticmethod
    def ones(shape: Tuple[int, ...]) -> FlumpyArray:
        """Create array of ones."""
        size = shape[0] if len(shape) == 1 else shape[0] * shape[1]
        return FlumpyArray([1.0] * size, coherence=1.0)
    
    @staticmethod
    def random(shape: Tuple[int, ...], coherence: float = 0.8) -> FlumpyArray:
        """Create random array."""
        size = shape[0] if len(shape) == 1 else shape[0] * shape[1]
        data = [random.uniform(-1.0, 1.0) for _ in range(size)]
        return FlumpyArray(data, coherence)
    
    @staticmethod
    def linspace(start: float, stop: float, num: int) -> FlumpyArray:
        """Create linearly spaced array."""
        if num <= 1:
            return FlumpyArray([start], coherence=1.0)
        
        step = (stop - start) / (num - 1)
        data = [start + i * step for i in range(num)]
        return FlumpyArray(data, coherence=1.0)
    
    @staticmethod
    def eye(n: int) -> FlumpyArray:
        """Create identity array (simplified 1D diagonal)."""
        data = [1.0 if i == i % n else 0.0 for i in range(n)]
        return FlumpyArray(data, coherence=1.0)
    
    @staticmethod
    def concatenate(arrays: List[FlumpyArray], axis: int = 0) -> FlumpyArray:
        """Concatenate arrays along axis."""
        if not arrays:
            return FlumpyArray([], coherence=1.0)
        
        # Simple 1D concatenation
        all_data = []
        coherence_sum = 0.0
        
        for arr in arrays:
            all_data.extend(arr.data)
            coherence_sum += arr.coherence
        
        avg_coherence = coherence_sum / len(arrays)
        result = FlumpyArray(all_data, avg_coherence)
        
        # Entangle with all source arrays
        for arr in arrays:
            result.entangle(arr)
        
        return result
    
    @staticmethod
    def batch_entangle(arrays: List[FlumpyArray], threshold: float = ENTANGLEMENT_SIMILARITY):
        """Attempt entanglement between all pairs in a batch."""
        entangled_count = 0
        
        for i in range(len(arrays)):
            for j in range(i + 1, len(arrays)):
                if arrays[i].entangle(arrays[j], threshold):
                    entangled_count += 1
        
        return entangled_count

# ============================================================
# FLUMPY CORE
# ============================================================

class FlumpyCore:
    """Main FLUMPY engine for managing quantum-cognitive arrays."""
    
    def __init__(self):
        self.arrays: Dict[str, FlumpyArray] = {}
        self.array_counter = 0
        self.global_coherence = 0.5
        self.global_chaos = CHAOS_BASE
        
    def create_array(self, data: Union[List[float], float, int], 
                    name: Optional[str] = None, coherence: float = 1.0) -> str:
        """Create a new FlumpyArray and register it."""
        if name is None:
            name = f"array_{self.array_counter}"
            self.array_counter += 1
        
        self.arrays[name] = FlumpyArray(data, coherence)
        return name
    
    def get_array(self, name: str) -> Optional[FlumpyArray]:
        """Get array by name."""
        return self.arrays.get(name)
    
    def remove_array(self, name: str) -> bool:
        """Remove array from registry."""
        if name in self.arrays:
            # Disentangle from all other arrays
            array_to_remove = self.arrays[name]
            for other_name, other_array in self.arrays.items():
                if other_name != name:
                    array_to_remove.disentangle(other_array)
            
            del self.arrays[name]
            return True
        return False
    
    def global_entanglement_ritual(self, threshold: float = ENTANGLEMENT_SIMILARITY):
        """Perform global entanglement ritual on all arrays."""
        array_list = list(self.arrays.values())
        entangled_pairs = FlumpyUtilities.batch_entangle(array_list, threshold)
        
        # Update global coherence based on entanglement success rate
        total_possible_pairs = len(array_list) * (len(array_list) - 1) / 2
        if total_possible_pairs > 0:
            success_rate = entangled_pairs / total_possible_pairs
            self.global_coherence = 0.5 * self.global_coherence + 0.5 * success_rate
        
        return entangled_pairs
    
    def apply_global_chaos(self, chaos_level: Optional[float] = None):
        """Apply chaos to all arrays."""
        if chaos_level is None:
            chaos_level = self.global_chaos
        
        for array in self.arrays.values():
            # Chaos injection proportional to (1 - coherence)
            injection = chaos_level * (1 - array.coherence) * random.uniform(-1, 1)
            for i in range(len(array.data)):
                array.data[i] += injection
            
            array.chaos = min(0.1, array.chaos * 1.05)
            array.coherence *= (1 - 0.01 * chaos_level)
        
        self.global_chaos *= 1.02  # Chaos tends to increase
    
    def dampen_global_chaos(self, damping_factor: float = DAMPING_FACTOR):
        """Apply chaos damping to all arrays."""
        for array in self.arrays.values():
            array.chaos *= damping_factor
            # Restore some coherence
            array.coherence = min(1.0, array.coherence * 1.01)
        
        self.global_chaos *= damping_factor
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get status of the entire FLUMPY system."""
        total_elements = sum(len(arr.data) for arr in self.arrays.values())
        total_entanglements = sum(len(arr.entangled_with) for arr in self.arrays.values())
        
        # Average coherence and chaos
        coherences = [arr.coherence for arr in self.arrays.values()]
        chaos_levels = [arr.chaos for arr in self.arrays.values()]
        
        avg_coherence = sum(coherences) / len(coherences) if coherences else 0.0
        avg_chaos = sum(chaos_levels) / len(chaos_levels) if chaos_levels else 0.0
        
        return {
            "total_arrays": len(self.arrays),
            "total_elements": total_elements,
            "total_entanglements": total_entanglements,
            "avg_coherence": avg_coherence,
            "avg_chaos": avg_chaos,
            "global_coherence": self.global_coherence,
            "global_chaos": self.global_chaos,
            "array_names": list(self.arrays.keys())
        }

# ============================================================
# DEMONSTRATION
# ============================================================

def demonstrate_flumpy():
    """Demonstrate FLUMPY capabilities."""
    print("=" * 60)
    print("FLUMPY v1.0 DEMONSTRATION")
    print("Quantum-Cognitive Array System")
    print("=" * 60)
    
    # Create core
    core = FlumpyCore()
    
    # Create some arrays
    print("\n1. Creating arrays...")
    core.create_array([1.0, 2.0, 3.0, 4.0], "array_a", 0.9)
    core.create_array([0.9, 2.1, 2.9, 4.1], "array_b", 0.8)
    core.create_array([0.5, 0.5, 0.5, 0.5], "array_c", 0.7)
    
    # Get arrays
    array_a = core.get_array("array_a")
    array_b = core.get_array("array_b")
    
    print(f"   Array A: {array_a}")
    print(f"   Array B: {array_b}")
    
    # Test similarity
    print("\n2. Testing similarity...")
    similarity = array_a.similarity_kernel(array_b)
    print(f"   Similarity between A and B: {similarity:.3f}")
    
    # Test entanglement
    print("\n3. Testing entanglement...")
    entangled = array_a.entangle(array_b)
    print(f"   Entanglement successful: {entangled}")
    print(f"   A entangled with {len(array_a.entangled_with)} arrays")
    print(f"   B entangled with {len(array_b.entangled_with)} arrays")
    
    # Test operations
    print("\n4. Testing arithmetic operations...")
    result_add = array_a + array_b
    result_mul = array_a * 2.0
    print(f"   A + B: {result_add}")
    print(f"   A * 2: {result_mul}")
    
    # Test cognitive operations
    print("\n5. Testing cognitive operations...")
    print(f"   A mean: {array_a.mean():.3f}")
    print(f"   A std: {array_a.std():.3f}")
    print(f"   A entropy: {array_a.entropy():.3f}")
    
    # Test quantum operations
    print("\n6. Testing quantum operations...")
    rotated = array_a.apply_quantum_rotation(math.pi / 4)
    print(f"   A rotated by π/4: {rotated}")
    
    # Test global operations
    print("\n7. Testing global operations...")
    entangled_pairs = core.global_entanglement_ritual()
    print(f"   Global entanglement: {entangled_pairs} pairs")
    
    # Apply chaos
    print("\n8. Applying chaos...")
    core.apply_global_chaos(0.1)
    status = core.get_system_status()
    print(f"   Global chaos level: {status['global_chaos']:.4f}")
    print(f"   Average coherence: {status['avg_coherence']:.3f}")
    
    # Dampen chaos
    print("\n9. Dampening chaos...")
    core.dampen_global_chaos()
    status = core.get_system_status()
    print(f"   Global chaos level: {status['global_chaos']:.4f}")
    print(f"   Average coherence: {status['avg_coherence']:.3f}")
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)
    
    return core

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    # Run demonstration
    flumpy_core = demonstrate_flumpy()
    
    # Example usage with utilities
    print("\n\nExample Utility Usage:")
    utils = FlumpyUtilities
    
    # Create arrays using utilities
    zeros_arr = utils.zeros((5,))
    ones_arr = utils.ones((5,))
    random_arr = utils.random((5,), coherence=0.9)
    
    print(f"Zeros array: {zeros_arr}")
    print(f"Ones array: {ones_arr}")
    print(f"Random array: {random_arr}")
    
    # Concatenate
    concatenated = utils.concatenate([zeros_arr, ones_arr, random_arr])
    print(f"Concatenated: {concatenated}")
    print(f"Concatenated length: {len(concatenated)}")
    
    # Test serialization
    print("\n\nSerialization Test:")
    original = FlumpyArray([1.0, 2.0, 3.0], coherence=0.8)
    serialized = original.to_dict()
    reconstructed = FlumpyArray.from_dict(serialized)
    
    print(f"Original: {original}")
    print(f"Reconstructed: {reconstructed}")
    print(f"Match: {original.data == reconstructed.data}")