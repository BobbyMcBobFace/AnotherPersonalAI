from simple_mode import simple_mode
from advanced_mode import advanced_mode
from models import models

def main():

    # Mode
    mode = input("What mode do you want to use? (Simple/Advanced/Models/Exit): ").lower()
    if mode == "simple":
        simple_mode()

    elif mode == "advanced":
        advanced_mode()

    elif mode == "models":
        models()

    elif mode == "exit":
        raise ValueError("Exited!")

    else:
        raise ValueError("Invalid mode selected")

if __name__ == "__main__":
    main()
