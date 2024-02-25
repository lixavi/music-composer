# music_utils.py
import music21

def save_midi_file(notes, file_path):
    """Save generated notes to a MIDI file."""
    midi_stream = music21.stream.Stream()
    for note in notes:
        if '.' in note:
            chord_notes = note.split('.')
            chord = music21.chord.Chord(chord_notes)
            midi_stream.append(chord)
        else:
            single_note = music21.note.Note(note)
            midi_stream.append(single_note)
    midi_stream.write('midi', fp=file_path)

def plot_music_sequence(notes):
    """Plot the music sequence."""
    music_stream = music21.stream.Stream()
    for note in notes:
        if '.' in note:
            chord_notes = note.split('.')
            chord = music21.chord.Chord(chord_notes)
            music_stream.append(chord)
        else:
            single_note = music21.note.Note(note)
            music_stream.append(single_note)
    music_stream.plot()

def load_midi_file(file_path):
    """Load a MIDI file and extract notes."""
    notes = []
    midi = music21.converter.parse(file_path)
    notes_to_parse = None
    parts = music21.instrument.partitionByInstrument(midi)
    if parts: # file has instrument parts
        notes_to_parse = parts.parts[0].recurse()
    else: # file has notes in a flat structure
        notes_to_parse = midi.flat.notes
    for element in notes_to_parse:
        if isinstance(element, music21.note.Note):
            notes.append(str(element.pitch))
        elif isinstance(element, music21.chord.Chord):
            notes.append('.'.join(str(n) for n in element.pitches))
    return notes
