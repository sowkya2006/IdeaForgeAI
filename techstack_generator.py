def generate_techstack(client, idea):

    prompt = f"""
    Analyze this project idea:

    {idea}

    Suggest:

    ## Frontend

    ## Backend

    ## Database

    ## Authentication

    ## Hosting

    ## AI/ML Tools

    ## Why This Stack

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