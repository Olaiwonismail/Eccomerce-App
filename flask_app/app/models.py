from datetime import datetime
from app import db,login_manager
from flask_login import UserMixin
from flask import url_for, current_app
# from itsdangerous import URLSafeTimedSerializer as Serializer


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    firstname = db.Column(db.Text,unique=True,nullable=False)
    lastname = db.Column(db.Text,nullable=False)
    email = db.Column(db.Text,unique=True,nullable=False)
    image_file = db.Column(db.Text,nullable=False,default = 'image.png')
    password = db.Column(db.Text,nullable=False)
    wishlist = db.Column(db.Text,nullable=True)
    # posts = db.relationship('Post',backref = 'author',lazy =True)


    def __repr__(self):
        return f' User {self.username} ,{self.email} ,{self.image_file}'


class Product(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.Text,nullable=False)
    price = db.Column(db.Integer,nullable=False)
    description = db.Column(db.Text,nullable=False)
    # image = db.Column(db.String(100),nullable=False)
    thumbnail = db.Column(db.Text,nullable=False)
    stock = db.Column(db.Integer,nullable=False)
    brand = db.Column(db.Text,nullable=True)
    ratings = db.Column(db.Integer,nullable=False)
    # buyer = db.Column(db.Integer,nullable = True)
    # date_bought = db.Column(db.DateTime,nullable = True  )
    category = db.Column(db.Text,nullable=False)
    tags = db.Column(db.Text,nullable=False)
    returnPolicy = db.Column(db.Text,nullable=False)
    shippingInformation = db.Column(db.Text,nullable=False)
    reviews = db.Column(db.Text)


#
# class Product(db.Model):
#     id = db.Column(db.Integer,primary_key = True)
#     title = db.Column(db.String(40),nullable=False)
#     price = db.Column(db.Integer,nullable=False)
#     # image = db.Column(db.String(100),nullable=False)
#     thumbnail = db.Column(db.String(100),nullable=False)
#     stock = db.Column(db.Integer,nullable=False)
#     brand = db.Column(db.String(20),nullable=True)
#     ratings = db.Column(db.Integer,nullable=False)
#     # buyer = db.Column(db.Integer,nullable = True)
#     # date_bought = db.Column(db.DateTime,nullable = True  )
#     category = db.Column(db.String(40),nullable=False)
#     tags = db.Column(db.String(100),nullable=False)
#     returnPolicy = db.Column(db.String(100),nullable=False)
#     shippingInformation = db.Column(db.String(100),nullable=False)
    # reviews = db.Column(db.String(1000))

    # reviews
    # date_posted = db.Column(db.DateTime,nullable = False ,default =datetime.utcnow )
#     content = db.Column(db.Text,nullable=False)
#     user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
#
    # def __repr__(self):
    #     return f' User {self.title} ,{self.date_posted}'
