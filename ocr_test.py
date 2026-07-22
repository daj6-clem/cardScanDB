import pytesseract
from PIL import Image
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

image = Image.open("fPush test white text.jpg")

data = pytesseract.image_to_data(
    image,
    config="--psm 11",
    output_type=pytesseract.Output.DICT
)

for i, text in enumerate(data["text"]):
    confidence = int(data["conf"][i])

    if confidence > 10 and text.strip():
        print(text, confidence)