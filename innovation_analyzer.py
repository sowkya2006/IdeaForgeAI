def analyze_innovation(client, idea):

    prompt = f"""
    Analyze the following project idea:

    {idea}

    Return:

    ## Innovation Score
    Give a score out of 100.

    ## Reason
    Explain why.

    ## Unique Selling Proposition (USP)
    Suggest a unique feature that can make this project stand out.

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