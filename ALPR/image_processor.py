import cv2
import numpy as np


class ImageProcessor:

    def crop_plate(self, image: np.ndarray, bbox):
        """
        Cắt vùng biển số từ ảnh gốc.

        image: ảnh đầu vào dạng BGR
        bbox: (x1, y1, x2, y2)
        """
        x1, y1, x2, y2 = bbox

        plate = image[y1:y2, x1:x2]

        return plate

    def preprocess(self, plate: np.ndarray):
        """
        Tiền xử lý ảnh biển số trước khi đưa vào OCR.
        """

        # Chuyển ảnh màu sang ảnh xám
        gray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)

        # Phóng to ảnh để OCR dễ đọc hơn
        gray = cv2.resize(
            gray,
            None,
            fx=2,
            fy=2,
            interpolation=cv2.INTER_CUBIC
        )

        return gray