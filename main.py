import qrcode
import cv2


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



