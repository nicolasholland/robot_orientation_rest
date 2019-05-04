Robot Orientation Recognition Rest Api
======================================

There's model.py which creates a model.pkl containing an sklearn model for recognising room orientations from kmeans cluster centers.
The cluster centers should be computed from imges from a camera mounted on my cleaning robot.

There's a server.py which is used to start a flask server.
It implements a rest api which accepts jsonfied images and returns propabilities for which orientation the camera could have had when taking the image.

There's a request.py which was used for tests.

The model.pkl was created by the model.py

The images folder contains images used for model training.


Server can be started with

```
$ FLASK_APP=server.py flask run --port $PORT
```

We had the idea to run this on heroku after reading [this](https://barnesanalytics.com/publishing-a-bokeh-app-to-heroku).
First thing we learned was we need something called gunicorn.

Rest api is available on [https://robotorientationrest.herokuapp.com/api](https://robotorientationrest.herokuapp.com/api)

