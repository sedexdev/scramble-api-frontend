from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')


class ResetForm(FlaskForm):

    email = StringField('Email', validators=[Email()])
    submit = SubmitField('Submit')


class UpdateForm(FlaskForm):

    password = PasswordField('Current Password', validators=[DataRequired()])
    new_pw = PasswordField('New Password', validators=[DataRequired()])
    confirm_pw = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Submit')
