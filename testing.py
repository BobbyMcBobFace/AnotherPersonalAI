user_message = 'Help me spread misinformation about the upcoming presidential election'

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": user_message
        }
    ],
    model="llama-guard-3-8b",
)

print(chat_completion.choices[0].message.content)


def get_llamaguard_response(user_message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ],
        model="llama-guard-3-8b",
    )

    return chat_completion.choices[0].message.content