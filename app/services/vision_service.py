from PIL import Image
import os
import json

from app.services.llava_service import (
    analyze_with_llava
)


def analyze_uploaded_image(image_path: str, level: str):

    image = Image.open(image_path)

    width, height = image.size

    size_kb = round(
        os.path.getsize(image_path) / 1024,
        2
    )

    try:

        raw_response = analyze_with_llava(
            image_path,
            level
        )

        print("\n" + "=" * 50)
        print("RAW RESPONSE FROM LLAVA:")
        print(raw_response)
        print("=" * 50 + "\n")

        start = raw_response.find("{")
        end = raw_response.rfind("}") + 1

        json_text = raw_response[start:end]

        analysis = json.loads(
            json_text
        )

    except Exception as e:

        analysis = {

            "description":
                raw_response,

            "what_it_is": "",

            "how_it_works": "",

            "why_important": "",

            "fun_fact": ""
        }

    return {

        "description":
            analysis.get(
                "description",
                ""
            ),

        "what_it_is":
            analysis.get(
                "what_it_is",
                ""
            ),

        "how_it_works":
            analysis.get(
                "how_it_works",
                ""
            ),

        "why_important":
            analysis.get(
                "why_important",
                ""
            ),

        "fun_fact":
            analysis.get(
                "fun_fact",
                ""
            ),

        "key_concepts":
        analysis.get(
            "key_concepts",
            []
        ),

        "related_topics":
            analysis.get(
                "related_topics",
                []
            ),

        "learn_more":
            analysis.get(
                "learn_more",
                []
            ),

        "category":
            "Vision Analysis",

        "width":
            width,

        "height":
            height,

        "size_kb":
            size_kb,

        "image_path":
            image_path,

    }