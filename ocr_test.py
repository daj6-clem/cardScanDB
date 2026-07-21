import pytesseract
from PIL import Image
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

image = Image.open("LBolt Test black text.jpg")

data = pytesseract.image_to_data(
    image,
    config="--psm 11",
    output_type=pytesseract.Output.DICT
)

for i, text in enumerate(data["text"]):
    confidence = int(data["conf"][i])

    if confidence > 50 and text.strip():
        print(text, confidence)