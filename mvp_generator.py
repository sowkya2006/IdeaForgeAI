def generate_mvp(client, idea):

    prompt = f"""
    Analyze this project idea:

    {idea}

    Create:

    ## MVP Version

    Mention only the minimum features
    required to launch Version 1.

    Also explain:

    Why these features are enough.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content