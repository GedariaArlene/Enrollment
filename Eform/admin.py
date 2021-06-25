from django.contrib import admin
from .models import Student, Requirements, Schedule, Specialization, Modality
#Register your models here.

admin.site.register(Student)
admin.site.register(Requirements)
admin.site.register(Schedule)
admin.site.register(Specialization)
admin.site.register(Modality)



'''
from django.contrib import admin
from .models import Item, User
#Register your models here.
admin.site.register(Item)
admin.site.register(User)'''



