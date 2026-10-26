from flask import Flask, render_template, send_from_directory, abort
from pathlib import Path

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
PROGRAMS_DIR = BASE_DIR / "programs"

PROGRAMS = [
    {"filename": "01_array_operations.py", "title": "Array Operations Using Python"},
    {"filename": "02_linked_list_operations.py", "title": "Linked List Operations Using Python"},
    {"filename": "03_stack_adt.py", "title": "Implementation of Stack Using Abstract Data Type in Python"},
    {"filename": "04_queue_adt.py", "title": "Implementation of ADT Queue Using Python"},
    {"filename": "05_binary_tree_traversals.py", "title": "Implementation of Binary Tree ADT and Tree Traversal Operations Using Python"},
    {"filename": "06_binary_search_adt.py", "title": "Implementation of Binary Search ADT"},
    {"filename": "07_avl_tree_and_heap_adt.py", "title": "Implementation of AVL Tree and Heap ADT Using Python"},
    {"filename": "08_heap_tree_adt.py", "title": "Implementation of Heap Tree ADT Using Python"},
    {"filename": "09_graph_adt.py", "title": "Implementation of Graph ADT Using Python"},
    {"filename": "10_dijkstra_shortest_path.py", "title": "Implementation of Shortest Path Algorithm Using Dijkstra's Algorithm"},
    {"filename": "11_sorting_adt.py", "title": "Implementation of Sorting ADT Using Python"},
    {"filename": "12_searching_adt.py", "title": "Implementation of Searching ADT Using Python"},
    {"filename": "13_hashing_adt.py", "title": "Implementation of Hashing ADT Using Python"},
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
