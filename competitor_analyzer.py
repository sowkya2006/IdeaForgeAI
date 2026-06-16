from groq import Groq

def analyze_competitors(client, idea):

    prompt = f"""
    Analyze competitors for this startup idea:

    {idea}

    Provide:

    1. Top 5 competitors
    2. What they do
    3. Their strengths
    4. Their weaknesses
    5. How this idea can differentiate itself

    Format nicely using headings and bullet points.
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