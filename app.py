from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import NumberRange
from tensorflow.keras.models import load_model  
import numpy as np 
import pickle

def return_prediction(model,scaler,sample_json):
    
    s_len = sample_json['sepal_length']
    s_wid = sample_json['sepal_width']
    p_len = sample_json['petal_length']
    p_wid = sample_json['petal_width']
    
    flower = [[s_len,s_wid,p_len,p_wid]]
    flower = scaler.transform(flower)
    
    classes = np.array(['setosa', 'versicolor', 'virginica'])

    predict_x=model.predict(flower) 
    class_ind=np.argmax(predict_x,axis=1)
    
    return classes[class_ind][0]

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

flower_model = load_model("final_iris_model.h5")
scaler = pickle.load(open('scaler.sav', 'rb'))

class FlowerForm(FlaskForm):
    sep_len = StringField('Sepal Length')
    sep_wid = StringField('Sepal Width')
    pet_len = StringField('Petal Length')
    pet_wid = StringField('Petal Width')

    submit = SubmitField('Analyze')

@app.route('/', methods=['GET', 'POST'])
def index():

    form = FlowerForm()
    if form.validate_on_submit():

        session['sep_len'] = form.sep_len.data
        session['sep_wid'] = form.sep_wid.data
        session['pet_len'] = form.pet_len.data
        session['pet_wid'] = form.pet_wid.data

        return redirect(url_for("prediction"))

    return render_template('home.html', form=form)


@app.route('/prediction')
def prediction():
    content = {}

    content['sepal_length'] = float(session['sep_len'])
    content['sepal_width'] = float(session['sep_wid'])
    content['petal_length'] = float(session['pet_len'])
    content['petal_width'] = float(session['pet_wid'])

    results = return_prediction(model=flower_model,scaler=scaler,sample_json=content)

    return render_template('prediction.html',results=results)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000) 
