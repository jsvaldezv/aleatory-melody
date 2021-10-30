import numpy as np
from braket.circuits import Circuit
from braket.aws import AwsDevice

# ##### IONQ IMPLEMENTATION #######
# YOU HAVE TU RUN IT WITH AMAZON BRAKET IN THE WEB

def hadamard_circuit(n_qubits):
    circuit = Circuit()
    for i in range(n_qubits):
        circuit.h(i)
    return circuit


def generateNotas(inNum, inRangeLeft, inRangeRight, inType, inLocation):

    countNotas = 0
    notasFinales = []
    countNotas = 0

    while countNotas < inNum:
        m_shots = 1
        result = device.run(state, inLocation, shots=m_shots).result()

        counts = result.measurement_counts.keys()

        list_one = list(counts)
        array_one = np.array([list_one])

        num = array_one[0][0]
        num = int(str(num), 2)

        if int(num) >= inRangeLeft and int(num) <= inRangeRight:
            notasFinales.append(num)
            countNotas += 1

    print(inType, notasFinales)


# DEFINE CIRCUIT
# OBTAIN BUCKET FROM AMAZON BRAKET CONSOLE
my_bucket = "amazon-braket-9a1ba65bbf6c" # the name of the bucket
my_prefix = "Your-Folder-Name" # the name of the folder in the bucket
s3_folder = (my_bucket, my_prefix)

# SPECIFIY CUANTIC MACHINE YOU ARE GOIN TO RUN THE PROGRAM
device = AwsDevice("arn:aws:braket:::device/quantum-simulator/amazon/sv1")
n_qubits = 7
state = hadamard_circuit(n_qubits)

# MAKE RANDOM NUMBERS
print("IONQ")
print("Melodia 1")
generateNotas(16, 21, 109, "Note:", s3_folder)
generateNotas(16, 0, 127, "Velocity:", s3_folder)