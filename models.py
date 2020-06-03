from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class Book(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    price=db.Column(db.Integer)
    filename=db.Column(db.String(100))
    student_id=db.Column(db.Integer,db.ForeignKey('student.id'))
    
    def __repr__(self):
        return '<Book %r>' % self.id

class Student(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20),nullable=False)
    profile_pic=db.Column(db.String(100))
    book=db.relationship('Book',backref='student',uselist=False)
    addresses=db.relationship('Address',backref='student')

class Address(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    addr=db.Column(db.String(200),nullable=False)
    student_id=db.Column(db.Integer,db.ForeignKey('student.id'))

    def __repr__(self):
        return self.addr

subs = db.Table('subs',
        db.Column('book_id',db.Integer,db.ForeignKey('audiobook.id')),
        db.Column('user_id',db.Integer,db.ForeignKey('listener.id'))
        )

class AudioBook(db.Model):
    __tablename__='audiobook'
    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    author=db.Column(db.String(20),nullable=False)
    speaker=db.Column(db.String(20),nullable=False)
  
    def __repr__(self):
        return self.name

class Listener(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    profile_pic=db.Column(db.String(100))
    name=db.Column(db.String(20),nullable=False)
    subscriptions=db.relationship('AudioBook',secondary=subs,
    backref=db.backref('subscribers',lazy='dynamic'))

    def __repr__(self):
        return self.name
