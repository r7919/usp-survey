from flask import Flask, render_template
from flask_wtf import FlaskForm

from wtforms import RadioField, SubmitField, FileField, TextAreaField

app = Flask(__name__)
app.config['SECRET_KEY']= '8d2c6184ae40cc9efdefe76c746248dd'
@app.route("/exp", methods=['GET', 'POST'])
def exp():
    form = ImageForm()
    if form.validate_on_submit():
        name = form.name.data
        # fileName = form.fileName.file.filename
        certification = form.certification.data
        return f"Name: {name}, certification: {certification}"
    return render_template("exp.html", form=form)


class ImageForm(FlaskForm):
    name = TextAreaField('name')
    # fileName = FileField('fileName')
    # certification = RadioField('certification', choices = ['option1', 'option2'])
    certification = RadioField('Label', choices=[('value','description'), ('value_two','whatever')])
    submit = SubmitField('Submit')
    



if __name__ =='__main__':
    app.run(debug=True)