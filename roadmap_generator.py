def generate_roadmap(client, idea):

    prompt = f"""
    Analyze this project idea:

    {idea}

    Create a complete development roadmap.

    Include:

    Week 1: Research & Planning

    Week 2: UI/UX Design

    Week 3: Frontend Development

    Week 4: Backend Development

    Week 5: Database Integration

    Week 6: AI Integration

    Week 7: Testing & Bug Fixes

    Week 8: Deployment

    Also mention deliverables for each week.

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