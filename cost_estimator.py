def generate_cost_estimate(client, idea):

    prompt = f"""
    Analyze this project idea:

    {idea}

    Estimate:

    ## Development Cost

    ## Hosting Cost

    ## Domain Cost

    ## Database Cost

    ## AI API Cost

    ## Total Monthly Cost

    ## Budget Version
    (Low-cost startup version)

    ## Professional Version
    (Production-ready version)

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