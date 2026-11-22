class RecognitionService:
    """
    Điều phối các bước nhận diện biển số xe.
    Hiện tại dùng dữ liệu giả để kiểm tra giao diện.
    """

    def recognize(self, image):
        if image is None:
            return None

        # TODO: Tích hợp YOLO, xử lý ảnh và OCR sau
        return "29A12345"