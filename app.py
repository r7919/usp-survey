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




@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
def home():
    return render_template('home.html')

@app.route("/survey", methods=['GET', 'POST'])
def survey():
    num_interfaces = 2
    
    interface_1_id = random.randint(1, num_interfaces)
    interface_2_id = random.randint(1, num_interfaces)
    while interface_1_id == interface_2_id:
        interface_2_id = random.randint(2, num_interfaces)
    
    form = SurveyForm(interface_1_id, interface_2_id)
    
    if form.validate_on_submit():
        print(form.data)
        try:
            response = Response(pre_1=form.pre_1.data, pre_2=form.pre_2.data, pre_3=form.pre_3.data, pre_4=form.pre_4.data, pre_5=form.pre_5.data, pre_6=form.pre_6.data,
                    post_1=form.post_1.data, post_2=form.post_2.data, post_3=form.post_3.data, post_4=form.post_4.data,
                    post_5=form.post_5.data, post_6=form.post_6.data, post_7=form.post_7.data, post_8=form.post_8.data,
                    interface_1_id=app.interface_1_id, interface_2_id=app.interface_2_id)
            db.session.add(response)
            db.session.commit()
        except Exception as exc:
            print(f"error : {exc}")
        flash(f'Thanks for your time, the survey form has been submitted successfully, yay! ','success')
        return redirect(url_for('home'))
    app.interface_1_id = form.interface_1_id
    app.interface_2_id = form.interface_2_id
    return render_template('survey.html', form=form)


class Response(db.Model):
    '''
    Survey Response store karega
    '''
    id = db.Column(db.Integer, primary_key=True)
    pre_1 = db.Column(db.String, nullable=False)
    pre_2 = db.Column(db.String, nullable=False)
    pre_3 = db.Column(db.String, nullable=False)
    pre_4 = db.Column(db.String, nullable=False)
    pre_5 = db.Column(db.String, nullable=False)
    pre_6 = db.Column(db.String, nullable=False)
    post_1 = db.Column(db.String, nullable=False)
    post_2 = db.Column(db.String, nullable=False)
    post_3 = db.Column(db.String, nullable=False)
    post_4 = db.Column(db.String, nullable=False)
    post_5 = db.Column(db.String, nullable=False)
    post_6 = db.Column(db.String, nullable=False)
    post_7 = db.Column(db.String, nullable=False)
    post_8 = db.Column(db.String, nullable=False)
    interface_1_id = db.Column(db.String, nullable=False)
    interface_2_id = db.Column(db.String, nullable=False)
class SurveyForm(FlaskForm):
    pre_1 = RadioField("Do you understand what is meant by an IP address ? (An example address might be 192.158.1.38)", choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    pre_2 = SelectField("Which of the following represents an Operating System(OS) ?", choices=[('google', 'https://Google.com/'), ('edge', 'Microsoft Edge'), ('windows', 'Microsoft Windows'), ('none', 'None')], validators=[DataRequired()])
    pre_3 = SelectField("Which of the following represents a Web browser ?", choices=[('google', 'https://Google.com/'), ('edge', 'Microsoft Edge'), ('windows', 'Microsoft Windows'), ('none', 'None')], validators=[DataRequired()])
    pre_4 = RadioField("Have you heard about 2-Factor Authentication ?", choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    pre_5 = RadioField("Have you ever used 2-Factor Authentication ?", choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    pre_6 = RadioField("Have you ever used password managers ?", choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])

    post_1 = RadioField("Have you ever seen this kind of notification before?", choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    post_2 = RadioField("How likely are you to change your passsword after recieving such a notification?", choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], validators=[DataRequired()])
    post_3 = RadioField("How likely are you to enable 2-Factor Authentication after recieving such a notification?", choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], validators=[DataRequired()])
    post_4 = RadioField("How likely are you to opt out of such noficiations?", choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], validators=[DataRequired()])
    post_5 = RadioField("Have you ever seen this kind of notification before?", choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    post_6 = RadioField("How likely are you to change your passsword after recieving such a notification?", choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], validators=[DataRequired()])
    post_7 = RadioField("How likely are you to enable 2-Factor Authentication after recieving such a notification?", choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], validators=[DataRequired()])
    post_8 = RadioField("How likely are you to opt out of such noficiations?", choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], validators=[DataRequired()])
    
    # res1 = StringField('Q1', validators=[DataRequired()])
    # res2 = SelectField('Q2', choices=[('c1', 'Choice 1'), ('c2', 'Choice2')])
    # res3 = RadioField('Q3', choices=[('Agree', 'Agree'), ('Neutral', 'Neutral'), ('Disagree', 'Disagree')], validators=[DataRequired()])
    submit=SubmitField('Submit')

    def __init__(self, interface_1_id, interface_2_id):
        super().__init__()
        self.interface_1_id = interface_1_id
        self.interface_2_id = interface_2_id

if __name__ =='__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')