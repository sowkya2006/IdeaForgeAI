from groq import Groq

def generate_revenue_model(client, idea):

    prompt = f"""
    Create a revenue model for this startup idea:

    {idea}

    Include:

    1. Revenue Streams
    2. Pricing Strategy
    3. Subscription Plans
    4. Expected Monthly Revenue
    5. Expected Yearly Revenue
    6. Monetization Opportunities
    7. Future Scaling Opportunities

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