from django.contrib import admin
from .models import Student, Requirements, ClassShift, Schedule, Specialization, StudentProfile
#Register your models here.

admin.site.register(Student)
admin.site.register(Requirements)
admin.site.register(ClassShift)
admin.site.register(Schedule)
admin.site.register(Specialization)
admin.site.register(StudentProfile)


'''
from django.contrib import admin
from .models import Item, User
#Register your models here.
admin.site.register(Item)
admin.site.register(User)'''