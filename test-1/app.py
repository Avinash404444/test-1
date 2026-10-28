from flask import Flask, render_template, send_from_directory, abort
from pathlib import Path

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
PROGRAMS_DIR = BASE_DIR / "program"

PROGRAMS = [
    {"filename": "p1.py", "title": "EXPLORE VARIOUS COLOR PALETTES IN SEABORN"},
    {"filename": "p2.py", "title": "CREATING DIFFERENT TYPES OF PLOTS USING MATPLOTLIB"},
    {"filename": "p3.py", "title": "ASSESS STUDENT PERFORMANCE IN THE ANNUAL EXAMINATION USING BOXPLOT"},
]

@app.route("/")
def home():
    available = [p for p in PROGRAMS if (PROGRAMS_DIR / p["filename"]).is_file()]
    return render_template("index.html", programs=available)

@app.route("/copy/<path:filename>")
def copy_code(filename):
    allowed = {p["filename"] for p in PROGRAMS}
    if filename not in allowed or not (PROGRAMS_DIR / filename).is_file():
        abort(404)
    return send_from_directory(PROGRAMS_DIR, filename, mimetype="text/plain")

@app.route("/download/<path:filename>")
def download(filename):
    allowed = {p["filename"] for p in PROGRAMS}
    if filename not in allowed or not (PROGRAMS_DIR / filename).is_file():
        abort(404)
    return send_from_directory(PROGRAMS_DIR, filename, as_attachment=True)

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
