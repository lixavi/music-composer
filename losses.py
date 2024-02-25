# losses.py
import torch
import torch.nn as nn

def custom_loss(outputs, labels):
    """Custom loss function."""
    loss = nn.CrossEntropyLoss()
    return loss(outputs, labels)

def weighted_loss(outputs, labels):
    """Weighted loss function."""
    class_weights = torch.tensor([1.0, 2.0])  # Example class weights
    loss = nn.CrossEntropyLoss(weight=class_weights)
    return loss(outputs, labels)
