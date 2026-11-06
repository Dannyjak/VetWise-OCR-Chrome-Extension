# VetWise — Veterinary Record OCR and Autofill

VetWise is a Chrome extension and Flask service prototype designed to reduce repetitive transcription of veterinary patient records. It explores extracting text from uploaded forms and populating matching fields in a web-based patient record system.

## Why I built it
My experience in veterinary medicine exposed how much time staff spend reading handwritten notes and re-entering patient information. VetWise explores automating that first pass while leaving clinical review to the user.

## How it works
1. Select a PDF, PNG, or JPEG in the Chrome extension popup.
2. The popup uploads the file to a Flask processing service.
3. The service extracts embedded PDF text using PyMuPDF or image text using Google Cloud Vision document text detection.
4. The extension parses labeled output and attempts to autofill matching page elements (patient ID, species, breed, microchip, owner details, diagnosis, treatment, and more).

## Tech stack
- Chrome Manifest V3, JavaScript, HTML, Chrome scripting/tabs APIs
- Python, Flask, Flask-CORS
- PyMuPDF and Google Cloud Vision API
- Multipart file upload, JSON response, browser DOM manipulation

## Repository structure
All implementation files are under `VW Autofill Chrome Extension/`: `manifest.json`, `popup.html`, `popup.js`, `background.js`, `content.js`, and `server.py`.

## Local development
Install `flask`, `flask-cors`, `pymupdf`, and `google-cloud-vision`; configure Google application credentials for OCR; and start `server.py`. Load the `VW Autofill Chrome Extension` folder as an unpacked extension from `chrome://extensions` (Developer mode). Update the hard-coded popup API URL, Flask route, and extension host permissions to match your environment before testing with synthetic records.

## Current limitations
This is a proof of concept, not a production clinical system. The extension's request URL and route do not currently match the Flask `/run-script` route. The PDF path extracts embedded text rather than OCRing scanned PDFs. Autofill depends on exact element IDs and consistent text labels, so all output must be reviewed. Do not send real patient/client records to an unreviewed service. Time-saving claims in the previous README have not been independently verified from this repository.
