
from flask import Flask, send_from_directory
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_FOLDER = os.path.join(BASE_DIR, "files")
ZIP_FILE = "programs.zip"

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Python Programs Download</title>
    </head>
    <body>
        <a href="/download">Download</a>
    </body>
    </html>
    """

@app.route("/download")
def download():
    if not os.path.isfile(os.path.join(DOWNLOAD_FOLDER, ZIP_FILE)):
        return "ZIP file not found. Check the files folder and filename.", 404

    return send_from_directory(
        DOWNLOAD_FOLDER,
        ZIP_FILE,
        as_attachment=True
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
