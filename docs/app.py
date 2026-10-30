from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os, json
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)

api_key = os.getenv("GEMINI_API_KEY")
print("API KEY:", "FOUND ✅" if api_key else "NOT FOUND ❌")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route('/generate', methods=['POST'])
def generate():
    topic = request.get_json().get('topic','html')
    prompt = f"For topic '{topic}', generate EXACTLY 10 flashcards with detailed 3-4 line answers with examples, and EXACTLY 10 MCQ quiz with 4 options each. Return ONLY JSON: {{\"flashcards\": [{{\"question\":\"\",\"answer\":\"\"}}], \"quiz\": [{{\"question\":\"\",\"options\":[], \"answer\":\"\"}}]}}"
    try:
        res = model.generate_content(prompt)
        text = res.text.replace("```json","").replace("```","").strip()
        data = json.loads(text)
        print(f"SUCCESS: Flashcards {len(data['flashcards'])} Quiz {len(data['quiz'])}")
        return jsonify(data)
    except Exception as e:
        print("GEMINI ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)