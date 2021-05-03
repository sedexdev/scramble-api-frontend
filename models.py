from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash

from extensions import db


class AdminUser(db.Model):

    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow())
    modified = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow())
    last_login = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow())
    login_attempts = db.Column(db.Integer, default=0)

    def hash_pw(self, password: str) -> bool:
        return generate_password_hash(password, salt_length=12)

    def check_pw(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def verify_password(self, password: str) -> bool:
        length = len(password) > 12
        upper = any(x.isupper() for x in password)
        lower = any(x.islower() for x in password)
        digit = any(x.isdigit() for x in password)
        symbols = ['@', '!', '?', '_', '#', '£', '$', '%', '&', '*']
        symbol = False
        for x in password:
            for s in symbols:
                if x == s:
                    symbol = True
                    break
        return length and upper and lower and digit and symbol
