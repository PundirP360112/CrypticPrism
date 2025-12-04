import os
import webbrowser
from flask import Flask, request, render_template_string

app = Flask(__name__)

def transform_text(text, key, action='encrypt'):
    result = []
    
    try:
        key = int(key)
    except ValueError:
        return text

    if action == 'decrypt':
        key = -key

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - start + key) % 26 + start
            result.append(chr(shifted))
        elif char.isdigit():
            start = ord('0')
            shifted = (ord(char) - start + key) % 10 + start
            result.append(chr(shifted))
        else:
            result.append(char)
            
    return "".join(result)

def brute_force_attack(text):
    results = []
    for i in range(1, 27):
        attempt = transform_text(text, i, 'decrypt')
        results.append(f"Shift -{i:02d}: {attempt}")
    return "\n".join(results)

HTML_GUI = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Caesar Web App</title>
    <style>
        body { font-family: sans-serif; background: #2c3e50; color: white; display: flex; justify-content: center; padding-top: 50px; }
        .container { background: #ecf0f1; color: #2c3e50; padding: 30px; border-radius: 10px; width: 500px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
        h1 { text-align: center; color: #e74c3c; }
        textarea { width: 100%; height: 100px; padding: 10px; margin: 10px 0; border: 2px solid #bdc3c7; border-radius: 5px; font-size: 16px; box-sizing: border-box;}
        input[type="number"] { width: 100%; padding: 10px; margin: 10px 0; border: 2px solid #bdc3c7; border-radius: 5px; font-size: 16px; box-sizing: border-box;}
        .btn-group { display: flex; gap: 10px; }
        button { flex: 1; padding: 15px; border: none; cursor: pointer; font-weight: bold; font-size: 16px; color: white; border-radius: 5px; transition: 0.3s; }
        .btn-enc { background: #27ae60; } .btn-enc:hover { background: #2ecc71; }
        .btn-dec { background: #2980b9; } .btn-dec:hover { background: #3498db; }
        .btn-brute { background: #e67e22; width: 100%; margin-top: 10px;} .btn-brute:hover { background: #d35400; }
        .result-box { background: #34495e; color: #ecf0f1; padding: 15px; margin-top: 20px; border-radius: 5px; min-height: 50px; white-space: pre-wrap; font-family: monospace; }
        label { font-weight: bold; }
    </style>
</head>
<body>

<div class="container">
    <h1>Caesar Cipher Web Tool</h1>
    <form method="POST">
        <label>Message:</label>
        <textarea name="message" placeholder="Enter text here...">{{ message }}</textarea>
        
        <label>Shift Key (Number):</label>
        <input type="number" name="shift" value="{{ shift }}" min="1">
        
        <div class="btn-group">
            <button type="submit" name="action" value="encrypt" class="btn-enc">Encrypt</button>
            <button type="submit" name="action" value="decrypt" class="btn-dec">Decrypt</button>
        </div>
        <button type="submit" name="action" value="brute" class="btn-brute">Brute Force (Crack)</button>
    </form>

    {% if result %}
    <div class="result-box">
        <strong>Result:</strong><br><br>{{ result }}
    </div>
    {% endif %}
</div>

</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    message = ""
    shift = 3

    if request.method == 'POST':
        message = request.form.get('message', '')
        shift_val = request.form.get('shift', '3')
        action = request.form.get('action')

        try:
            shift = int(shift_val)
        except ValueError:
            shift = 3

        if action == 'encrypt':
            result = transform_text(message, shift, 'encrypt')
        elif action == 'decrypt':
            result = transform_text(message, shift, 'decrypt')
        elif action == 'brute':
            result = brute_force_attack(message)

    return render_template_string(HTML_GUI, result=result, message=message, shift=shift)

if __name__ == '__main__':
    print("Starting Web App...")
    webbrowser.open("http://127.0.0.1:5000")
    
    app.run(debug=True, use_reloader=False)