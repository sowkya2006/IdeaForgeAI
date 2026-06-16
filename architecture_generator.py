def generate_architecture(client, idea):

    prompt = f"""
    Analyze this project idea:

    {idea}

    Generate:

    ## System Architecture

    Explain the complete architecture flow:

    Frontend
    ↓
    Backend
    ↓
    Database
    ↓
    AI Services

    ## API Flow

    ## Deployment Architecture

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