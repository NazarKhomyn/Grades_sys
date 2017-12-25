from Project.views import db


class Person:
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))



class Teacher(Person, db.Model):
    id = db.Column('teacher_id', db.Integer, primary_key=True)
   # subjects = db.relationship('')




class Group(db.Model):
    __tablename__ = "group"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    students = db.relationship('Student',backref='Group',lazy='dynamic')

class Student(Person, db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)



class Subject(db.Model):
    id = db.Column('teacher_id', db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    description = db.Column(db.String(225))



class TeacherSubject(db.Model):
    id = db.Column('teacher_subject_id', db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('Teacher.id'), nullable=False)
    subject_id = db.Column(db.Integer,db.ForeignKey('Subject.id'), nullable=False)





class Course(db.Model):
    id = db.Column('Course_id', db.Integer, primary_key=True)
    teacher_subject = db.Column(db.Integer, db.ForeignKey(TeacherSubject.id), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey(Group.id), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey(Teacher.id), nullable=False)

db.create_all()
