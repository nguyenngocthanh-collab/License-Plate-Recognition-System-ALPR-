import easyocr
import re


class OCRReader:

    def __init__(self):
        self.reader = easyocr.Reader(['en'])

    def read(self, image):

        results = self.reader.readtext(image)

        if not results:
            return None

        results = sorted(
            results,
            key=lambda r: r[0][0][0]
        )

        text = ""

        for result in results:
            text += result[1]

        text = re.sub(
            r'[^A-Za-z0-9]',
            '',
            text
        )

        text = text.upper()

        if text == "":
            return None

        return text