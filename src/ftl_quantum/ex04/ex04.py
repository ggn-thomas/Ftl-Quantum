from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime import SamplerV2 as Sampler
from qiskit.transpiler import generate_preset_pass_manager

service = QiskitRuntimeService()

# get the first available operational backend that is not a simulator
backend = service.least_busy(simulator=False, operational=True)

# Convert to an ISA circuit and layout-mapped observable
pm = generate_preset_pass_manager(backend=backend, optimization_level=1)

# create a quantum circuit with 2 qubit
qc = QuantumCircuit(2)

#  add a Hadamard gate to the qubit to create superposition
qc.h(0)

# add a CNOT gate to entangle the qubits
qc.cx(0, 1)

# measure all the qubits in the circuit, part of the circuit is to be measured
qc.measure_all()

# translates the circuit into an ISA circuit
isa_circuit = pm.run(qc)

# draw the circuit
print(isa_circuit.draw("mpl", idle_wires=False))

# create a sampler for the backend
sampler = Sampler(mode=backend)

# run the circuit on the sampler with 500 shots and get the result
job = sampler.run([isa_circuit], shots=500)

# print the job ID
print(job.job_id())

# get the result of the job
result = job.result()

# plot the histogram of the measurement results
plot_histogram(result[0].data.meas.get_counts())

plt.show()
