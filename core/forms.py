from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import RadioField, SelectField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class APIForm(FlaskForm):

    service = SelectField(
        'Service Type',
        choices=[
            ('encrypt', 'Encryption'),
            ('hash', 'Hashing')
        ],
        validators=[DataRequired()])

    encryption = RadioField(
        'Encryption Types',
        choices=[
            ('rsa', 'RSA'),
            ('aes', 'AES')
        ])

    hashing = RadioField(
        'Hashing Algorithm',
        choices=[
            ('sha256', 'SHA3-256'),
            ('sha512', 'SHA3-512'),
        ]
    )

    plaintext = SelectField(
        'Plaintext Type',
        choices=[
            ('text', 'Text'),
            ('file', 'File')
        ],
        validators=[DataRequired()])

    text = TextAreaField('Plaintext')

    file_upload = FileField(
        'Upload file',
        validators=[
            FileRequired(),
            FileAllowed(['.txt', '.pdf', '.docx'], 'Text files only!')])

    submit = SubmitField('Submit')
