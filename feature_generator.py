def generate_features(client, idea):

    prompt = f"""
    Analyze this project idea:

    {idea}

    Generate:

    ## Must Have Features
    List 5-8 features

    ## Nice To Have Features
    List 5 features

    ## Future Features
    List 5 advanced features

    Format using markdown.
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