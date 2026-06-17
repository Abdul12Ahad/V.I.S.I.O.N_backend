import ollama


def analyze_with_llava(image_path: str):

    prompt = """
You are an educational AI assistant.

Analyze the uploaded image and provide:

1. Description
2. What the object is
3. How it works
4. Why it is important
5. One fun fact

Keep the explanation beginner-friendly.
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