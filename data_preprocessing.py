# data_preprocessing.py
import music21
import numpy as np

def load_midi_files(file_paths):
    """Load MIDI files from the given list of file paths."""
    notes = []
    for file_path in file_paths:
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

def prepare_sequences(notes, sequence_length):
    """Prepare sequences used to train the LSTM model."""
    sequence_length = sequence_length
    pitchnames = sorted(set(notes))
    note_to_int = dict((note, number) for number, note in enumerate(pitchnames))
    network_input = []
    network_output = []
    for i in range(0, len(notes) - sequence_length, 1):
        sequence_in = notes[i:i + sequence_length]
        sequence_out = notes[i + sequence_length]
        network_input.append([note_to_int[char] for char in sequence_in])
        network_output.append(note_to_int[sequence_out])
    n_patterns = len(network_input)
    network_input = np.reshape(network_input, (n_patterns, sequence_length, 1))
    network_input = network_input / float(len(set(notes)))
    network_output = np_utils.to_categorical(network_output)
    return (network_input, network_output)
