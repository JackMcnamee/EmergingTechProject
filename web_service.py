# flask for web app.
import flask as fl
from flask import jsonify
# numpy for numerical work.
import numpy as np

# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/")
def home():
  return app.send_static_file('index.html')

# Add power route.
@app.route('/api/normal')
def power():
  data = {"value": np.random.normal()}
  return jsonify(data)