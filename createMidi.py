from midiutil.MidiFile import MIDIFile


# Create midi file
def createMidiFile(notas, velocities, inName):
    mf = MIDIFile(1)
    track = 0

    time = 0
    mf.addTrackName(track, time, "Test One")
    mf.addTempo(track, time, 120)

    cont = 0
    channel = 0
    duration = 1
    time = 0

    for i in range(len(notas)):
        pitch = notas[cont]
        volume = velocities[cont]
        mf.addNote(track, channel, pitch, time, duration, volume)

        time += 1
        cont += 1

    # Write it to disk
    with open("melodies/" + inName, "wb") as outf:
        mf.writeFile(outf)
