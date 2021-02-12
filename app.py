from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])

def predict():
    return {"response": "YO"}

if __name__ == '__main__':
    app.run()
