import os
from qiskit_ibm_runtime import QiskitRuntimeService

QiskitRuntimeService.save_account(
    channel="ibm_quantum_platform",
    token=os.environ["IBM_API_KEY"],
    instance=os.environ.get("IBM_CRN"),
    set_as_default=True,
    overwrite=True,
)