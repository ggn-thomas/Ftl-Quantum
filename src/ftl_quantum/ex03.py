from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# create a quantum circuit with 2 qubit
qc = QuantumCircuit(2)

#  add a Hadamard gate to the qubit to create superposition
qc.h(0)

# add a CNOT gate to entangle the qubits
qc.cx(0, 1)

# measure all the qubits in the circuit, part of the circuit is to be measured
qc.measure_all()

# create a StatevectorSampler instance (object)
sampler = StatevectorSampler()

# draw the circuit
print(qc.draw())

# run the circuit on the sampler with 500 shots and get the result
result = sampler.run([qc], shots=500).result()

# get the counts of the measurement results and plot a histogram
counts = result[0].data.meas.get_counts()

# plot the histogram of the measurement results
plot_histogram(counts)

plt.show()
