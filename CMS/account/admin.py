# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Student, Academy, College, Classroom, Major, Course, Teacher, Company,Choice, Activity
from django.contrib import admin

# Register your models here.


admin.site.register([Student, Academy, College, Classroom, Major, Course, Teacher, Company, Choice, Activity,])
