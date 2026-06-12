import easyocr


class OCRReader:

    def __init__(self):

        self.reader = easyocr.Reader(
            ['en']
        )

    def read_text(
        self,
        image_path
    ):

        result = self.reader.readtext(
            image_path,
            detail=0
        )

        return " ".join(result)