from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    number = IntegerField('Please enter your V-Number: (Leave off the V)', validators=[DataRequired()])
    name = StringField('Please enter your full name:', validators=[DataRequired()])
    email = StringField('Please enter your VCU email address:', validators=[DataRequired()])
    courseNumber = StringField('Please enter the course number for which you would like an override:', validators=[DataRequired()])
    sectionNumber = IntegerField('Please enter the section number for which you would like an override:', validators=[DataRequired()])
    courseReferenceNumber = IntegerField('Please enter the course reference number(CRN) for which you would like an override:', validators=[DataRequired()])
    reason = StringField('Please enter the reason why you are requesting override:', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
 

@app.route('/confirmation', methods=['GET', 'POST'])
def confirmation():
    return render_template('confirmation.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = NameForm()
    if form.validate_on_submit():
        return redirect(url_for('confirmation'))
    return render_template('home.html', form = form)