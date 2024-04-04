# Deployment of flask app with iris ki (ann)

- https://www.udemy.com/course/deep-learning-tensorflow chapter 20 Deployment
- demo : [https://iris-ann.onrender.com](https://iris-ann.onrender.com)

## Login with google to render.com account
- `https://dashboard.render.com`

## Install Miniconda if locally run
- https://docs.anaconda.com/free/miniconda

## Windows, Linux or MacOS x64 Intel (IMPORTANT: No M1 Mac supported with python version 3.7.0)
- `conda create --name tensorflow37 python=3.7.0`
- `conda activate tensorflow37`

## Installation of dependencies locally
- `pip install gunicorn`
- `pip install flask`
- `pip install Flask-WTF`
- `pip install tensorflow`
- `pip install scikit-learn`
- `pip install numpy`

- `pip freeze > requirements.txt`
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

## build
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

## generation of safed model and safed scaler see:
- [https://github.com/peterruler/iris-ann-ipynb](https://github.com/peterruler/iris-ann-ipynb)
