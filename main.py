def main():
    mode_handlers = {
        "simple": lambda: __import__("simple_mode").simple_mode(),
        "advanced": lambda: __import__("advanced_mode").advanced_mode(),
        "models": lambda: __import__("models").models(),
        "exit": lambda: print("Exited!")
    }
    
    mode = input("What mode do you want to use? (Simple/Advanced/Models/Exit): ").lower()
    
    handler = mode_handlers.get(mode)
    if handler:
        handler()
    else:
        raise ValueError("Invalid mode selected")

if __name__ == "__main__":
    main()
