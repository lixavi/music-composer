# config.py

# Data
DATA_PATH = "path/to/music/data"

# Model
INPUT_SIZE = 100
HIDDEN_SIZE = 128
NUM_LAYERS = 2
OUTPUT_SIZE = 100

# Training
BATCH_SIZE = 64
NUM_EPOCHS = 50
LEARNING_RATE = 0.001

# Generation
SEQUENCE_LENGTH = 50
GENERATION_LENGTH = 100

# Model Saving and Loading
MODEL_PATH = "path/to/saved/model/model.pth"

# Note to Integer Mapping (for dataset preparation)
NOTE_TO_INT = {
    "C": 0,
    "C#": 1,
    "D": 2,
    "D#": 3,
    "E": 4,
    "F": 5,
    "F#": 6,
    "G": 7,
    "G#": 8,
    "A": 9,
    "A#": 10,
    "B": 11
}

# Integer to Note Mapping (for sequence generation)
INT_TO_NOTE = {v: k for k, v in NOTE_TO_INT.items()}
