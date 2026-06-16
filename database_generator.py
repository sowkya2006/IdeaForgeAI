def generate_database(client, idea):

    prompt = f"""
    Analyze this project idea:

    {idea}

    Generate:

    ## Database Tables

    Mention important tables.

    For each table:
    - Table Name
    - Columns

    ## Relationships

    Explain table relationships.

    ## Recommended Database

    Suggest database and explain why.

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