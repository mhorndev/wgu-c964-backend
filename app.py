from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])

def predict():
    return {"response": "YO"}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 5000, debug=True)
