from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class AdminForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AdminUpdateForm(FlaskForm):

    password = PasswordField('Current Password', validators=[DataRequired()])
    new_pw = PasswordField('New Password', validators=[DataRequired()])
    confirm_pw = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Submit')
