# flask for web app.
import flask as fl
from flask import request, render_template
# tensor
import tensorflow as tf
from tensorflow import keras

# create a web service
app = fl.Flask(__name__)

# add home route
@app.route('/', methods=["GET", "POST"])
def home():
  # Adapted from https://medium.com/techcrush/how-to-deploy-your-ml-model-in-jupyter-notebook-to-your-flask-app-d1c4933b29b5
  if request.method == "POST":
    # speed that user enters, cast to float
    wind_speed = request.form.get("speed")
    wind_speed = [float(wind_speed)]
    # load model compiled in jupyter notebook
    model = keras.models.load_model('model.h5')
    # output prediction
    prediction = model.predict(wind_speed)
    # returns home page with prediction
    return render_template('index.html', prediction=prediction[0])
  # returns home page
  return render_template('index.html')
