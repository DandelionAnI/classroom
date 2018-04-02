# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class College(models.Model):
    collegeId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name


class Academy(models.Model):
    academyId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    brief = models.TextField(null=True, blank=True)
    college = models.ForeignKey(College)

    def __unicode__(self):
        return self.name


class Classroom(models.Model):
    classroomId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    maximum = models.IntegerField()
    college = models.ForeignKey(College)

    def __unicode__(self):
        return self.classroomId


class Major(models.Model):
    majorId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    academy = models.ForeignKey(Academy)
    college = models.ForeignKey(College)

    def __unicode__(self):
        return self.name


class Student(models.Model):
    studentId = models.AutoField(primary_key=True)
    number = models.CharField(max_length=50)
    password = models.CharField(max_length=50, default='000000')
    name = models.CharField(max_length=40)
    classes = models.CharField(max_length=40)
    college = models.ForeignKey(College)
    academy = models.ForeignKey(Academy, default='null')
    major = models.ForeignKey(Major)

    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    teacherId = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=40)
    belief = models.TextField(null=True, blank=True)
    academy = models.ForeignKey(Academy)
    college = models.ForeignKey(College)

    def __unicode__(self):
        return self.name


class Course(models.Model):
    courseId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    weekday = models.IntegerField(default=0)
    #date = models.DateField()
    start = models.IntegerField()
    end = models.IntegerField()
    classroom = models.ForeignKey(Classroom)
    teacher = models.ForeignKey(Teacher)
    college = models.ForeignKey(College)

    def __unicode__(self):
        return self.name


class Company(models.Model):
    companyId = models.AutoField(primary_key=True)
    account = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=60)
    address = models.TextField(max_length=100, null=True, blank=True)
    tel = models.CharField(max_length=60, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Choice(models.Model):
    switch = models.CharField(max_length=20)

    def __unicode__(self):
        return self.switch


class Activity(models.Model):
    activityId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    userId = models.CharField(max_length=60)
    tel = models.CharField(max_length=60)
    classroom = models.ForeignKey(Classroom)
    date = models.DateField()
    start = models.IntegerField()
    end = models.IntegerField()
    switch = models.ForeignKey(Choice, default=2)

    def __unicode__(self):
        return self.name
