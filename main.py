def main():
    # Mode
    mode = input("What mode do you want to use? (Simple/Advanced/Models/Exit): ").lower()
    if mode == "simple":
        from simple_mode import simple_mode
        simple_mode()
    elif mode == "advanced":
        from advanced_mode import advanced_mode
        advanced_mode()
    elif mode == "models":
        from models import models
        models()
    elif mode == "exit":
        raise ValueError("Exited!")
    else:
        raise ValueError("Invalid mode selected")

if __name__ == "__main__":
    main()
