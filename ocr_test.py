import pytesseract
from PIL import Image
from PIL import ImageOps
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

image = Image.open("fPush test black text.jpg")

grayed = ImageOps.graysclae(image)

data = pytesseract.image_to_data(
    grayed,
    config="--psm 11",
    output_type=pytesseract.Output.DICT
)

for i, text in enumerate(data["text"]):
    confidence = int(data["conf"][i])

    if confidence > 50 and text.strip():
        print(text, confidence)