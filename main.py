import qrcode
import cv2

import streamlit as st

def generate_qr(text):
    """Generează un cod QR pe baza textului/URL-ului."""
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    return img

def decode_qr(image):
    """Decodare QR code dintr-o imagine."""
    detector = cv2.QRCodeDetector()
    value, _, _ = detector.detectAndDecode(image)
    return value

def scan_qr_from_camera():
    """Scanează un cod QR folosind camera web."""
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()

    stop_button = st.button("Stop Camera")

    stframe = st.empty()
    decoded_value = None

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Nu se poate accesa camera.")
            break


        value, _, _ = detector.detectAndDecode(frame)


        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stframe.image(frame_rgb, channels="RGB", use_container_width=True)


        if value:
            decoded_value = value
            break


        if stop_button:
            break

    cap.release()
    return decoded_value

