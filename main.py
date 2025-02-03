from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

def quantum_random_bit():
    """Returns a truly random 0 or 1 using a quantum circuit."""
    qc = QuantumCircuit(1)
    qc.h(0)  # Put the qubit in superposition

    sampler = StatevectorSampler()
    job = sampler.run([qc])  # Wrap qc in a list
    result = job.result()
    probabilities = result.quasi_dists[0]  # Get probability distribution

    return max(probabilities, key=probabilities.get)  # Return the most probable outcome (0 or 1)

print(quantum_random_bit())  # Output: 0 or 1
