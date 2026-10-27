from flask import Flask, render_template, send_from_directory, abort
from pathlib import Path

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
PROGRAMS_DIR = BASE_DIR / "programs"

PROGRAMS = [
    {"filename": "01_bfs_dfs.py", "title": "BFS and DFS in Python"},
    {"filename": "02_astar_maze.py", "title": "A* Search: Maze Navigation"},
    {"filename": "03_tic_tac_toe_minimax.py", "title": "Tic-Tac-Toe Game with AI (Minimax)"},
    {"filename": "04_peas_intelligent_agent.py", "title": "PEAS-Based Intelligent Agent"},
    {"filename": "05_sudoku_backtracking.py", "title": "Sudoku Solver Using Backtracking"},
    {"filename": "06_prolog_inference.py", "title": "Prolog-Style Inference Simulation"},
    {"filename": "07_forward_chaining.py", "title": "Rule-Based System Using Forward Chaining"},
    {"filename": "08_fuzzy_logic_controller.py", "title": "Fuzzy Logic Controller Using Scikit-Fuzzy"},
    {"filename": "09_bayesian_network.py", "title": "Bayesian Network Modeling Using pgmpy"},
    {"filename": "10_frame_and_script.py", "title": "Frame and Script Implementation"},
    {"filename": "11a_preprocessing_nltk.py", "title": "Preprocessing with NLTK"},
    {"filename": "11b_preprocessing_spacy.py", "title": "Preprocessing with spaCy"},
    {"filename": "11c_pos_tagging.py", "title": "POS Tagging"},
    {"filename": "11d_named_entity_recognition.py", "title": "Named Entity Recognition (NER)"},
    {"filename": "12a_information_extraction_regex.py", "title": "Information Extraction Using Regex"},
    {"filename": "12b_tfidf_analysis.py", "title": "TF-IDF Analysis Using Scikit-learn"},
    {"filename": "13_rule_based_chatbot.py", "title": "Rule-Based Chatbot with NLTK"},
    {"filename": "14a_gridworld_mdp.py", "title": "GridWorld MDP Simulation"},
    {"filename": "14b_multi_agent_simulation.py", "title": "Multi-Agent Simulation"},
    {"filename": "15a_boids_pygame.py", "title": "Swarm Behavior Using Boids Model"},
    {"filename": "15b_strips_planning.py", "title": "Planning with STRIPS-Style Simulation"},
    {"filename": "16_warehouse_coordination.py", "title": "Smart Traffic / Warehouse Coordination"},
    {"filename": "17_bias_detection_shap_lime.py", "title": "Bias Detection with SHAP/LIME"},
    {"filename": "18_ethics_case_study_chatbot.py", "title": "Ethics Case Study Chatbot"},
    {"filename": "19_ai_policy_roleplay.py", "title": "Roleplay-Based Simulation of AI Policy"},
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
