from flaskblog import db,login_manager,app
from datetime import datetime
from flask_login import UserMixin,current_user
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    post = db.relationship('Post',backref='author', lazy=True)
   # reply = db.relationship('Reply', backref='author1', lazy=True)
    
    def get_reset_token(self,expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'],expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),  nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    content = db.Column(db.Text(100),  nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #reply = db.relationship('Reply', backref='owner', lazy=True)

    def __repr__(self):
        return f"User('{self.title}','{self.date_posted}')"


class Reply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    replies = db.Column(db.Text)
    ruser = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

   # owner_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
   # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def __repr__(self):
        return f"User('{self.username}')"