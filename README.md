# Groq API Interaction Tool

This Python script provides an interface to interact with the Groq API, allowing users to generate text using various AI models.
This is not complete and is only a small part of a much larger project

## Features

- Simple mode: Quick interaction with a default AI model: llama-3.3-70b-versatile
- Advanced mode: Choose a specific AI model for text generation
- Model listing: View available AI models

## Prerequisites

- Python 3.6+
- Groq API key

## Installation

1. Clone this repository via <https://github.com/BobbyMcBobFace/AnotherPersonalAI.git>
2. Install required packages: pip install groq requests python-dotenv httpx
3. Head to <https://console.groq.com/keys> and generate an API Key
4. Create a `.env` file in the project root and add your Groq API key:

## Functions

- `simple_mode()`: Interact with the default AI model
- `advanced_mode()`: Choose a specific AI model for text generation
- `models()`: Display available AI models
- `main()`: Main program loop and mode selection

## API Reference

This tool uses the Groq API. For more information, visit [Groq API Documentation](https://console.groq.com/docs/overview).

## License

[MIT License](LICENSE.txt)

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/groq-api-tool/issues) if you want to contribute.

## Author

[@BobbyMcBobFace](https://github.com/BobbyMcBobFace)
