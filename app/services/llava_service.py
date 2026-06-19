import ollama


def analyze_with_llava(image_path: str):

    prompt = """
    Analyze the image.

    Return ONLY valid JSON.

    {
        "description":"",
        "what_it_is":"",
        "how_it_works":"",
        "why_important":"",
        "fun_fact":"",
        "key_concepts":[],
        "related_topics":[],
        "learn_more":[]
    }

    Keep explanations beginner friendly.
    Do not return any text outside JSON.
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