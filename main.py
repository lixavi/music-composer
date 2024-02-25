# main.py
from train import train_model
from generate import generate_music
from evaluation import evaluate_model

def main():
    # Train the model
    train_model()

    # Generate music
    generate_music()

    # Evaluate the model
    evaluate_model()

    # Interactive mode
    user_interaction()

def user_interaction():
    print("Welcome to the Music Composer!")
    while True:
        command = input("Enter 'generate' to generate new music, 'quit' to exit: ")
        if command == 'generate':
            generate_music()
        elif command == 'quit':
            print("Exiting...")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
