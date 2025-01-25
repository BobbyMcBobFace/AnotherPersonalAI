import os

from groq import Groq

# Mode 
user_input = input("What mode do you want to use? (Simple/Advanced): ")
if user_input.lower() == "simple":

    # Api
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    # Input
    chat_content = input("Hi, I'm Groq. How may I help you today? ")
    print("Your input is:", chat_content)

    # Confirmation 
    user_input = input("Do you want to continue? (yes/no): ")
    if user_input.lower() == "yes":
        print("Continuing...")
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

    else:
        print("Exiting...")
        raise ValueError("Exited!")


    #Return Result
    print(chat_completion.choices[0].message.content)

    result = chat_completion.choices[0].message.content
    with open('result.md', 'w') as f:
        f.write(result)

    print("Result saved to result.md")

elif user_input.lower() == "advanced":
    print("Work in Progeress")
    raise ValueError("Work in Progress")

else:
    raise ValueError("No")