# from app.views import user_profile
from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # cryptos = db.relationship('Profile', backref='crypto', lazy='dynamic')
    # about_me = db.Column(db.String(140))
    # last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


# class Profile(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username_profile = db.Column(db.String(64), index=True, unique=True)
#     email_profile = db.Column(db.String(120), index=True, unique=True)
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#     def __repr__(self):
#         return f'<Profile {self.username_profile}>'


# Code to initialize db within code block as opposed to Flask-Migrate
# def init_db():
#     db.create_all()

#     # Create a test user
#     new_user = User('a@a.com', 'aaaaaaaa')
#     db.session.add(new_user)
#     db.session.commit()
#     db.session.commit()


# Miguel's table: keeping it here for now
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#     def __repr__(self):
#         return '<Post {}>'.format(self.body)


# if __name__ == '__main__':
#     init_db()
