from PIL import Image
import os

from app.services.llava_service import (
    analyze_with_llava
)


def analyze_uploaded_image(
    image_path: str
):

    image = Image.open(
        image_path
    )

    width, height = image.size

    size_kb = round(
        os.path.getsize(image_path) / 1024,
        2
    )

    try:

        analysis = analyze_with_llava(
            image_path
        )

    except Exception as e:

        analysis = (
            f"Vision Model Error: {str(e)}"
        )

    return {

        "analysis": analysis,

        "category": "Vision Analysis",

        "width": width,
        "height": height,

        "size_kb": size_kb,

        "image_path": image_path
    }