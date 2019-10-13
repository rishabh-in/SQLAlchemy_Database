import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir=os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+os.path.join(basedir,"data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db=SQLAlchemy(app)

Migrate(app,db)

#####################################

class Student(db.Model):

    __tablename__= "Students"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)

    ## One to Many Relation
    ## One Student --> Many Subjects

    subject=db.relationship("Subject",backref="student",lazy="dynamic")

    ## One to One Relation
    ## One student --> One Class_room

    class_room=db.relationship("Class_room",backref="student",uselist=False)

    def __init__(self,name):
        self.name=name

    def __repr__(self):
        if self.class_room:
            return "I am {} from {} class".format(self.name,self.class_room.class_name)

        else:
            return "I am {}.I have not decided my class yet!!".format(self.name)

    def report_subject(self):
        print("Here is the list of my Subjects")
        for subject in self.subject:
            print(subject.subject_name)

class Subject(db.Model):

    __tablename__="Subjects"

    subject_id=db.Column(db.Integer,primary_key=True)
    subject_name=db.Column(db.Text)

    student_ID=db.Column(db.Integer,db.ForeignKey("Students.id"))

    def __init__(self,subject_name,student_ID):

        self.subject_name=subject_name
        self.student_ID=student_ID

class Class_room(db.Model):

    __tablename__="ClassRoom"

    class_id=db.Column(db.Integer,primary_key=True)
    class_name=db.Column(db.Text)

    student_ID = db.Column(db.Integer, db.ForeignKey("Students.id"))

    def __init__(self,class_name,student_ID):

        self.class_name=class_name
        self.student_ID=student_ID


