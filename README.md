# Emerging Technologies Project
***
A web service that uses machine learning to make predictions based on a data set that contains wind speed and wind turbine power values. Enter a wind speed value to receive the corresponding wind turbine power output.

## How to run
***
### Requirements
* Python 3.8.5
* Flask 1.1.2
* Tensorflow 2.4.0


### Linux
```
export FLASK_APP=web_service.py 
python3 -m flask run 
```

### Windows
```
set FLASK_APP=web_service.py 
python -m flask run 
```

### How to build and run Dockerfile
```
docker build . -t web-service
docker run -d -p 5000:5000 web-service
```
