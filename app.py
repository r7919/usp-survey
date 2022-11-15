import os
import datetime
from flask import Flask, render_template, url_for, flash, redirect, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required
import random

app = Flask(__name__)

app.config['SECRET_KEY']= '8d2c6184ae40cc9efdefe76c746248dd'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///ishan.db'

db=SQLAlchemy(app)


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    num_interfaces = 2
    form = SurveyForm(random.randint(1, num_interfaces))
    if form.validate_on_submit():
        response = Response(res1=form.res1.data, res2=form.res2.data, res3=form.res3.data, interface_id=app.interface_id)
        db.session.add(response)
        db.session.commit()
        flash(f'Survey form submitted, yay!','success')
        return redirect(url_for('home'))
    app.interface_id = form.interface_id
    return render_template('survey.html', form=form)


class Response(db.Model):
    '''
    Survey Response store karega
    '''
    id = db.Column(db.Integer, primary_key=True)
    res1 = db.Column(db.String, nullable=False)
    res2 = db.Column(db.String, nullable=False)
    res3 = db.Column(db.String, nullable=False)
    interface_id = db.Column(db.String, nullable=False)

class SurveyForm(FlaskForm):
    res1 = StringField('Q1', validators=[DataRequired()])
    res2 = SelectField('Q2', choices=[('c1', 'Choice 1'), ('c2', 'Choice2')])
    res3 = RadioField('Q3', choices=[('Agree', 'Agree'), ('Neutral', 'Neutral'), ('Disagree', 'Disagree')], validators=[DataRequired()])
    submit=SubmitField('Submit')

    def __init__(self, interface_id):
        super().__init__()
        self.interface_id = interface_id


if __name__ =='__main__':
    db.create_all()
    app.run(debug=True)