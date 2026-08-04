from paddleocr import PaddleOCR

ocr = PaddleOCR(lang="en")

result = ocr.ocr("app/uploads/HOszrFdWAAA9kUC.jpg")

print(result)