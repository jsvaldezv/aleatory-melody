# IMPORTS
from braket.circuits import Circuit
from braket.devices import LocalSimulator
from AleatoryMelody import midiToNote
from AleatoryMelody import createMidi
from AleatoryMelody import rangeNote
import numpy as np

# ############# SIMULATOR IMPLEMENTATION #######
# YOU CAN RUN IT EVERYWHERE, JUST INSTALL THE LIBRARIES
def hadamard_circuit(n_qubits):
    circuit = Circuit()
    for i in range(n_qubits):
        circuit.h(i)
    return circuit


def generateNotas(inNum, inRangeLeft, inRangeRight, inType):

    countNotas = 0
    notasFinales = []
    countNotas = 0
    rangeIn = range(inRangeLeft, inRangeRight)

    while countNotas < inNum:
        m_shots = 1
        result = device.run(state, shots=m_shots).result()
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
    return notasFinales


# DEFINE CIRCUIT AND QUBITS
device = LocalSimulator()
n_qubits = 7
state = hadamard_circuit(n_qubits)

# GENERAR RANGOS POSIBLES EN ESCALAS MAYORES #
MajorScale = np.array([0, 2, 4, 5, 7, 9, 11])
MajorScale = np.append(MajorScale, [[MajorScale+12 * i] for i in range(1, 9)])
scale = rangeNote.calculateRangeNote("C", MajorScale)

# MAKE RANDOM NUMBERS
print("LOCAL SIMULATOR")
notasFinales = generateNotas(16, 21, 109, "Note:")
velocityFinales = generateNotas(16, 10, 127, "Velocity:")

# MIDI A NOTA MUSICAL #
notasName = []
for i in notasFinales:
    notasName.append(midiToNote.number_to_note(i))

print("DE MIDI A NOTA:", notasName)

# CREAR MIDI FILE #
createMidi.createMidiFile(notasFinales, velocityFinales, "Melody.mid")