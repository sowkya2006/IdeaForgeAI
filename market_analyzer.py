def analyze_market(client, idea):

    prompt = f"""
    Analyze the market potential for:

    {idea}

    Return:

    1. Market Overview
    2. Target Customers
    3. Competitor Analysis
    4. Industry Trends
    5. Revenue Opportunities
    6. SWOT Analysis

    Use clear headings.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content