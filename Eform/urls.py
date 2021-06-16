from django.urls import path
from . import views 

urlpatterns = [
	path ('',views.EStudent),
	path('students', views.List, name="students"),
	path('requirement.html', views.Require, name="requirement.html"),
	path('specialization.html', views.Special, name="specialization.html"),
	path('shifts.html', views.Shift, name="shifts.html"),
	path('schedule.html', views.Sched, name="schedule.html"),	
]
	#path ('',views.Page),
	#path('requirement', views.Requirements, name="requirement"),



#	path ('',views.StudentList),
#	path('studentlist', views.Student, name="studentlist"),
	


'''
urlpatterns = [
	path ('',views.Omepage),
	path('students', views.Page, name="students"),
	
]'''