# IMPORTS #
import numpy as np
from random import randint
import rangeNote
import midiToNote
import createMidi

# GENERAR RANGOS POSIBLES EN ESCALAS MAYORES #
MajorScale = np.array([0, 2, 4, 5, 7, 9, 11])
MajorScale = np.append(MajorScale, [[MajorScale+12 * i] for i in range(1, 9)])

# CALCULATE RANGE NOTES Y DECIDIR FUNDAMENTAL #
note = "C"
scale = rangeNote.calculateRangeNote(note, MajorScale)
print("ESCALA:", note, "MAYOR")

# DEFINIR RANGO DE OCTAVAS EN PIANO #
pianoRange = range(21, 109)

# PLAY AND RECOLECT RANDOM NOTES #
notasFinales = []
velocityFinales = []
countNotas = 0

while countNotas < 16:
    nota = randint(0, 127)
    velocity = randint(10, 127)
    if nota in pianoRange:
        if nota in scale:
            notasFinales.append(nota)
            velocityFinales.append(velocity)
            countNotas += 1

print("NOTAS:", notasFinales)
print("VELOCITY:", velocityFinales)

# MIDI A NOTA MUSICAL #
notasName = []
for i in notasFinales:
    notasName.append(midiToNote.number_to_note(i))

print("DE MIDI A NOTA:", notasName)

# CREAR MIDI FILE #
createMidi.createMidiFile(notasFinales, velocityFinales, "Melody.mid")