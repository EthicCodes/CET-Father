from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import fitz  # PyMuPDF
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
from college_data import DTE_CODE_TO_COLLEGE  # Importing the dictionary
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Constants for folder paths
FOLDER_PATH = "clg"
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
    print("\n")  # Add an empty line for readability
def search_pdf_for_string(pdf_path, search_string):
    """Searches for a string in a PDF file."""
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        if search_string.upper() in text.upper():
            return os.path.basename(pdf_path)
    return None
def search_pdfs_in_folder(search_string, folder_path, max_workers=8):
    """Searches for a string in all PDF files within a specified folder using multiprocessing."""
    found_pdfs = []
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = []
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
    # Determine which folder to search based on the selected region
    folder_path = FOLDER_PATH if region == "all_maharashtra" else FOLDER_PATH_MUMBAI
    found_pdfs = search_pdfs_in_folder(search_string, folder_path)
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
    # Determine the correct folder based on the file name
    folder_path = FOLDER_PATH if filename.startswith("CAPR-I") else FOLDER_PATH_MUMBAI
    return send_from_directory(folder_path, filename)

# New API endpoints
# New API endpoint to search for AppxID in PDFs

@app.route('/api/fetch_data', methods=['POST'])
def fetch_data():
@app.route('/api/search_pdf', methods=['POST'])
def search_pdf():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No title found"

        return jsonify({"title": title, "status": "success"}), 200

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/get_college_info', methods=['GET'])
def get_college_info():
    college_code = request.args.get('college_code')
    if not college_code:
        return jsonify({"error": "College code is required"}), 400

    college_info = DTE_CODE_TO_COLLEGE.get(college_code.upper())

    if college_info:
        return jsonify({"college_name": college_info, "status": "success"}), 200
    appx_id = data.get('appx_id')
    region = data.get('region', 'all_maharashtra')

    if not appx_id:
        return jsonify({"error": "AppxID is required"}), 400

    # Determine which folder to search based on the selected region
    folder_path = FOLDER_PATH if region == "all_maharashtra" else FOLDER_PATH_MUMBAI
    found_pdfs = search_pdfs_in_folder(appx_id, folder_path)

    if found_pdfs:
        results = [{"filename": pdf, "college_name": get_college_name_from_filename(pdf)} for pdf in found_pdfs]
        return jsonify({"found_pdfs": results})
    else:
        return jsonify({"error": "College not found"}), 404
        return jsonify({"message": "No matches found for the provided AppxID."})

if __name__ == '__main__':
    app.run(debug=True)
