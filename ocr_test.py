import pytesseract
from PIL import Image
from PIL import ImageOps
from PIL import ImageEnhance
from pytesseract import Output

#LATER ON WE WILL NEED TO CORRECT FOR PERPECTIVE ON CROOKED PHOTOS
#THIS IS WHERE OpenCV WILL BE USEFUL
#cv2.fastN1MeansDenoising() can be useful for reducing noise on mobile images


pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# THERE IS NO SINGULAR WAY TO MAKE A CARD INTO TEXT
# DIFFERENT COLORS WILL REQUIRE DIFFERENT METHODS
# SO WE NEED A FUNCTION THAT WILL TRY MULTIPLE TRIED AND TRUE METHODS, 
# AND THEN SELECT THE ONE WITH THE HIGHEST AVERAGE CONFIDENCE SCORE

def ocrTester(pic):
    print("searching for text...")
    width, height = pic.size
    title = pic.crop((0, 0, width, height/8))
    grayed = ImageOps.grayscale(title)

    for i in range(0,6):
        for j in range(0,6):
            for k in range(0,2):
                contrast = i/2
                sharpness = j/2
                contra = ImageEnhance.Contrast(grayed).enhance(contrast)
                sharp = ImageEnhance.Sharpness(contra).enhance(sharpness)
                if (k > 0):
                    binariated = sharp.point(lambda p: 255 if p > 180 else 0)
                else:
                    binariated = sharp    

                data = pytesseract.image_to_data(
                    binariated,
                    config="--psm 11",
                    output_type=pytesseract.Output.DICT
                )

                totalConf = 0
                textCount = 0
                for l, text in enumerate(data["text"]):
                    confidence = int(data["conf"][l])
                    if text.strip() and confidence >= 0:
                        totalConf += confidence
                        textCount += 1


                    #if confidence > 50 and text.strip():
                        #print(text, confidence)

                if textCount > 0:
                    avgConf = totalConf / textCount
                else:
                    avgConf = 0
                print(avgConf)

image = Image.open("fPush test black text.jpg")

ocrTester(image)

#grayed.show()
#image.show()
#bigger.show()
#grayed.show()
#contra.show()
#sharper.show()
#binary.show()