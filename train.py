# train.py
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from dataset import MusicDataset
from model import LSTMModel
import config

def train_model():
    # Load and preprocess data
    dataset = MusicDataset(config.DATA_PATH)
    dataloader = DataLoader(dataset, batch_size=config.BATCH_SIZE, shuffle=True)
    
    # Initialize model
    model = LSTMModel(input_size=config.INPUT_SIZE, hidden_size=config.HIDDEN_SIZE,
                      num_layers=config.NUM_LAYERS, output_size=config.OUTPUT_SIZE)
    
    # Define loss function and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=config.LEARNING_RATE)
    
    # Move model to GPU if available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    
    # Training loop
    for epoch in range(config.NUM_EPOCHS):
        total_loss = 0.0
        hidden = model.init_hidden(config.BATCH_SIZE)
        for inputs, labels in dataloader:
            # Move inputs and labels to GPU if available
            inputs, labels = inputs.to(device), labels.to(device)
            
            # Zero the gradients
            optimizer.zero_grad()
            
            # Forward pass
            outputs, hidden = model(inputs, hidden)
            
            # Calculate loss
            loss = criterion(outputs, torch.max(labels, 1)[1])
            total_loss += loss.item()
            
            # Backward pass and optimization
            loss.backward()
            optimizer.step()
        
        # Print epoch loss
        print(f"Epoch {epoch+1}/{config.NUM_EPOCHS}, Loss: {total_loss}")
