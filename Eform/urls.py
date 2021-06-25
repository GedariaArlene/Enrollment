from django.contrib import admin
from django.urls import path
from . import views 
from django.conf.urls import url 

urlpatterns = [
	path ('',views.EStudent),
	path('students', views.List, name="students"),
	path('requirement.html', views.Requirements, name="requirement"),
	path('specialization.html', views.Specialization, name="specialization"),
	path('modality.html', views.Modality, name="modality"),	
	path('schedule.html', views.Schedule, name="schedule"),	
	path('Done.html', views.Done, name="Done"),	

	url(r'^EditList/(?P<id>\d+)$', views.EditList, name="EditList"),
	url(r'^EditList/UpdateList/(?P<id>\d+)$', views.UpdateList, name="UpdateList"),
	url(r'^DeleteList/(?P<id>\d+)$', views.DeleteList, name="DeleteList"),

	path('EStudent.html', views.Home, name="EStudent"),	
	path('students.html', views.Masterlist, name="students"),	
]

#path('edit/<int:id>', views.edit),  
#path('update/<int:id>', views.update),  
#path('delete/<int:id>', views.destroy),
