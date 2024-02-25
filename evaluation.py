# evaluation.py
import music21
import numpy as np
import config

def evaluate_music_quality(generated_notes):
    """Evaluate the quality of generated music sequences."""
    # Convert generated notes to a music21 stream
    generated_stream = music21.stream.Stream()
    for note in generated_notes:
        if '.' in note:
            chord_notes = note.split('.')
            chord = music21.chord.Chord(chord_notes)
            generated_stream.append(chord)
        else:
            single_note = music21.note.Note(note)
            generated_stream.append(single_note)
    
    # Calculate average pitch range of generated music
    pitch_range = calculate_pitch_range(generated_stream)
    
    # Calculate average note duration of generated music
    note_duration = calculate_note_duration(generated_stream)
    
    # Print evaluation metrics
    print("Evaluation Metrics:")
    print(f"Average Pitch Range: {pitch_range}")
    print(f"Average Note Duration: {note_duration}")

def calculate_pitch_range(music_stream):
    """Calculate the pitch range of the music."""
    pitches = [note.pitch.midi for note in music_stream.flat.notes]
    pitch_range = max(pitches) - min(pitches)
    return pitch_range

def calculate_note_duration(music_stream):
    """Calculate the average note duration of the music."""
    durations = [note.duration.quarterLength for note in music_stream.flat.notes]
    avg_duration = np.mean(durations)
    return avg_duration
