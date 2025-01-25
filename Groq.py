import os

from groq import Groq

def simple_mode():
    
    # Api
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    # Input
    chat_content = input("Hi, I'm Groq. How may I help you today? ")
    print("Your input is:", chat_content)

    # Confirmation    
    if input("Do you want to continue? (yes/no): ").lower() != "yes":
        print("Exiting...")
        return

    # Query the LLM 
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": chat_content,
        }
    ],
    # Specify
    model="llama-3.3-70b-versatile",
    )

    result = chat_completion.choices[0].message.content
    print(result)

    with open('result.md', 'w') as f:
        f.write(result)
    print("Result saved to result.md")

def main():

    # Mode
    mode = input("What mode do you want to use? (Simple/Advanced): ").lower()
    if mode == "simple":
        simple_mode()

    elif mode == "advanced":
        print("Work in Progress")
        raise NotImplementedError("Advanced mode is not yet implemented")

    else:
        raise ValueError("Invalid mode selected")


if __name__ == "__main__":
    main()
