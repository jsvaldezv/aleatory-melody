import numpy as np
from AleatoryMelody import rangeNote
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
    rangeIn = range(inRangeLeft, inRangeRight)

    while countNotas < inNum:
        m_shots = 1
        result = device.run(state, inLocation, shots=m_shots).result()

        counts = result.measurement_counts.keys()

        list_one = list(counts)
        array_one = np.array([list_one])

        num = array_one[0][0]
        num = int(str(num), 2)

        if int(num) in rangeIn:
            if inType == "Note:":
                if int(num) in scale:
                    notasFinales.append(num)
                    countNotas += 1
            elif inType == "Velocity:":
                notasFinales.append(num)
                countNotas += 1

    print(inType, notasFinales)


# GENERAR RANGOS POSIBLES EN ESCALAS MAYORES #
MajorScale = np.array([0, 2, 4, 5, 7, 9, 11])
MajorScale = np.append(MajorScale, [[MajorScale + 12 * i] for i in range(1, 9)])
scale = rangeNote.calculateRangeNote("C", MajorScale)

# DEFINE CIRCUIT
# OBTAIN BUCKET FROM AMAZON BRAKET CONSOLE
my_bucket = "amazon-braket-9a1ba65bbf6c"  # the name of the bucket
my_prefix = "Your-Folder-Name"  # the name of the folder in the bucket
s3_folder = (my_bucket, my_prefix)

# SPECIFIY CUANTIC MACHINE YOU ARE GOIN TO RUN THE PROGRAM
device = AwsDevice("arn:aws:braket:::device/quantum-simulator/amazon/sv1")
n_qubits = 7
state = hadamard_circuit(n_qubits)

# MAKE RANDOM NUMBERS
print("IONQ")
print("Melodia 1")
generateNotas(16, 21, 109, "Note:", s3_folder)
generateNotas(16, 10, 127, "Velocity:", s3_folder)

"""
IONQ
Melodia 1
Note: [67, 84, 88, 103, 24, 43, 40, 52, 62, 76, 88, 84, 95, 59, 47, 57]
Velocity: [110, 87, 41, 59, 59, 57, 38, 75, 21, 25, 123, 75, 39, 93, 20, 19]
Melodia 2
Note: [88, 72, 38, 98, 74, 77, 69, 95, 31, 41, 81, 79, 33, 65, 71, 21]
Velocity: [101, 121, 69, 56, 32, 102, 61, 35, 27, 56, 106, 42, 46, 55, 48, 26]
Melodia 3
Note: [98, 100, 59, 101, 79, 86, 62, 62, 26, 35, 45, 65, 101, 47, 101, 62]
Velocity: [93, 116, 47, 36, 36, 19, 39, 62, 63, 17, 30, 105, 35, 29, 111, 82]
Melodia 4
Note: [93, 95, 57, 47, 50, 89, 65, 28, 86, 98, 26, 50, 98, 60, 31, 55]
Velocity: [108, 112, 22, 12, 125, 92, 30, 83, 122, 47, 58, 95, 119, 75, 71, 40]
Melodia 5
Note: [67, 107, 77, 29, 41, 43, 91, 36, 65, 40, 77, 60, 53, 98, 59, 57]
Velocity: [26, 119, 92, 14, 119, 33, 27, 82, 102, 115, 52, 101, 35, 51, 124, 23]
Melodia 6
Note: [108, 26, 76, 89, 95, 88, 65, 33, 62, 65, 35, 47, 35, 45, 108, 69]
Velocity: [16, 31, 12, 120, 45, 78, 126, 86, 73, 54, 76, 42, 70, 72, 25, 72]
"""
