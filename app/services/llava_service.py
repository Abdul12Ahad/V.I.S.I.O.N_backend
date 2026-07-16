import ollama

import os

def analyze_with_llava(image_path: str, level: str,previous_learning):

    print(image_path)
    print(os.path.exists(image_path))

    history_text = ""

    if previous_learning:

        for item in previous_learning:
            history_text += f"""
    Description:
    {item['description']}

    Key Concepts:
    {", ".join(item['key_concepts'])}
    """

    else:

        history_text = "No previous learning history."

    prompt = f"""
    Analyze the image.

    The user has previously learned these concepts:

    {history_text}

    If the current image is related to anything above:

    - Mention the connection naturally.
    - Build upon previous knowledge.
    - Do NOT force connections if unrelated.

    The explanation level should be:
    {level}

    Rules:

    If level is Beginner:
    - Use simple words.
    - Explain like you are teaching a school student.
    - Avoid technical jargon.

    If level is Intermediate:
    - Use moderate technical terms.
    - Give balanced explanations.

    If level is Advanced:
    - Use proper technical terminology.
    - Give detailed explanations.
    - Assume the user already understands the basics.

    Return ONLY valid JSON.

    Follow this JSON schema EXACTLY.

    {{
        "description": "",
        "what_it_is": "",
        "how_it_works": "",
        "why_important": "",
        "fun_fact": "",
        "key_concepts": [],
        "related_topics": [
            {{
                "title": "",
                "points": []
            }}
        ],
        "learn_more": []
    }}

    IMPORTANT RULES:

    - description MUST be a string.
    - what_it_is MUST be a string.
    - how_it_works MUST be a string.
    - why_important MUST be a string.
    - fun_fact MUST be a string.
    - key_concepts MUST be an array of strings only.
    - related_topics MUST contain only title and points.
    - learn_more MUST be an array of strings only.
    - Do NOT return nested objects for any field except related_topics.
    - Do NOT include markdown.
    - Do NOT include ```json.
    - Do NOT include trailing commas.
    - Do NOT add extra fields.
    - Return ONLY the JSON object.
    """

    response = ollama.chat(
        model="llava:7b",
        messages=[
            {
                "role": "user",
                "content": prompt,
                "images": [image_path]
            }
        ]
    )

    return response["message"]["content"]

def answer_followup_question(
        context: str,
        question: str
    ):

    prompt = f"""
    You are an educational assistant.

    Context:

    {context}

    User Question:

    {question}

    Answer clearly and simply.
    """

    response = ollama.chat(
        model="llava:7b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]