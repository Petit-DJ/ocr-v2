import os


os.environ["PADDLE_PDX_ENABLE_MKLDNN_BYDEFAULT"] = "0"
import numpy as np
from paddleocr import PaddleOCR
from PIL import Image

ocr_engine = PaddleOCR(
    lang="en",
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False,
)

# def run_ocr(images):
#     results = []


#     for image in images:
#         print(type(image))
#         image_np = np.array(image)
#         print(type(image_np))
#         result = list(ocr_engine.predict([image_np]))
#         results.append(result)
#     return results
def run_ocr(images: list[Image.Image]):
    results = []
    for image in images:
        image_np = np.asarray(image)
        page_result = ocr_engine.ocr(image_np)
        results.append(page_result)
        print(page_result)
    return results


def extract_text(ocr_results: list) -> str:
    lines = []

    for page in ocr_results:
        for line in page[0]:
            text = line[1][0]     
            lines.append(text)

    return "\n".join(lines)


def normalise_text(text: str) -> str:
    lines = []

    for line in text.splitlines():
        line = line.strip()
        if line:
            lines.append(line)

    return "\n".join(lines)

# if __name__ == "__main__":
#     from PIL import Image

#     img = Image.open("app/uploads/HOszrFdWAAA9kUC.jpg")

#     result = run_ocr([img])

#     print(result)