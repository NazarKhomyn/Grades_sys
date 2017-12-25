from . import app
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/students2'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from . import models
admin = Admin(app,'Grade sys', url='/')
db.create_all()


admin.add_view(ModelView(models.Student, db.session))
admin.add_view(ModelView(models.Teacher, db.session))
admin.add_view(ModelView(models.Subject, db.session))
admin.add_view(ModelView(models.TeacherSubject, db.session))
admin.add_view(ModelView(models.Course, db.session))
admin.add_view(ModelView(models.Group, db.session))

