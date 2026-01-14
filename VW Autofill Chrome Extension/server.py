# import logging
# from flask import Flask, request, jsonify
# import fitz  # PyMuPDF
# import io
# from google.cloud import vision_v1p3beta1 as vision
# import os
# from flask_cors import CORS

# app = Flask(__name__)
# # CORS(app, resources={r"/run-script": {"origins": ["chrome-extension://", "http://localhost:5001"]}})

# CORS(app, resources={r"/run-script": {"origins": [
#     "chrome-extension://opablligfegdnikmmkegkdfllcejkaif", 
#     "chrome-extension://jkjnkbbkponocmpjpoddeojehmhjhgcc", 
#     "hhttp://localhost:8001"
# ]}})

# # Configure logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# @app.route('/')
# def home():
#     logging.info('Home route accessed')
#     return "Server is running!"

# @app.route('/run-script', methods=['POST'])
# def run_script():
#     logging.info('Received a request to /run-script')
#     if 'file' not in request.files:
#         logging.error('No file part in the request')
#         return jsonify({'error': 'No file part in the request'}), 400

#     file = request.files['file']
#     if file.filename == '':
#         logging.error('No selected file')
#         return jsonify({'error': 'No selected file'}), 400

#     # Check if the file is a supported type (PDF, JPEG, PNG)
#     if file and (file.content_type == 'application/pdf' or file.content_type == 'image/jpeg' or file.content_type == 'image/png'):
#         try:
#             if file.content_type == 'application/pdf':
#                 logging.info('Processing PDF file')
#                 content = file.read()
#                 document = fitz.open(stream=content, filetype="pdf")
#                 text = ""
#                 for page_num in range(document.page_count):
#                     page = document.load_page(page_num)
#                     text += page.get_text()
#                 logging.info('PDF processed successfully')
#                 return jsonify({'output': text})
#             else:
#                 logging.info('Processing image file')
#                 client = vision.ImageAnnotatorClient()
#                 content = file.read()
#                 image = vision.Image(content=content)

#                 image_context = vision.ImageContext(language_hints=["en-t-i0-handwrit"])
#                 response = client.document_text_detection(image=image, image_context=image_context)

#                 if response.error.message:
#                     error_message = (
#                         "{}\nFor more info on error messages, check: "
#                         "https://cloud.google.com/apis/design/errors".format(response.error.message)
#                     )
#                     logging.error(error_message)
#                     raise Exception(error_message)

#                 result_text = f"Full Text: {response.full_text_annotation.text}\n"
#                 for page in response.full_text_annotation.pages:
#                     for block in page.blocks:
#                         result_text += f"\nBlock confidence: {block.confidence}\n"

#                         for paragraph in block.paragraphs:
#                             result_text += "Paragraph confidence: {}\n".format(paragraph.confidence)

#                             for word in paragraph.words:
#                                 word_text = "".join([symbol.text for symbol in word.symbols])
#                                 result_text += "Word text: {} (confidence: {})\n".format(word_text, word.confidence)

#                                 for symbol in word.symbols:
#                                     result_text += "\tSymbol: {} (confidence: {})\n".format(symbol.text, symbol.confidence)

#                 logging.info('Image processed successfully')
#                 return jsonify({'output': result_text})
#         except Exception as e:
#             logging.exception('An error occurred during file processing')
#             return jsonify({'error': str(e)}), 500
#     else:
#         logging.error('Unsupported file type')
#         return jsonify({"error": "Unsupported file type"}), 400

# if __name__ == '__main__':
#     os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/Deeje/Downloads/tester-420821-40f256da5cc7.json'
#     app.run(port=8001, debug=True)

#########################

# import logging
# from flask import Flask, request, jsonify
# import fitz  # PyMuPDF
# import io
# from google.cloud import vision_v1p3beta1 as vision
# import os
# from flask_cors import CORS
# import requests

# app = Flask(__name__)
# # CORS(app, resources={r"/run-script": {"origins": ["chrome-extension://", "http://localhost:5001"]}})

# CORS(app, resources={r"/run-script": {"origins": [
#     "chrome-extension://opablligfegdnikmmkegkdfllcejkaif", 
#     "chrome-extension://jkjnkbbkponocmpjpoddeojehmhjhgcc", 
#     "hhttp://localhost:8001"
# ]}})

# # Configure logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# @app.route('/')
# def home():
#     logging.info('Home route accessed')
#     return "Server is running!"

# @app.route('/run-script', methods=['POST'])
# def run_script():
#     logging.info('Received a request to /run-script')
#     if 'file' not in request.files:
#         logging.error('No file part in the request')
#         return jsonify({'error': 'No file part in the request'}), 400

#     file = request.files['file']
#     if file.filename == '':
#         logging.error('No selected file')
#         return jsonify({'error': 'No selected file'}), 400

