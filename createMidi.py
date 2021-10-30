from midiutil.MidiFile import MIDIFile

# CREATE MIDI FILE #
def createMidiFile(notas, velocities, inName):
    # create your MIDI object
    mf = MIDIFile(1)  # only 1 track
    track = 0  # the only track

    time = 0  # start at the beginning
    mf.addTrackName(track, time, "Prueba Uno")
    mf.addTempo(track, time, 120)

    cont = 0
    channel = 0
    duration = 1  # 1 beat long
    time = 0  # start on beat 0

    for i in range(len(notas)):
        pitch = notas[cont]
        volume = velocities[cont]
        mf.addNote(track, channel, pitch, time, duration, volume)

        time += 1
        cont += 1

    # write it to disk
    with open("/Users/jsvaldezv/Downloads/" + inName, 'wb') as outf:
        mf.writeFile(outf)