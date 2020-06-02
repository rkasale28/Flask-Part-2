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
