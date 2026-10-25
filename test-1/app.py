from flask import Flask, send_from_directory
import os

app = Flask(__name__)

DOWNLOAD_FOLDER = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "files"
)

@app.route("/")
def home():
    return """
    <h2>Python Project Downloads</h2>
    <a href="/download">Download Python Project ZIP</a>
    """

@app.route("/download")
def download():
    return send_from_directory(
        DOWNLOAD_FOLDER,
        "my-python-project.zip",
        as_attachment=True
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
