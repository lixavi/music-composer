# dataset.py
import torch
from torch.utils.data import Dataset
from music_utils import load_midi_files, prepare_sequences
import config

class MusicDataset(Dataset):
    def __init__(self, data_path):
        self.notes = load_midi_files(data_path)
        self.network_input, self.network_output = prepare_sequences(self.notes, config.SEQUENCE_LENGTH)

    def __len__(self):
        return len(self.network_input)

    def __getitem__(self, index):
        return self.network_input[index], self.network_output[index]
