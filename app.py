import json
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

with open('features.json') as f:
    FEATURES = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    q = request.args.get('q', '').lower()
    results = [feat for feat in FEATURES if q in feat['name'].lower() or q in feat['description'].lower()]
    return jsonify(results)

@app.route('/generate', methods=['POST'])
def generate():
    selected = request.json.get('features', [])
    script_lines = [next((f['script'] for f in FEATURES if f['name'] == name), '') for name in selected]
    script = "\n".join(script_lines)
    return jsonify({'script': script})

if __name__ == '__main__':
    app.run(port=5001, debug=True)
