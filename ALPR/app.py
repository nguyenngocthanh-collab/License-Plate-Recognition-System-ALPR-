import streamlit as st
import numpy as np
import cv2
from PIL import Image

from src.services.recognition_service import RecognitionService


st.set_page_config(
    page_title="Nhận diện biển số xe",
    page_icon="🚗",
    layout="centered"
)


@st.cache_resource
def load_service():
    return RecognitionService()


service = load_service()

st.title("🚗 HỆ THỐNG NHẬN DIỆN BIỂN SỐ XE")
st.write("Tải ảnh phương tiện lên để nhận diện biển số.")

st.divider()

uploaded_file = st.file_uploader(
    "Chọn ảnh phương tiện",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    image_rgb = np.array(image)
    image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

    st.subheader("Ảnh đầu vào")
    st.image(image, caption="Ảnh đã tải lên", use_container_width=True)

    st.divider()

    if st.button("🔍 Nhận diện biển số", use_container_width=True):
        with st.spinner("Đang xử lý ảnh..."):
            try:
                result = service.recognize(image_bgr)

                st.subheader("Kết quả nhận diện")

                if result:
                    st.success(f"Biển số xe: {result}")
                else:
                    st.warning("Không phát hiện hoặc không đọc được biển số.")

            except Exception as error:
                st.error(f"Đã xảy ra lỗi: {error}")

else:
    st.info("Vui lòng tải lên một ảnh để bắt đầu.")