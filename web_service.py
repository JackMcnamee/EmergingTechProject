# flask for web app.
import flask as fl
from flask import jsonify
# numpy for numerical work.
import numpy as np
from numpy import loadtxt
# tensor
import tensorflow as tf
from tensorflow import keras

# Create a new web app.
app = fl.Flask(__name__)

# https://machinelearningmastery.com/save-load-keras-deep-learning-models/
# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = keras.models.model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

# load dataset
dataset = loadtxt("Dataset.csv")
# seperate power and speed values
dataset_power = dataset.copy()
dataset_speed = dataset_power.pop("speed")

# Add root route.
@app.route("/")
def home():
  return app.send_static_file('index.html')

# Add power route.
@app.route('/api/power')
def power():
  data = {"value": np.random.uniform()}
  return jsonify(data)


# def ValuePredictor(to_predict_list):
#   to_predict = np.array(to_predict_list).reshape(1,2)
#   loaded_model = pickle.load(open("model.pkl", "rb"))
#   result = loaded_model.predict(to_predict)
#   return result[0]

# @app.route('/predict', methods = ['POST'])
# def result():
#   if request.method == 'POST':
#     to_predict_list = request.form.to_dict()
#     to_predict_list=list(to_predict_list.values())
#     to_predict_list = list(map(float, to_predict_list))
#     result = ValuePredictor(to_predict_list)
#     prediction = str(result)
#   return render_template("predict.html", prediction=prediction)

# if __name__ == "__main__":
#  app.run(debug=True)

