from flask import Flask, render_template, request, jsonify, send_from_directory, session
import os
import fitz  # PyMuPDF
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
from college_data import DTE_CODE_TO_COLLEGE  # Importing the dictionary

app = Flask(__name__)
app.secret_key = 'super-secret-key'  # Set a secret key for sessions

# Constants for folder paths
FOLDER_PATH = "clg"
FOLDER_PATH_2 = "clg2"  # Additional folder for "all_maharashtra"
FOLDER_PATH_MUMBAI = "clgmum"

def log_search(query, results, region):
    """Logs the search query, results, and timestamp to the console (captured by Heroku logs)."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"Timestamp: {timestamp}")
    print(f"Search Query: {query} | Region: {region}")
    if results:
        print("Results:")
        for result in results:
            print(f" - {result}")
    else:
        print("Results: No matches found.")
    print("\n")

def search_pdf_for_string(pdf_path, search_string):
    """Searches for a string in a PDF file."""
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        if search_string.upper() in text.upper():
            return os.path.basename(pdf_path)
    return None

def search_pdfs_in_multiple_folders(search_string, folder_paths, max_workers=8):
    """Searches for a string in all PDF files within the specified folders using multiprocessing."""
    found_pdfs = []

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for folder_path in folder_paths:
            for filename in os.listdir(folder_path):
                if filename.endswith('.pdf'):
                    file_path = os.path.join(folder_path, filename)
                    futures.append(executor.submit(search_pdf_for_string, file_path, search_string))
        for future in futures:
            result = future.result()
            if result:
                found_pdfs.append(result)

    return found_pdfs

def get_college_name_from_filename(filename):
    """Extracts the DTE code from the filename and returns the corresponding college name."""
    dte_code = filename.split('_')[-1].replace('.pdf', '')
    return DTE_CODE_TO_COLLEGE.get(dte_code, "Unknown College")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_pdfs', methods=['POST'])
def search_pdfs():
    data = request.json
    search_string = data.get('search_string')
    region = data.get('region')

    if not search_string:
        return jsonify({"error": "search_string is required"}), 400

    # Determine which folders to search based on the selected region
    if region == "all_maharashtra":
        folder_paths = [FOLDER_PATH, FOLDER_PATH_2]  # Search both clg and clg2 folders
    else:
        folder_paths = [FOLDER_PATH_MUMBAI]  # Search only in clgmum for Mumbai region

    found_pdfs = search_pdfs_in_multiple_folders(search_string, folder_paths)

    # Log the search query and results
    log_search(search_string, found_pdfs, region)

    if found_pdfs:
        results = [{"filename": pdf, "college_name": get_college_name_from_filename(pdf)} for pdf in found_pdfs]
        return jsonify({"found_pdfs": results})
    else:
        return jsonify({"message": "Use the following format, (Lastname Firstname Midname) OR No allotments until CAPR-II"})

@app.route('/pdfs/<filename>')
def serve_pdf(filename):
    """Serve a specific PDF file."""
    folder_path = FOLDER_PATH if filename.startswith("CAPR-I") else FOLDER_PATH_MUMBAI
    return send_from_directory(folder_path, filename)

if __name__ == '__main__':
    app.run(debug=False)
