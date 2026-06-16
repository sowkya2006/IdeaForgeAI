def analyze_benefits(client, idea):

    prompt = f"""
    Analyze this project idea:

    {idea}

    Return:

    ## Benefits
    - List 5 benefits

    ## Challenges
    - List 5 challenges

    ## Difficulty Level
    - Easy / Medium / Hard

    Format the response nicely using markdown.
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