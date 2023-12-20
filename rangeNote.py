def calculateRangeNote(note, MajorScale):
    if note == "C":
        scale = 12 + MajorScale
    elif note == "C#":
        scale = 13 + MajorScale
    elif note == "D":
        scale = 14 + MajorScale
    elif note == "D#":
        scale = 15 + MajorScale
    elif note == "E":
        scale = 16 + MajorScale
    elif note == "F":
        scale = 17 + MajorScale
    elif note == "F#":
        scale = 18 + MajorScale
    elif note == "G":
        scale = 19 + MajorScale
    elif note == "G#":
        scale = 20 + MajorScale
    elif note == "A":
        scale = 21 + MajorScale
    elif note == "A#":
        scale = 22 + MajorScale
    elif note == "B":
        scale = 23 + MajorScale

    return scale
