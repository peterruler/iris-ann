# Deployment of Flask App with Iris KI (ANN)

- [Udemy Course: Deep Learning with TensorFlow](https://www.udemy.com/course/deep-learning-tensorflow) - Chapter 20: Deployment
- Demo: [https://iris-ann.onrender.com](https://iris-ann.onrender.com)
- Please wait for approx. 2 min. until the queued webservice (due to long inactivity) is restarted.

## Login with Google to Render.com Account
- [Render Dashboard](https://dashboard.render.com)
- Better login via GitHub.com so you can deploy by using this (e.g. forked) repo.
- For deployment, it's easiest to use a GitHub repository.
- Choose the free plan with 512 MB and 0.1 CPU.

## Install Miniconda if Running Locally
- [Miniconda Installation Guide](https://docs.anaconda.com/free/miniconda)

## Windows, Linux, or macOS x64 Intel (IMPORTANT: No M1 Mac supported with Python version 3.7.0)
```sh
conda create --name tensorflow37 python=3.7.0
conda activate tensorflow37
```

## Installation of dependencies locally (optional)
- `pip install gunicorn`
- `pip install flask`
- `pip install Flask-WTF`
- `pip install tensorflow`
- `pip install scikit-learn`
- `pip install numpy`

- `pip freeze > requirements.txt` # dont do this
- Optional:
- `pip show <PACKAGE>` check versions of package
- Content of requirements.txt, don't neet to regenerate:
```
Flask==2.0.3
Flask-WTF==0.15.1
gunicorn==20.1.0
joblib==1.1.1
scikit-learn==0.21.3
scipy==1.5.2
tensorflow==2.6.2
werkzeug==2.0.3
```

## run locally
- `conda activate tensorflow37`

## build (do this to install dependencies)
- `pip install -r requirements.txt`

## Set Env Vars in render.com choose app then choose Environment menu item
 - Only thing needed for sure is: `PYTHON_VERSION` / `3.7.7`
 - and maybe:
 - `PORT` / `5000`
 - optional:
 - `PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION` / `python`

 ## Start command
 - replace: `gunicorn app:app`
 - dont use: `gunicorn --timeout 600 --bind 0.0.0.0:$PORT app:app` # timeout error
 - instead use:
- `python app.py` #also in render backend configuration

## generation of saved model and saved scaler see:
- [https://github.com/peterruler/iris-ann-ipynb](https://github.com/peterruler/iris-ann-ipynb)
