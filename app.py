from flask import Flask, render_template, request, jsonify
from ast_analyzer import analyze_code
from bkt_student_model import BayesianKnowledgeTracing
from pedagogical_engine import generate_feedback
import os

app = Flask(__name__)
bkt = BayesianKnowledgeTracing()
STUDENT_ID = "STU_WEB_001"

@app.route('/')
def index():
    mastery = bkt.get_student_mastery(STUDENT_ID)
    return render_template('index.html', mastery=mastery)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    code = data.get('code', '')
    
    # 1. Analyze AST
    analysis = analyze_code(code)
    
    # 2. Update Knowledge Tracing Model
    bkt.update_session(STUDENT_ID, analysis['concepts'], analysis['issues'])
    mastery = bkt.get_student_mastery(STUDENT_ID)
    
    # 3. Generate Feedback
    feedback = generate_feedback(analysis['issues'], mastery)
    
    return jsonify({
        'feedback': feedback,
        'mastery': mastery,
        'parsed_successfully': analysis['parsed_successfully']
    })

if __name__ == '__main__':
    # Use the port environment variable if available (for cloud deployment)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
