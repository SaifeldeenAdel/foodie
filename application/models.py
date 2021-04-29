from application import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    recipes = db.relationship('Recipes', backref='', lazy=True)

    def __repr__(self):
        return f"User ('{self.id}','{self.username}', '{self.password}')"

class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    uri = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=True) 
    url = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    

    def __repr__(self):
        return f"{self.user_id}, {self.name}"