#     # Check if the file is a supported type (PDF, JPEG, PNG)
#     if file and (file.content_type == 'application/pdf' or file.content_type == 'image/jpeg' or file.content_type == 'image/png'):
#         try:
#             if file.content_type == 'application/pdf':
#                 logging.info('Processing PDF file')
#                 content = file.read()
#                 document = fitz.open(stream=content, filetype="pdf")
#                 text = ""
#                 for page_num in range(document.page_count):
#                     page = document.load_page(page_num)
#                     text += page.get_text()
#                 logging.info('PDF processed successfully')
#                 return jsonify({'output': text})
#             else:
#                 logging.info('Processing image file')
#                 client = vision.ImageAnnotatorClient()

#                 if file.startswith('http'):
#                     # If the input is a URL, download the image from the URL
#                     image_data = requests.get(file).content
#                     image = vision.Image(content=image_data)
#                 else:
#                     # If the input is a local file path, load the image from the file
#                     with io.open(file, 'rb') as image_file:
#                         content = image_file.read()
#                     image = vision.Image(content=content)

#                 # Language hint codes for handwritten OCR:
#                 # en-t-i0-handwrit, mul-Latn-t-i0-handwrit
#                 # Note: Use only one language hint code per request for handwritten OCR.
#                 image_context = vision.ImageContext(language_hints=["en-t-i0-handwrit"])

#                 response = client.document_text_detection(image=image, image_context=image_context)

#                 if response.error.message:
#                     raise Exception(
#                         "{}\nFor more info on error messages, check: "
#                         "https://cloud.google.com/apis/design/errors".format(response.error.message)
#                     )
                
#                 result_text = f"Full Text: {response.full_text_annotation.text}\n"
#                 logging.info('Image processed successfully')
#                 return jsonify({'output': result_text})
#         except Exception as e:
#             logging.exception('An error occurred during file processing')
#             return jsonify({'error': str(e)}), 500
#     else:
#         logging.error('Unsupported file type')
#         return jsonify({"error": "Unsupported file type"}), 400

# if __name__ == '__main__':
#     os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/Deeje/Downloads/tester-420821-40f256da5cc7.json'
#     app.run(port=8001, debug=True)


#########################


import logging
import os
import time

from flask import Flask, request, jsonify
from flask_cors import CORS
import fitz  # PyMuPDF
from google.cloud import vision_v1p3beta1 as vision

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.INFO)

MAX_PDF_PAGES = 5        # hard cap
MAX_PROCESS_SECONDS = 10  # hard timeout


@app.route("/run-script", methods=["POST"])
def run_script():
    start_time = time.time()

    if "file" not in request.files:
        return jsonify(error="No file uploaded"), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify(error="Empty filename"), 400

    extracted_text = ""

    try:
        # ---------------- PDF ----------------
        if file.content_type == "application/pdf":
            pdf_bytes = file.read()
            document = fitz.open(stream=pdf_bytes, filetype="pdf")

            for i, page in enumerate(document):
                if i >= MAX_PDF_PAGES:
                    break
                if time.time() - start_time > MAX_PROCESS_SECONDS:
                    break

                extracted_text += page.get_text()

            if not extracted_text.strip():
                extracted_text = "[No extractable text — scanned PDF]"

        # ---------------- IMAGE OCR ----------------
        elif file.content_type in ("image/png", "image/jpeg"):
            client = vision.ImageAnnotatorClient()
            image = vision.Image(content=file.read())

            response = client.document_text_detection(image=image)

            if response.error.message:
                raise RuntimeError(response.error.message)

            extracted_text = response.full_text_annotation.text

        else:
            return jsonify(error="Unsupported file type"), 400

        # ---------------- STRUCTURED OUTPUT ----------------
        output = (
            "Patient ID:\n"
            "Name:\n"
            "Species:\n"
            "Breed:\n"
            "Age/DOB Years:\n"
            "Age/DOB Months:\n"
            "Gender:\n"
            "Color/Markings:\n"
            "Microchip ID:\n"
            "Owner Name:\n"
            "Contact Number:\n"
            "Address:\n"
            "Email:\n"
            "Condition:\n"
            "Date Diagnosed:\n"
            "Treatment Provided:\n"
            "Outcome/Current Status:\n\n"
            "--- RAW OCR TEXT ---\n"
            f"{extracted_text}"
        )

        return jsonify(output=output), 200

    except Exception as e:
        logging.exception("Processing failed")
        return jsonify(error=str(e)), 500


if __name__ == "__main__":
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = (
        "/Users/Deeje/Downloads/tester-420821-40f256da5cc7.json"
    )

    app.run(host="0.0.0.0", port=8082, debug=True)
