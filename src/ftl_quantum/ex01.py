from qiskit.providers.basic_provider import BasicProvider
from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService()

print("Simulated quantum computers:")
# IBM retired its cloud simulators, so this list is empty on current accounts.
for backend in service.backends(simulator=True):
    print(f"\t{backend.name} has {backend.status().pending_jobs} queues")
# Local simulators run on this machine: they have no queue.
for backend in BasicProvider().backends():
    print(f"\t{backend.name} (local) has 0 queues")

print("\nReal quantum computers:")
for backend in service.backends(simulator=False):
    queue = backend.status().pending_jobs
    print(f"\t{backend.name} has {queue} queues with {backend.num_qubits} qubits")
