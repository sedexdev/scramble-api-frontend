from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import RadioField, SubmitField, TextAreaField


class APIForm(FlaskForm):

    encryption = RadioField(
        'Encryption Type',
        choices=[
            ('rsa', 'RSA'),
            ('aes', 'AES')
        ])

    hashing = RadioField(
        'Hashing Algorithm',
        choices=[
            ('md5', 'MD5*'),
            ('blake2b', 'BLAKE2b'),
            ('blake2s', 'BLAKE2s'),
            ('pbkdf2_hmac', 'PBKDF2-HMAC'),
            ('sha1', 'SHA-1*'),
            ('sha224', 'SHA-224'),
            ('sha256', 'SHA-256'),
            ('sha384', 'SHA-384'),
            ('sha512', 'SHA-512'),
            ('sha3_224', 'SHA3-224'),
            ('sha3_256', 'SHA3-256'),
            ('sha3_384', 'SHA3-384'),
            ('sha3_512', 'SHA3-512'),
            ('shake_128', 'SHAKE-128'),
            ('shake_256', 'SHAKE-256'),
        ]
    )

    text = TextAreaField('Paste Plaintext')

    file_upload = FileField(
        'Upload file',
        validators=[
            FileAllowed(['.txt', '.pdf', '.docx'], 'Text files only!')])

    submit = SubmitField('Submit')
