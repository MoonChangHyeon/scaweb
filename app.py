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
    lang = request.args.get('lang', '').lower()
    results = [feat for feat in FEATURES if lang in [l.lower() for l in feat.get('languages', [])]]
    return jsonify(results)

@app.route('/generate', methods=['POST'])
def generate():
    selected = request.json.get('features', [])
    script_lines = [next((f['script'] for f in FEATURES if f['name'] == name), '') for name in selected]
    script = "\n".join(script_lines)
    return jsonify({'script': script})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
