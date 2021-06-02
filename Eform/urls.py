from django.urls import path
from . import views 

urlpatterns = [
	path ('',views.EStudent),
	path('students', views.Page, name="students"),

]

#	path ('',views.StudentList),
#	path('studentlist', views.Student, name="studentlist"),
	


'''
urlpatterns = [
	path ('',views.Omepage),
	path('students', views.Page, name="students"),
	
]'''