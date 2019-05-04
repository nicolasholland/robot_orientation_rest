Robot Orientation Recognition Rest Api
======================================

There's model.py which creates a model.pkl containing an sklearn model for recognising room orientations from kmeans cluster centers.
The cluster centers should be computed from imges from a camera mounted on my cleaning robot.

There's a server.py which is used to start a flask server.
It implements a rest api which accepts jsonfied images and returns propabilities for which orientation the camera could have had when taking the image.

There's a request.py which was used for tests.

The model.pkl was created by the model.py

The images folder contains images used for model training.

We learned how to deploy an application on heroku from [here](https://barnesanalytics.com/publishing-a-bokeh-app-to-heroku).

Server can be started with

```
$ FLASK_APP=server.py flask run --port $PORT
```
