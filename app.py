from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/sum', methods=['POST'])
def suma():
    data = request.get_json()
    a = data.get('a', 0)
    b = data.get('b', 0)
    
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return jsonify({"error": "Los valores deben ser números"}), 400
    
    result = a + b
    return jsonify({"result": result})

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    a = data.get('a', 0)
    b = data.get('b', 0)
    
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return jsonify({"error": "Los valores deben ser números"}), 400
    
    result = a * b
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
