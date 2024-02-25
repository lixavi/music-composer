# model.py
import torch
import torch.nn as nn

class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(LSTMModel, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.output_size = output_size
        
        # Define LSTM layer
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        
        # Define fully connected layer
        self.fc = nn.Linear(hidden_size, output_size)
        
        # Define activation function
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, x, hidden):
        # Forward pass through LSTM layer
        lstm_out, hidden = self.lstm(x, hidden)
        
        # Only take the output from the final LSTM cell
        lstm_out = lstm_out[:, -1, :]
        
        # Forward pass through fully connected layer
        output = self.fc(lstm_out)
        
        # Apply activation function
        output = self.softmax(output)
        
        return output, hidden

    def init_hidden(self, batch_size):
        # Initialize hidden state and cell state
        weight = next(self.parameters()).data
        hidden = (weight.new(self.num_layers, batch_size, self.hidden_size).zero_().to(device),
                  weight.new(self.num_layers, batch_size, self.hidden_size).zero_().to(device))
        return hidden
