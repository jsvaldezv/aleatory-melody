NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
OCTAVES = list(range(11))
NOTES_IN_OCTAVE = len(NOTES)

errors = {
    "program": "Bad input, please refer this spec-\n"
    "http://www.electronics.dit.ie/staff/tscarff/Music_technology/midi/program_change.htm",
    "notes": "Bad input, please refer this spec-\n"
    "http://www.electronics.dit.ie/staff/tscarff/Music_technology/midi/midi_note_numbers_for_octaves.htm",
}


def number_to_note(number: int) -> tuple:
    octave = number // NOTES_IN_OCTAVE
    assert octave in OCTAVES, errors["notes"]
    assert 0 <= number <= 127, errors["notes"]
    note = NOTES[number % NOTES_IN_OCTAVE]

    return note, octave
