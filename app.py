from flask import Flask, request, jsonify
import os
import pandas
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))

@app.route('/', methods=['POST'])

def post():
  # read request body
    data = request.get_json(force=True)

    # convert request body into a dataframe
    data.update((x, [y]) for x, y in data.items())
    dataframe = pandas.DataFrame.from_dict(data)

    # predictions
    prediction = model.predict(dataframe)
    
    # return data
    return jsonify(cost=int(prediction[0]))

port = int(os.environ.get('PORT', 8080))

if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)
