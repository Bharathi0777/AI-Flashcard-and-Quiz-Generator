from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def generate_flashcards(topic):
    return [
        {"question": f"What is {topic}?", "answer": f"{topic} is a key concept to learn."},
        {"question": f"Why is {topic} important?", "answer": f"{topic} helps in understanding basics."},
        {"question": f"Give an example of {topic}?", "answer": f"Example of {topic} is in daily life."},
    ]

def generate_quiz(topic):
    return [
        {"question": f"Which is TRUE about {topic}?", "options": [f"{topic} is useful", f"{topic} is useless", "Both wrong", "None"], "answer": f"{topic} is useful"},
        {"question": f"What is {topic} mainly used for?", "options": ["Learning", "Gaming", "Sleeping", "None"], "answer": "Learning"},
    ]

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json(force=True, silent=True) or {}
    topic = data.get('topic', 'General')
    if not topic:
        topic = 'General'
    return jsonify({
        "flashcards": generate_flashcards(topic),
        "quiz": generate_quiz(topic)
    })

@app.route('/')
def home():
    return "Backend Running"

if __name__ == '__main__':
    app.run(port=5000, debug=True)