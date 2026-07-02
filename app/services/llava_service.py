import ollama


def analyze_with_llava(image_path: str, level: str):

    prompt = f"""
    Analyze the image.

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

    {{
        "description":"",
        "what_it_is":"",
        "how_it_works":"",
        "why_important":"",
        "fun_fact":"",
        "key_concepts":[],
        "related_topics":[],
        "learn_more":[]
    }}

    Do not return anything outside the JSON.
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