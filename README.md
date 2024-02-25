# Music Composer

Music Composer is a Python-based program that employs LSTM (Long Short-Term Memory) networks to generate unique musical sequences. This tool can be used to create original music compositions or assist musicians in the creative process.

## Features

- **Data Preprocessing**: Load MIDI files, extract musical notes and chords, and prepare sequences for training the LSTM model.
- **Model Training**: Train the LSTM model using preprocessed music data to learn the patterns and structure of musical sequences.
- **Music Generation**: Generate new musical sequences using the trained LSTM model, allowing for the creation of original compositions.
- **Evaluation**: Evaluate the quality of the generated music sequences based on metrics such as pitch range and note duration.
- **User Interaction**: Interact with the program through a command-line interface to generate music and control the process.

## Files and Components

The program consists of the following components and files:

1. **main.py**: The main entry point of the program that orchestrates the training, generation, evaluation, and user interaction.
2. **data_preprocessing.py**: Handles preprocessing of music data, including loading MIDI files and preparing sequences.
3. **model.py**: Defines the LSTM model architecture for music generation.
4. **train.py**: Trains the LSTM model using preprocessed music data.
5. **generate.py**: Generates new musical sequences using the trained model.
6. **evaluation.py**: Evaluates the quality of the generated music sequences.
7. **music_utils.py**: Utility functions for handling music data, such as saving MIDI files and plotting music sequences.
8. **config.py**: Configuration parameters for the model, training process, and data handling.
9. **dataset.py**: Dataset class for loading and preprocessing music data.
10. **losses.py**: Custom loss functions for training the LSTM model.

## Usage

To use the Music Composer program:

1. Install the required dependencies listed in `requirements.txt`.
2. Prepare your music dataset in MIDI format and specify the data path in `config.py`.
3. Run `main.py` to train the model, generate music, and interact with the program.

## Future Improvements

- Implement more sophisticated evaluation metrics for assessing the musicality of generated sequences.
- Explore advanced LSTM architectures and hyperparameter tuning for improved music generation.
- Integrate with external libraries or APIs for additional features such as music playback and visualization.
