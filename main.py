import numpy as np
from random import randint
import rangeNote
import midiToNote
import createMidi

# Generate possible ranges in major scales
MajorScale = np.array([0, 2, 4, 5, 7, 9, 11])
MajorScale = np.append(MajorScale, [[MajorScale + 12 * i] for i in range(1, 9)])

# Calculate note ranges and dedicing root note
note = "C"
scale = rangeNote.calculateRangeNote(note, MajorScale)
print("Scale:", note, "major")

# Define range in octaves
pianoRange = range(21, 109)

# Play and collect random notes
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

print("Notes:", notasFinales)
print("Velocity:", velocityFinales)

# MIDI to musical note
notasName = []
for i in notasFinales:
    notasName.append(midiToNote.number_to_note(i))

print("From MIDI to note:", notasName)

# Create MIDI File
createMidi.createMidiFile(notasFinales, velocityFinales, "melodies/Melody.mid")
