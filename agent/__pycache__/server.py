from flask import Flask, request, jsonify
import json
import subprocess
import sys

app = Flask(__name__)

@app.route('/research', methods=['POST'])
def research():
    try:
        data = request.json
        result = subprocess.run(
            [sys.executable, 'runner.py', json.dumps(data)],
            capture_output=True,
            text=True,
            cwd='/Users/kindafaisalhotmail.com/Desktop/week5/project '
        )
        return jsonify(json.loads(result.stdout))
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)