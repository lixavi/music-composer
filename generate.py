# generate.py
import torch
from model import LSTMModel
import config

def generate_music():
    # Load trained model
    model = LSTMModel(input_size=config.INPUT_SIZE, hidden_size=config.HIDDEN_SIZE,
                      num_layers=config.NUM_LAYERS, output_size=config.OUTPUT_SIZE)
    model.load_state_dict(torch.load(config.MODEL_PATH))
    model.eval()

    # Generate initial input sequence
    initial_input = torch.rand(1, config.SEQUENCE_LENGTH, config.INPUT_SIZE)

    # Move model to GPU if available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    initial_input = initial_input.to(device)

    # Generate music sequence
    generated_sequence = []
    hidden = model.init_hidden(1)
    with torch.no_grad():
        for _ in range(config.GENERATION_LENGTH):
            output, hidden = model(initial_input, hidden)
            _, predicted = torch.max(output, 1)
            generated_sequence.append(predicted.item())
            initial_input = torch.cat((initial_input[:, 1:, :], output.unsqueeze(0)), dim=1)

    # Convert numerical representation back to notes/chords
    generated_notes = [config.INT_TO_NOTE[i] for i in generated_sequence]

    # Print generated music sequence
    print("Generated Music Sequence:")
    print(generated_notes)
