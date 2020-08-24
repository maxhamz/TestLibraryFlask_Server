from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
# from dataclasses import dataclass
from src import db, login_manager, bcrypt
from flask_login import UserMixin
from marshmallow import fields, Schema

# additions @ postgresql
from flask_serialize import FlaskSerializeMixin

FlaskSerializeMixin.db = db


# class User(db.Model, UserMixin):
# @dataclass
# class User(db.Model):
class User(db.Model, FlaskSerializeMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    modified_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    books = db.relationship('Book', backref='users', lazy=True)
    

    __tablename__ = 'users'


    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        print("HELLO, THIS IS USER CONSTRUCTOR")
        print("test one, what is username?")
        # print(data.get('username'))
        self.username = data['username']
        self.email = data['email']
        # self.image_file = data.get('image_file')
        self.password = self.generate_hash(data['password']) # add this line
        self.created_at = datetime.utcnow()
        self.modified_at = datetime.utcnow()

    

    def save(self):
        db.session.add(self)
        db.session.commit()


    # def update(self, data):
    #     for key, item in data.items():
    #         if key == 'password': # add this new line
    #             self.password = self.__generate_hash(item) # add this new line
    #         setattr(self, key, item)
    #     self.modified_at = datetime.datetime.utcnow()
    #     db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    @staticmethod
    def get_all():
        return User.query.all()


    @staticmethod
    def get_one(id):
        return User.query.get(id)

    
    # add this new method
    @staticmethod
    def generate_hash(passwordInput):
        return bcrypt.generate_password_hash(passwordInput, rounds=10).decode("utf-8")
  
    # # add this new method
    # def check_hash(self, password):
    #     return bcrypt.check_password_hash(self.password, password)

    # add this new method
    @staticmethod
    def check_hash(stored, typed):
        return bcrypt.check_password_hash(stored, typed)

    # # serialize to JSON
    # def as_dict(self):
    #    return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    # serialize to JSON, STATIC METHOD
    @staticmethod
    def as_dict(thing):
       return {c.name: getattr(thing, c.name) for c in thing.__table__.columns}
    
    #  freeze
    # def get_reset_token(self, expires_sec=1800):
    #     s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
    #     return s.dumps({
    #         'user_id': self.id, 
    #         'username': self.username, 
    #         'email': self.email,
    #         'image_file': self.image_file
    #     }).decode('utf-8')
    
    # @staticmethod
    # def verify_reset_token(token):
    #     s = Serializer(current_app.config['SECRET_KEY'])
    #     try:
    #         user_id = s.loads(token)['user_id']
    #     except:
    #         return None
        
    #     userRaw = User.query.get(user_id).first_or_404()
    #     userJSON = userRaw
    #     return 






class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    author = db.Column(db.String(), nullable=False)
    published = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    illustration = db.Column(db.String(30), nullable=False, default='cover_default.jpg')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    modified_at = db.Column(db.DateTime, default=datetime.utcnow)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    __tablename__ = 'books'


    def __init__(self, data):
        self.title = data.get('title')
        self.author = data.get('author')
        self.published = data.get('published')
        self.illustration = data.get('illustration')
        self.owner_id = data.get('owner_id') # add this new line
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()
    

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
  
    @staticmethod
    def get_all():
        return Book.query.all()
  
    @staticmethod
    def get_one(id):
        return Book.query.get(id)




# add this new class
class BookSchema(Schema):
  """
  Book Schema
  """
  id = fields.Int(dump_only=True)
  title = fields.Str(required=True)
  author = fields.Str(required=True)
  published = fields.DateTime(dump_only=True)
  illustration = fields.Str(required=True)
  owner_id = fields.Int(required=True)
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)


# add this class
class UserSchema(Schema):
  """
  User Schema
  """
  id = fields.Int(dump_only=True)
  username = fields.Str(required=True)
  email = fields.Email(required=True)
  image_file = fields.Str(required=True)
  password = fields.Str(required=True)
  books = fields.Nested(BookSchema, many=True)
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)