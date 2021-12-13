from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, IntegerField,DateTimeField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=80)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Messaage', validators=[DataRequired(), Length(min=5, max=200)])
    submit = SubmitField('submit')

class AdminForm(FlaskForm):
    name = StringField('Name')
    password = PasswordField('Password')
    submit = SubmitField('submit')