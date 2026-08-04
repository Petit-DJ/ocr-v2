#app/processing/pipeline.py

from pathlib import Path

# from app.processing.stages.address import extract_address
from app.processing.stages.ocr import extract_text, run_ocr, normalise_text
from app.processing.stages.pdf import pdf_to_images



def process_document(pdf_path: str) -> str:
    
    images = pdf_to_images(pdf_path)
    ocr_result = run_ocr(images)
    text = extract_text(ocr_result)
    text = normalise_text(text)
    # address = extract_address(text)
    return text




# if __name__ == "__main__":
#     address = process_document("C:/Users/DJSuryansh-BroadwayI/AI_Team/Invoice-Processing-Pipeline/app/uploads/Invoice206027.pdf")
#     print(address)