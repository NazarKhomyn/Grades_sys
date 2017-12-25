from Project.views import db


class Person:
    first_name = db.Column(db.String(100),nullable=False)
    second_name = db.Column(db.String(100),nullable=False)
    phone = db.Column(db.Numeric(12),nullable=False)



class Teacher(Person, db.Model):
    __tablename__ = "teacher"
    id = db.Column(db.Integer, primary_key=True)
    hire_date = db.Column(db.Date)
    subjects = db.relationship('TeacherSubject', backref='Teacher', lazy='dynamic')

    def __repr__(self):
        return 'Teacher id-{},{}'.format(self.id,self.second_name)

class Student(Person, db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    government_subsidized = db.Column(db.BOOLEAN)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    grades = db.relationship('Grade', backref='Student', lazy='dynamic')

    def __repr__(self):
        return 'Student id-{},{}'.format(self.id,self.second_name)


class Group(db.Model):
    __tablename__ = "group"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25),nullable=False)
    enter_date = db.Column(db.Date,nullable=False)
    students = db.relationship('Student', backref='Group', lazy='dynamic')
    courses = db.relationship('Course', backref='Group', lazy='dynamic')

    def __repr__(self):
        return 'Group %r' % self.name


class Subject(db.Model):
    __tablename__ = "subject"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25),nullable=False)
    description = db.Column(db.String(225),nullable=False)
    teachers = db.relationship('TeacherSubject', backref='Subject', lazy='dynamic')

    def __repr__(self):
        return 'Subject %r' % self.name


class TeacherSubject(db.Model):
    __tablename__ = "teacher_subject"
    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)
    subject_id = db.Column(db.Integer,db.ForeignKey('subject.id'), nullable=False)
    courses = db.relationship('Course', backref='TeacherSubject', lazy='dynamic')



class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    teacher_subject = db.Column(db.Integer, db.ForeignKey('teacher_subject.id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    grade = db.relationship('Grade', backref='Course', lazy='dynamic')



class Assignment(db.Model):
    __tablename__ = "assignment"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    description = db.Column(db.String(225))
    grades = db.relationship('Grade', backref='Assignment', lazy='dynamic')

    def __repr__(self):
        return 'Assignment %r' % self.name

class Grade(db.Model):
    __tablename__ = "grade"
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)
    data = db.Column(db.Date)
    course = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    student = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    assignment = db.Column(db.Integer, db.ForeignKey('assignment.id'), nullable=False)

db.create_all()
