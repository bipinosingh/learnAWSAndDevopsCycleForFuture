from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "My First Flask API!"

@app.route('/health')
def health():
    return "API is healthy!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)