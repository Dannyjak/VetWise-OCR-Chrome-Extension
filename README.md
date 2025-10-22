VetWise is a Chrome Extension and Flask web app that automates the transcription of veterinary medical records using Google Cloud Vision OCR. Designed for clinics and animal shelters, VetWise simplifies the process of recording patient data, reducing manual entry time by up to 40%.

**Features**

OCR Automation: Extracts key patient and treatment data from scanned veterinary forms.

Web Dashboard: Displays parsed records for quick review, correction, and export.

Cloud Integration: Uses Google Cloud Vision API for high-accuracy text recognition.

Workflow Efficiency: Automatically formats and structures extracted data into record fields.

User Research Driven: Built with input from Michigan Humane’s Director of Veterinary Medicine to align with real clinical workflows.



**Tech Stack**

  Frontend: Chrome Extensions API, HTML, CSS, JavaScript
  Backend: Flask (Python), Google Cloud Vision API, RESTful API communication
  Data: JSON-based record transfer, local and cloud storage options



**Project Architecture**

		  vetwise/ 
		  │
		  ├── extension/
		  │ ├── popup.html
		  │ ├── popup.js
		  │ ├── manifest.json
		  │ └── styles.css
		  │
		  ├── server/
		  │ ├── app.py
		  │ ├── templates/
		  │ └── static/
		  │
		  ├── assets/
		  │ └── sample_records/
		  │
		  └── README.md



**Setup Instructions**

  Clone the repository
  git clone https://github.com/<your-username>/vetwise.git
  cd vetwise
  
  Set up the Flask server
  cd server
  pip install -r requirements.txt
  python app.py
  
  Add Google Cloud Vision credentials
  Create a Google Cloud Vision API key and store it in an .env file:
  GOOGLE_APPLICATION_CREDENTIALS=path/to/your-key.json
  
  Load the Chrome Extension
  
  Go to chrome://extensions
  
  Enable Developer Mode
  
  Click “Load Unpacked”
  
  Select the /extension directory



**Usage**

  Upload a scanned record or image through the Chrome Extension popup.
  
  VetWise automatically processes the document using OCR.
  
  The extracted data appears in the Flask web dashboard for review.
  
  Export or store the cleaned data in clinic systems.



**Impact**

  Reduced average record-entry time by 40% per case.
  
  Increased data accuracy and standardization.
  
  Empowered veterinary teams to focus on care instead of paperwork.



**Contributors**

Danny Jakubowski – Founder & Lead Developer
Special thanks to Michigan Humane for research collaboration and workflow testing.
