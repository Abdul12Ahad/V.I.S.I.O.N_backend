from fastapi import APIRouter, UploadFile, File
from app.services.vision_service import analyze_uploaded_image
from app.models.analyze_response import AnalyzeResponse
from app.database import save_analysis

import os
import shutil
import uuid

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

ALLOWED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp"
}

@router.post(
    "/analyze",
    response_model=AnalyzeResponse
)
async def analyze_image(
    file: UploadFile = File(...)
):

    extension = os.path.splitext(
        file.filename
    )[1].lower()

    if extension not in ALLOWED_EXTENSIONS:

        return {
            "object": "Invalid File",
            "category": "Error",
            "width": 0,
            "height": 0,
            "size_kb": 0,
            "image_path": ""
        }

    unique_filename = (
        f"{uuid.uuid4().hex}_{file.filename}"
    )

    file_path = os.path.join(
        UPLOAD_DIR,
        unique_filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    result = analyze_uploaded_image(
        file_path
    )

    save_analysis(
        file.filename,
        result
    )

    return result