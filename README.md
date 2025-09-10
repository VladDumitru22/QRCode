# QRCode

A lightweight and user-friendly application for generating and scanning QR codes. This repository provides all the tools and features needed to create custom QR codes and decode them from images.

---

## Features

- **Generate QR Codes**: Input any text or URL to generate a QR code and download it as a PNG file.  
- **Decode QR Codes**: Upload an image containing a QR code to extract its encoded information.  
- **Scan QR Codes with Webcam**: Use your computer's webcam to scan QR codes in real time.  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/QRCode.git
cd QRCode
```
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```
3. Run the Streamlit application:

```bash
streamlit run main.py
```

4. Open your browser to:
```bash
http://localhost:8501
```

## Installation with Docker

1. Clone the repository:

```bash
git clone https://github.com/your-username/QRCode.git
cd QRCode
```
2. Build the Docker image:

```bash
docker build -t qr-app .
```
3. Run the container:
```bash
  docker run -p 8501:8501 qr-app
```
4. Open your browser to:
```bash
http://localhost:8501
```

## How it works

### QR Code Generation
- Input text or a URL.  
- The app generates a QR code and displays it.  
- Option to download the QR code as a PNG file.  

### QR Code Decoding
- Upload an image containing a QR code.  
- The app decodes the image and extracts the encoded information.  

### QR Code Scanning
- Activate your webcam.  
- The app displays a live feed and detects QR codes in real time.  
