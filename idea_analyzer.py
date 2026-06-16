from groq import Groq

def analyze_idea(client, idea):

    prompt = f"""
    Analyze the following project idea:

    {idea}

    Return in this format:

    ## Project Summary

    ## Category

    ## Target Audience

    ## Problem Statement

    ## Proposed Solution
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content